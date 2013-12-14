# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Dec 12 14:50:43 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 601, 521))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection) 
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True) 
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.update = QtGui.QPushButton(self.centralwidget)
        self.update.setGeometry(QtCore.QRect(630, 70, 75, 23))
        self.update.setObjectName(_fromUtf8("update"))
        self.add = QtGui.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(720, 130, 75, 23))
        self.add.setObjectName(_fromUtf8("add"))
        self.modify = QtGui.QPushButton(self.centralwidget)
        self.modify.setGeometry(QtCore.QRect(630, 130, 75, 23))
        self.modify.setObjectName(_fromUtf8("modify"))
        self.startapp = QtGui.QPushButton(self.centralwidget)
        self.startapp.setGeometry(QtCore.QRect(720, 70, 75, 23))
        self.startapp.setObjectName(_fromUtf8("startapp"))
        self.restartapp = QtGui.QPushButton(self.centralwidget)
        self.restartapp.setGeometry(QtCore.QRect(630, 190, 75, 23))
        self.restartapp.setObjectName(_fromUtf8("restartapp"))
        self.opentestpath = QtGui.QPushButton(self.centralwidget)
        self.opentestpath.setGeometry(QtCore.QRect(720, 190, 75, 23))
        self.opentestpath.setObjectName(_fromUtf8("opentestpath"))
        self.opencopypath = QtGui.QPushButton(self.centralwidget)
        self.opencopypath.setGeometry(QtCore.QRect(630, 250, 71, 23))
        self.opencopypath.setObjectName(_fromUtf8("opencopypath"))
        self.openupdatepath = QtGui.QPushButton(self.centralwidget)
        self.openupdatepath.setGeometry(QtCore.QRect(720, 250, 75, 23))
        self.openupdatepath.setObjectName(_fromUtf8("openupdatepath"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "部署助手v0.1", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "项目名称", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "更新时间", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "项目类型", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "项目状态", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "更新方式", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "更新后启动", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "是否主项目", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "最大备份数", None))
        self.update.setText(_translate("MainWindow", "更新", None))
        self.add.setText(_translate("MainWindow", "新增", None))
        self.modify.setText(_translate("MainWindow", "编辑", None))
        self.startapp.setToolTip(_translate("MainWindow", "<html><head/><body><p>单独启动选中项目，不做更新</p></body></html>", None))
        self.startapp.setText(_translate("MainWindow", "启动项目", None))
        self.restartapp.setText(_translate("MainWindow", "重启", None))
        self.opentestpath.setText(_translate("MainWindow", "测试路径", None))
        self.opencopypath.setText(_translate("MainWindow", "备份路径", None))
        self.openupdatepath.setText(_translate("MainWindow", "更新路径", None))

