#coding=utf-8

import shutil
import os
import time
import zipfile
import mylog
import psutil
import model
import subprocess
import sys 

#将log日志设为全局变量 是否有更好方法再说
mylog = mylog.initlog()

class rule(object):
    """升级、备份、替换测试程序"""
    def __init__(self):
        super(rule, self).__init__()

    def do_update(self,updatepath):
        """从svn更新最新程序(不管有没更新都会进行后续操作，需优化)"""
#        updatepath = self.updatepath
        #检查路径是否为目录
        if os.path.isdir(updatepath):
            try:
                updateshell = 'TortoiseProc.exe /command:update /path:"%s" /closeonend:1'%updatepath
                os.system(updateshell)
                mylog.info('升级成功')
                return True
            except Exception,msg:
                mylog.error('升级失败，%s'%msg)
                return False
        else:
            mylog.error('升级失败，升级目录不合法')
            return False


    
    def start_app(self,startpath,updatepath,command):
        '''起程序'''
#        startpath = self.startpath
#        updatepath = self.updatepath
        apppath = os.path.split(startpath)[0]
        apppname = os.path.split(startpath)[1]
#        command = self.command
        #print startpath
        if os.path.isfile(startpath):
            try:
                os.chdir(apppath)#如果启动程序不在第一层目录下？ 需优化
#                #os.system(startpath)#启动程序后应该退出脚本，现没有退出 一直占用资源 需优化【用start app或 execl解决】
#                os.system('start %s' %apppname) 
#                #os.execl(startpath,'i') #直接退出进程
#                #规避删除目录error32错误，临时解决方法
                #os.chdir(updatepath)
                #bug3 os.system执行后进程不带路径导致close失败
                if command is None:
                    subprocess.Popen(startpath)
                else:
                    subprocess.Popen([command,startpath])

                #bug1 规避删除目录error32错误，临时解决方法
                os.chdir(updatepath)
                mylog.info('启动服务成功')
                return True
#                subprocess.Popen(startpath, shell=True)
            except Exception,msg:
                mylog.error('启动服务失败，%s'%msg)
                return False
        else:
            mylog.error('启动服务失败，启动命令错误')
            return False

        #sys.exit()


    def close_app(self,startpath):
        '''关闭程序进程'''
#        startpath = self.startpath
#        try:
#            closeshell = 'taskkill /f /im %s'%startpath
#            os.system(closeshell)
#        except Exception,msg:
#            print msg
#            return False
        startpath = self.startpath
#        print startpath
        pid = self.check_process(startpath)
        if pid:
            try:
                psutil.Process(pid).kill()
                mylog.info('关闭服务成功,进程号为%s'%pid)
                return True
            except Exception,msg:
                mylog.error('关闭服务失败，%s'%msg)
                return False
        else:
            mylog.warning('关闭服务失败，服务未启动')
            return True
        


 
    def zip_dir(self,copypath,testpath):
        '''打包备份'''
#        copypath = self.copypath
#        testpath = self.testpath
        nowtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
        if os.path.isdir(copypath):
            zipFile1 = zipfile.ZipFile(os.path.join(copypath,os.path.basename(testpath)+nowtime+'.zip'),'w') 
        else:
            mylog.error('备份失败，备份目录不合法')
            return False
        #用宽度优先搜索全路径
        if os.path.isdir(testpath):
            filelist = os.listdir(testpath)
            while len(filelist)>0:
                out = filelist.pop()
                if os.path.isdir(os.path.join(testpath,out)):
                    #os.path.join(os.path.basename(testpath),out) 短目录替换全路径
                    #out 当前路径
                    zipFile1.write(os.path.join(testpath,out),out)
                    for outfile in os.listdir(os.path.join(testpath,out)):
                        filelist.append(os.path.join(out,outfile))
                else:
                    zipFile1.write(os.path.join(testpath,out),out)
        else:
            mylog.error('备份失败，测试目录不合法')
            return False
        #用os.walk搜索全路径下文件,还不能做到压缩目录不带全路径
        """for dirpath, dirnames, filenames in os.walk(testpath):
            
            for filename in filenames:   
            #print filename
                zipFile1.write(os.path.join(dirpath,filename))"""        
        zipFile1.close() 
        mylog.info('备份成功')
        return True 
       
    def replace_app(self,updatepath,testpath):
        ''' 更新程序'''
