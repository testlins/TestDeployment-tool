#coding=utf-8

import shutil
import os
import time
import zipfile
import mylog
import subprocess


import sys 
#f = open('rule.py','r',encoding='gbk') 
#reload(sys)
#sys.setdefaultencoding('gbk') 

class cont_app(object):
    """升级、备份、替换测试程序"""
    def __init__(self,updatepath,testpath,copypath,appname):
#        reload(sys)
#        sys.setdefaultencoding('gbk')

#        a = "E:\\电子病历接口\\exe"
#        print u'%s'%a

        super(cont_app, self).__init__()
        self.updatepath = os.path.normpath(updatepath.decode('utf-8').encode('gbk'))
#        print self.updatepath
        self.testpath = os.path.normpath(testpath.decode('utf-8').encode('gbk'))
#        print self.testpath
        self.copypath = os.path.normpath(copypath.decode('utf-8').encode('gbk'))
#        print self.copypath
        self.appname = appname.decode('utf-8').encode('gbk')

    def do_update(self):
        """从svn更新最新程序(不管有没更新都会进行后续操作，需优化)"""
        updatepath = self.updatepath
        #检查路径是否为目录
        if os.path.isdir(updatepath):
            try:
                updateshell = 'TortoiseProc.exe /command:update /path:"%s" /closeonend:1'%updatepath
                os.system(updateshell)
            except Exception,msg:
                print msg
                return False
        else:
            print 'nn'
            return False


    
    def start_app(self):
        '''起程序'''
        appname = self.appname
        testpath = self.testpath
        apppath = os.path.normpath(os.path.join(testpath,appname))
#        print apppath
#        print apppath
        if os.path.isfile(apppath):
            try:
                os.chdir(testpath)#如果启动程序不在第一层目录下？ 需优化
                #os.system(appname)#启动程序后应该退出脚本，现没有退出 一直占用资源 需优化【用start app或 execl解决】
                os.system('start %s' %appname) 
                #由于os.chdir会占用目录导致第二次调用删除不了目录 现在先这样规避
                os.chdir('D:\\')
#                os.execl(appname,'i') #直接退出进程
            except Exception,msg:
                print msg
                return False
        else:
            print 'apppath is error'
            return False

        #sys.exit()


    def close_app(self):
        '''关闭程序进程'''
        appname = self.appname
        try:
            closeshell = 'taskkill /f /im %s'%appname
            os.system(closeshell)
        except Exception,msg:
            print msg
            return False


 
    def zip_dir(self):
        '''打包备份'''
        copypath = self.copypath
        testpath = self.testpath
        nowtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
        if os.path.isdir(copypath):
            zipFile1 = zipfile.ZipFile(os.path.join(copypath,os.path.basename(testpath)+nowtime+'.zip'),'w') 
        else:
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
            return False
        #用os.walk搜索全路径下文件,还不能做到压缩目录不带全路径
        """for dirpath, dirnames, filenames in os.walk(testpath):
            
            for filename in filenames:   
            #print filename
                zipFile1.write(os.path.join(dirpath,filename))"""        
        zipFile1.close() 
        return True 
       
    def replace_app(self):
        ''' 更新程序'''
        updatepath  = self.updatepath
        testpath = self.testpath
        try:
            shutil.rmtree(testpath)
        except  Exception,msg:
            print 'rmtree error is %s'%msg
            return False  

        try:
            shutil.copytree(updatepath,testpath)
        except  Exception,msg:
            print msg
            return False        

    def conn_pc(self,path=None,user=None,psd=None):
        shell = r'NET USE "%s" "%s" /user:"%s"'%(path,psd,user)
        #print shell
        try:
            os.popen(shell)
        except Exception,msg:
            print msg
            return False  





    def do(self):
        

        #self.do_update()
        #self.close_app()
        #self.zip_dir()

        self.replace_app()
        time.sleep(3)
        self.start_app()


def do():
    app = cont_app(updatepath,testpath,copypath,appname)

    app.do_update()
    print '1'
    app.close_app()
    print '2'
    app.zip_dir()
    print '3'
    app.replace_app()
    print '4'
    app.start_app()
    print '5'



        




        

if __name__ == '__main__':
    #加载sys，编码模式改成gbk识别win中文
#    reload(sys)
#    sys.setdefaultencoding('gbk') 
    updatepath = "E:\\电子病历接口\\DLLv2\\exe" #svn路径
    testpath = "C:\Documents and Settings\Administrator\桌面\信息对照\exe" #测试程序路径
    copypath = "C:\Documents and Settings\Administrator\桌面\信息对照" #备份路径
    #copypath = r"\\192.168.29.15\TEST"
    appname = "EBM_PortTool.exe"
#    print testpath
    user = 'Administrator'
    psd = 'jidezhu911'
    #do()
    app = cont_app(updatepath,testpath,copypath,appname)
    app.do()































