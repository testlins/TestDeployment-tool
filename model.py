#coding=utf-8
import sqlite3
import os
iddb = sqlite3.connect("db/dep.db")
iddb.text_factory = str
cu = iddb.cursor()

class depdb(object):
    """docstring for depdb"""
    def __init__(self):
        super(depdb, self).__init__()
      
        
    def selectid(self,id):
        cu.execute('select * from Project  where id="%s"'%id)
        qs =cu.fetchall()
        print qs
        return qs
    
    #查询列表界面显示信息
    def selectlist(self):
        cu.execute('select Name,updatetime,type,prostatus,updatetype,startapp,mainpro,copynum from Project ')
        qs =cu.fetchall()
        #print qs
        return qs

    #查询更新部署所需参数
    def selectrule(self,Name):
        cu.execute('select updatepath,testpath,copypath,startpath from Project where Name="%s"'%Name)
        #a = 'select updatepath,testpath,copypath,startpath from Project where Name="%s"'%Name
        #print a
        qs =cu.fetchall()
        #print qs
        return qs
        

    def insertdb(self,Project):
        print Project
        
            


        p_insert = 'insert into Project (Id) values (?);'
        #print xxx
        cu.execute(p_insert,Project)
        #xx = cu.execute(p_insert,Project).lastrowid
        iddb.commit()
        #print xx

    def updatedb(self,id,datalist):
        pass


if __name__ == '__main__':
    #Project ={'Id':None,'Name':'x1111x'}
#    Project = [None]
    x=depdb()
    print x.selectrule('信息对照1')
#    x.insertdb(Project)

    