#        updatepath  = self.updatepath
#        testpath = self.testpath
#        shutil.rmtree(testpath)
        try:
            #time.sleep(3)
            shutil.rmtree(testpath)

          
        except  Exception,msg:
            mylog.error('删除测试目录失败 %s'%msg)
            return False  

        try:
            shutil.copytree(updatepath,testpath)
            #插入当前时间做更新时间
            db = model.depdb()
            #sqllite接受utf-8格式 所以要转码
            db.updatetime(updatepath.decode('gbk').encode('utf-8'),testpath.decode('gbk').encode('utf-8'))
            mylog.info('更新成功')
            return True
        except  Exception,msg:
            mylog.error('替换更新文件失败 %s'%msg)
            return False        

    def conn_pc(self,path=None,user=None,psd=None):
        shell = r'NET USE "%s" "%s" /user:"%s"'%(path,psd,user)
        #print shell
        try:
            os.popen(shell)
            return True
        except Exception,msg:
            print msg
            return False  


    def check_process(self,path):                                                    
        """查找是否有对应pid"""                                                             
        path = path.decode('gbk').encode('utf-8')
        path_list = path.split(' ')                               
        pid_list = psutil.get_pid_list()
        sub_list = []
        for pid in pid_list:                                                         
            cmdline = psutil.Process(pid).cmdline
            #print cmdline
            if path in cmdline:
                mylog.info('程序进程号为 %s'%pid)
                return pid
            #bug2 执行路径 调用路径有空格 以及部分路径重复都能处理；其他情况未知
            elif set(path_list).issubset(cmdline):
                for i in xrange(len(cmdline)):
                    if cmdline[i]==path_list[0]:
                        sub_list.append(cmdline[i:i+len(path_list)])
                    if path_list in sub_list:
                        mylog.info('程序进程号为 %s'%pid)
                        return pid
        mylog.info('未找到程序进程')
        return False                                            
        #bug 2 修复路径中有空格不能正确处理的bug 默认路径间只有一个空格//处理有误 注释掉重写                                    
#            if  len(cmdline)>2:                                                      
#                cmdline[1]=reduce(lambda x,y : x+' '+y,cmdline[1:])                  
##                print  cmdline                                                      
#            for i in cmdline:                                                        
#                if i==path:                                                          
#                    return pid                                                       
#                                                                                                                                                                                                                   
#         print psutil.Process(5060).cmdline[1:]                                  
#         #用cmdline 应对脚本调用其他exe的情况;列表中编码为utf-8 编解码搞死人                             
#         if path.decode('gbk').encode('utf-8') in psutil.Process(pid).cmdline:   
#              print pid                                                          
#              return pid                                                         
#         return False    
    def opendir(self,path):
        os.startfile(path)
                                                                

class cont_app(rule):
    """增加此类 继承rule 实现业务逻辑"""
    def __init__(self,updatepath,testpath,copypath,startpath,command=None):
        super(cont_app, self).__init__()
        #bug 5 脏数据引起和bug4原因一样，数据字段已为必填，可规避此问题
        self.updatepath = os.path.normpath(updatepath.decode('utf-8').encode('gbk'))
        self.testpath = os.path.normpath(testpath.decode('utf-8').encode('gbk'))
        self.copypath = os.path.normpath(copypath.decode('utf-8').encode('gbk'))
        self.startpath = os.path.normpath(startpath.decode('utf-8').encode('gbk'))
        self.command = command

    def do(self):
        updatepath = self.updatepath
        testpath = self.testpath
        copypath = self.copypath
        startpath = self.startpath
        command = self.command
#        do_update = self.do_update(updatepath)
#        close_app = self.close_app(startpath)
#        zip_dir = self.zip_dir(copypath,testpath)
#        replace_app = self.replace_app(updatepath,testpath)
#        start_app = self.start_app(startpath,updatepath,command)s
        
        if self.do_update(updatepath):
            if self.close_app(startpath):
                if self.zip_dir(copypath,testpath):
                    if self.replace_app(updatepath,testpath):
                        if self.start_app(startpath,updatepath,command):
                            return 'start'
                        else:
                            return 'nostart'
                    else:
                        return  'noreplace'
                else:
                    return 'nozip'
            else:
                return 'noclose'
        else:
            return 'noupdate'
                    
        
        


    def restart(self):
        updatepath = self.updatepath
        startpath = self.startpath
        command = self.command
        if self.close_app(startpath):
            if self.start_app(startpath,updatepath,command):
                return 'start'
            else:
                return 'nostart'
        else:
            return 'noclose'

    def startalone(self):
        updatepath = self.updatepath
        startpath = self.startpath
        command = self.command
        if self.check_process(startpath):
            return 'isstart'
        elif self.start_app(startpath,updatepath,command):
            return  'start'
        else:
            return 'nostart'

        
        

if __name__ == '__main__':
    #加载sys，编码模式改成gbk识别win中文
#    reload(sys)
#    sys.setdefaultencoding('gbk') 
    updatepath = r"E:\\电子病历接口\\DLLv2\\exe" #svn路径
    testpath = r"C:\Documents and Settings\Administrator\桌面\信息对照\exe" #测试程序路径
    copypath = r"C:\Documents and Settings\Administrator\桌面\信息对照" #备份路径
    #copypath = r"\\192.168.29.15\TEST"
    startpath = r"C:\Documents and Settings\Administrator\桌面\信息对照\exe\EBM_PortTool.exe"
#    print testpath
    user = 'Administrator'
    psd = 'jidezhu911'
#    rule1 = rule(updatepath,testpath,copypath,startpath)
#    rule1.do()
    app = cont_app(updatepath,testpath,copypath,startpath)
    app.do()

