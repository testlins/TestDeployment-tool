#coding=utf-8
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
#import ui_10_1,ui_10_2,ui_10_3  
import main,check,modify,add
import sys  
import model 
import rule
import subprocess

  
class TestDialog(QMainWindow,QDialog):  
    def __init__(self,parent=None):  
        super(TestDialog,self).__init__(parent) 
        reload(sys)
        sys.setdefaultencoding('utf-8')
 
#        self.textlist = []
        self.mainUi=main.Ui_MainWindow()
        self.mainUi.setupUi(self) 
        self.db = model.depdb()
        self.loadtable() 
        
#        self.db = model.depdb()
#        self.rule = rule.cont_app()
        self.addUi=add.Ui_dialog()  
        self.modifyUi=modify.Ui_dialog()  
#self.connect(self.MyTable, SIGNAL("itemClicked (QTableWidgetItem*)"), self.outSelect)
        #因为用itemClicked只能在有值时调用，改用clicked没有查到相关资料
        #self.mainUi.tableWidget.clicked.connect(self.outSelect)
#行表头
#        self.mainUi.tableWidget.verticalHeader().sectionClicked.connect(self.VerSectionClicked)
        #列表头
#        self.mainUi.tableWidget.horizontalHeader().sectionClicked.connect(self.HorSectionClicked)
       #new style       
        self.mainUi.add.clicked.connect(self.addChild)
        self.mainUi.update.clicked.connect(self.updateapp)
#       old style
#        self.connect(mainUi.add,SIGNAL("clicked()"),self.addChild)  
    
    def addChild(self):
        dlg=QDialog()  
        self.addUi.setupUi(dlg)  
        dlg.exec_()  

    def loadtable(self):
        #加载编码设置 没搞懂为什么首行设置的utf-8不行？？
#        reload(sys)
#        sys.setdefaultencoding('utf-8')

        db = self.db
        self.alldata =  db.selectlist()
        for i in xrange(len(self.alldata)):

            for x in xrange(len(self.alldata[i])):
                        
                #解决中文乱码问题，待学习具体原因
                item = u'%s'%self.alldata[i][x]
#                item1 = str(self.alldata[i][x])#.decode('utf-8').encode('gbk')
#                print item1
#                item = item1.decode('gbk').encode('utf-8')

#                print item
                newItem = QTableWidgetItem(item) 
                self.mainUi.tableWidget.setItem(i, x, newItem)  

#    def outSelect(self,Item=None):
##        print Item
#
##        print len(self.textlist)
#        if len(self.textlist)>0:
#            self.textlist = []
##        else:
####            print self.mainUi.tableWidget.item(Item.row(),0).text()
##            print self.textlist
#        try:
#            self.textlist.append(self.mainUi.tableWidget.item(Item.row(),0).text())
#        except Exception,msg:
##            print 'error is:%s'%msg
#            print 'no data'
#
#
#
#
#    
#    def VerSectionClicked(self,index):
#        print self.mainUi.tableWidget.item(index,0).text()
#        
#        self.textlist.append(self.mainUi.tableWidget.item(index,0).text())

    def updateapp(self):
#        reload(sys)
#        sys.setdefaultencoding('gbk')
#
#        print self.mainUi.tableWidget.currentItem().row()#不选中返回值为0
#        currentrow = self.mainUi.tableWidget.currentRow()#不选中返回值为0
        currentrow = self.mainUi.tableWidget.selectedItems()

        if currentrow==[]:
            print 'no data'
        else:
#            print currentrow[0].text()
            db = self.db
            selectrule =  db.selectrule(currentrow[0].text())
#            print selectrule[0][0].decode('gbk').encode('utf-8')

            dorule = rule.cont_app(selectrule[0][0],selectrule[0][1],selectrule[0][2],selectrule[0][3])
#            handle=subprocess.Popen(dorule.do(), shell=True,  stdout=subprocess.PIPE)
#            handle.terminate()
            dorule.do()
        
        
        
        

if __name__ == "__main__":          
    app=QApplication(sys.argv)  
    myapp=TestDialog()  
    myapp.show()  
    sys.exit(app.exec_())  


#class MyForm(QtGui.QMainWindow):
#    def __init__(self, parent=None):
#        QtGui.QWidget.__init__(self, parent)
#        self.ui = Ui_MainWindow()
#        self.ui.setupUi(self)
#
#if __name__ == "__main__":
#    app = QtGui.QApplication(sys.argv)
#    myapp = MyForm()
#    myapp.show()
#    sys.exit(app.exec_())




