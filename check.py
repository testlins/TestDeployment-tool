# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check.ui'
#
# Created: Tue Dec 10 16:06:10 2013
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

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(861, 730)
        self.buttonBox = QtGui.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(410, 600, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayoutWidget = QtGui.QWidget(dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 781, 551))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 15, 0, 1, 1)
        self.updateuser = QtGui.QLineEdit(self.gridLayoutWidget)
        self.updateuser.setMaximumSize(QtCore.QSize(50, 16777215))
        self.updateuser.setText(_fromUtf8(""))
        self.updateuser.setMaxLength(30)
        self.updateuser.setReadOnly(True)
        self.updateuser.setObjectName(_fromUtf8("updateuser"))
        self.gridLayout.addWidget(self.updateuser, 2, 5, 1, 1)
        self.label_13 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 2, 4, 1, 1)
        self.label_10 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 14, 0, 1, 1)
        self.startpush = QtGui.QPushButton(self.gridLayoutWidget)
        self.startpush.setMaximumSize(QtCore.QSize(60, 16777215))
        self.startpush.setObjectName(_fromUtf8("startpush"))
        self.gridLayout.addWidget(self.startpush, 10, 3, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 13, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.nameEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.nameEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.nameEdit.setAutoFillBackground(False)
        self.nameEdit.setMaxLength(30)
        self.nameEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameEdit.setReadOnly(True)
        self.nameEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.gridLayout.addWidget(self.nameEdit, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.copypathEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.copypathEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.copypathEdit.setAutoFillBackground(False)
        self.copypathEdit.setMaxLength(200)
        self.copypathEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.copypathEdit.setReadOnly(True)
        self.copypathEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.copypathEdit.setObjectName(_fromUtf8("copypathEdit"))
        self.gridLayout.addWidget(self.copypathEdit, 7, 2, 1, 1)
        self.startapp = QtGui.QComboBox(self.gridLayoutWidget)
        self.startapp.setEnabled(False)
        self.startapp.setMaximumSize(QtCore.QSize(40, 16777215))
        self.startapp.setObjectName(_fromUtf8("startapp"))
        self.startapp.addItem(_fromUtf8(""))
        self.startapp.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.startapp, 14, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 12, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.updatepush = QtGui.QPushButton(self.gridLayoutWidget)
        self.updatepush.setMaximumSize(QtCore.QSize(60, 16777215))
        self.updatepush.setObjectName(_fromUtf8("updatepush"))
        self.gridLayout.addWidget(self.updatepush, 2, 3, 1, 1)
        self.mainpro = QtGui.QComboBox(self.gridLayoutWidget)
        self.mainpro.setEnabled(False)
        self.mainpro.setMaximumSize(QtCore.QSize(40, 16777215))
        self.mainpro.setObjectName(_fromUtf8("mainpro"))
        self.mainpro.addItem(_fromUtf8(""))
        self.mainpro.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.mainpro, 13, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 11, 0, 1, 1)
        self.startappEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.startappEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.startappEdit.setAutoFillBackground(False)
        self.startappEdit.setMaxLength(200)
        self.startappEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.startappEdit.setReadOnly(True)
        self.startappEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.startappEdit.setObjectName(_fromUtf8("startappEdit"))
        self.gridLayout.addWidget(self.startappEdit, 10, 2, 1, 1)
        self.type = QtGui.QComboBox(self.gridLayoutWidget)
        self.type.setEnabled(False)
        self.type.setMaximumSize(QtCore.QSize(40, 16777215))
        self.type.setEditable(True)
        self.type.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.type.setFrame(True)
        self.type.setObjectName(_fromUtf8("type"))
        self.type.addItem(_fromUtf8(""))
        self.type.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.type, 1, 2, 1, 1)
        self.updatepathEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.updatepathEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.updatepathEdit.setAutoFillBackground(False)
        self.updatepathEdit.setMaxLength(200)
        self.updatepathEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.updatepathEdit.setReadOnly(True)
        self.updatepathEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.updatepathEdit.setObjectName(_fromUtf8("updatepathEdit"))
        self.gridLayout.addWidget(self.updatepathEdit, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)
        self.stopappEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.stopappEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.stopappEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.stopappEdit.setAutoFillBackground(False)
        self.stopappEdit.setText(_fromUtf8(""))
        self.stopappEdit.setMaxLength(200)
        self.stopappEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.stopappEdit.setReadOnly(True)
        self.stopappEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.stopappEdit.setObjectName(_fromUtf8("stopappEdit"))
        self.gridLayout.addWidget(self.stopappEdit, 11, 2, 1, 1)
        self.stoppush = QtGui.QPushButton(self.gridLayoutWidget)
        self.stoppush.setMaximumSize(QtCore.QSize(60, 16777215))
        self.stoppush.setObjectName(_fromUtf8("stoppush"))
        self.gridLayout.addWidget(self.stoppush, 11, 3, 1, 1)
        self.testpush = QtGui.QPushButton(self.gridLayoutWidget)
        self.testpush.setMaximumSize(QtCore.QSize(60, 16777215))
        self.testpush.setObjectName(_fromUtf8("testpush"))
        self.gridLayout.addWidget(self.testpush, 6, 3, 1, 1)
        self.copypush = QtGui.QPushButton(self.gridLayoutWidget)
        self.copypush.setMaximumSize(QtCore.QSize(60, 16777215))
        self.copypush.setObjectName(_fromUtf8("copypush"))
        self.gridLayout.addWidget(self.copypush, 7, 3, 1, 1)
        self.updatetype = QtGui.QComboBox(self.gridLayoutWidget)
        self.updatetype.setEnabled(False)
        self.updatetype.setMaximumSize(QtCore.QSize(80, 16777215))
        self.updatetype.setObjectName(_fromUtf8("updatetype"))
        self.updatetype.addItem(_fromUtf8(""))
        self.updatetype.addItem(_fromUtf8(""))
        self.updatetype.addItem(_fromUtf8(""))
        self.updatetype.setItemText(2, _fromUtf8(""))
        self.gridLayout.addWidget(self.updatetype, 3, 2, 1, 1)
        self.copyuser = QtGui.QLineEdit(self.gridLayoutWidget)
        self.copyuser.setMaximumSize(QtCore.QSize(50, 16777215))
        self.copyuser.setText(_fromUtf8(""))
        self.copyuser.setMaxLength(30)
        self.copyuser.setReadOnly(True)
        self.copyuser.setObjectName(_fromUtf8("copyuser"))
        self.gridLayout.addWidget(self.copyuser, 7, 5, 1, 1)
        self.label_15 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 7, 4, 1, 1)
        self.copypsd = QtGui.QLineEdit(self.gridLayoutWidget)
        self.copypsd.setMaximumSize(QtCore.QSize(70, 16777215))
        self.copypsd.setText(_fromUtf8(""))
        self.copypsd.setMaxLength(30)
        self.copypsd.setEchoMode(QtGui.QLineEdit.Password)
        self.copypsd.setReadOnly(True)
        self.copypsd.setObjectName(_fromUtf8("copypsd"))
        self.gridLayout.addWidget(self.copypsd, 7, 6, 1, 1)
        self.label_14 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 6, 4, 1, 1)
        self.testuser = QtGui.QLineEdit(self.gridLayoutWidget)
        self.testuser.setMaximumSize(QtCore.QSize(50, 16777215))
        self.testuser.setText(_fromUtf8(""))
        self.testuser.setMaxLength(30)
        self.testuser.setReadOnly(True)
        self.testuser.setObjectName(_fromUtf8("testuser"))
        self.gridLayout.addWidget(self.testuser, 6, 5, 1, 1)
        self.updatepsd = QtGui.QLineEdit(self.gridLayoutWidget)
        self.updatepsd.setMaximumSize(QtCore.QSize(70, 16777215))
        self.updatepsd.setMaxLength(30)
        self.updatepsd.setEchoMode(QtGui.QLineEdit.Password)
        self.updatepsd.setReadOnly(True)
        self.updatepsd.setObjectName(_fromUtf8("updatepsd"))
        self.gridLayout.addWidget(self.updatepsd, 2, 6, 1, 1)
        self.copynum = QtGui.QSpinBox(self.gridLayoutWidget)
        self.copynum.setEnabled(False)
        self.copynum.setMaximumSize(QtCore.QSize(40, 16777215))
        self.copynum.setProperty("value", 20)
        self.copynum.setObjectName(_fromUtf8("copynum"))
        self.gridLayout.addWidget(self.copynum, 15, 2, 1, 1)
        self.testpsd = QtGui.QLineEdit(self.gridLayoutWidget)
        self.testpsd.setMaximumSize(QtCore.QSize(70, 16777215))
        self.testpsd.setText(_fromUtf8(""))
        self.testpsd.setMaxLength(30)
        self.testpsd.setEchoMode(QtGui.QLineEdit.Password)
        self.testpsd.setReadOnly(True)
        self.testpsd.setObjectName(_fromUtf8("testpsd"))
        self.gridLayout.addWidget(self.testpsd, 6, 6, 1, 1)
        self.prostatus = QtGui.QComboBox(self.gridLayoutWidget)
        self.prostatus.setEnabled(False)
        self.prostatus.setMaximumSize(QtCore.QSize(50, 16777215))
        self.prostatus.setObjectName(_fromUtf8("prostatus"))
        self.prostatus.addItem(_fromUtf8(""))
        self.prostatus.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.prostatus, 12, 2, 1, 1)
        self.copypathEdit_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.copypathEdit_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.copypathEdit_2.setAutoFillBackground(False)
        self.copypathEdit_2.setMaxLength(200)
        self.copypathEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.copypathEdit_2.setReadOnly(True)
        self.copypathEdit_2.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.copypathEdit_2.setObjectName(_fromUtf8("copypathEdit_2"))
        self.gridLayout.addWidget(self.copypathEdit_2, 6, 2, 1, 1)
        self.label_2.setBuddy(self.updatetype)
        self.label_11.setBuddy(self.copynum)
        self.label_13.setBuddy(self.updateuser)
        self.label_10.setBuddy(self.startapp)
        self.label.setBuddy(self.nameEdit)
        self.label_8.setBuddy(self.mainpro)
        self.label_7.setBuddy(self.copypathEdit)
        self.label_5.setBuddy(self.type)
        self.label_12.setBuddy(self.prostatus)
        self.label_6.setBuddy(self.updatepathEdit)
        self.label_9.setBuddy(self.stopappEdit)
        self.label_4.setBuddy(self.startappEdit)
        self.label_15.setBuddy(self.copyuser)
        self.label_14.setBuddy(self.testuser)

        self.retranslateUi(dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)
        dialog.setTabOrder(self.nameEdit, self.type)
        dialog.setTabOrder(self.type, self.updatepathEdit)
        dialog.setTabOrder(self.updatepathEdit, self.updatepush)
        dialog.setTabOrder(self.updatepush, self.updateuser)
        dialog.setTabOrder(self.updateuser, self.updatepsd)
        dialog.setTabOrder(self.updatepsd, self.updatetype)
        dialog.setTabOrder(self.updatetype, self.testpush)
        dialog.setTabOrder(self.testpush, self.testuser)
        dialog.setTabOrder(self.testuser, self.testpsd)
        dialog.setTabOrder(self.testpsd, self.copypathEdit)
        dialog.setTabOrder(self.copypathEdit, self.copypush)
        dialog.setTabOrder(self.copypush, self.copyuser)
        dialog.setTabOrder(self.copyuser, self.copypsd)
        dialog.setTabOrder(self.copypsd, self.startappEdit)
        dialog.setTabOrder(self.startappEdit, self.startpush)
        dialog.setTabOrder(self.startpush, self.stopappEdit)
        dialog.setTabOrder(self.stopappEdit, self.stoppush)
        dialog.setTabOrder(self.stoppush, self.prostatus)
        dialog.setTabOrder(self.prostatus, self.mainpro)
        dialog.setTabOrder(self.mainpro, self.startapp)
        dialog.setTabOrder(self.startapp, self.copynum)
        dialog.setTabOrder(self.copynum, self.buttonBox)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "查看项目", None))
        self.label_2.setText(_translate("dialog", "项目更新方式", None))
        self.label_11.setText(_translate("dialog", "最大备份数", None))
        self.label_13.setToolTip(_translate("dialog", "<html><head/><body><p>远程路径 需要输入对应账号密码 获取路径权限</p></body></html>", None))
        self.label_13.setText(_translate("dialog", "账号/密码", None))
        self.label_10.setText(_translate("dialog", "更新后启动程序", None))
        self.startpush.setText(_translate("dialog", "选择路径", None))
        self.label.setToolTip(_translate("dialog", "<html><head/><body><p><br/></p></body></html>", None))
        self.label.setText(_translate("dialog", "项目名称", None))
        self.label_8.setText(_translate("dialog", "主项目", None))
        self.label_7.setText(_translate("dialog", "项目备份路径", None))
        self.label_3.setText(_translate("dialog", "项目测试路径", None))
        self.startapp.setItemText(0, _translate("dialog", "否", None))
        self.startapp.setItemText(1, _translate("dialog", "是", None))
        self.label_5.setText(_translate("dialog", "项目类型", None))
        self.label_12.setText(_translate("dialog", "项目状态", None))
        self.label_6.setText(_translate("dialog", "项目更新路径", None))
        self.updatepush.setText(_translate("dialog", "选择路径", None))
        self.mainpro.setItemText(0, _translate("dialog", "否", None))
        self.mainpro.setItemText(1, _translate("dialog", "是", None))
        self.label_9.setText(_translate("dialog", "项目停止路径", None))
        self.type.setItemText(0, _translate("dialog", "C/S", None))
        self.type.setItemText(1, _translate("dialog", "B/S", None))
        self.label_4.setText(_translate("dialog", "项目启动路径", None))
        self.stoppush.setText(_translate("dialog", "选择路径", None))
        self.testpush.setText(_translate("dialog", "选择路径", None))
        self.copypush.setText(_translate("dialog", "选择路径", None))
        self.updatetype.setItemText(0, _translate("dialog", "需SVN更新", None))
        self.updatetype.setItemText(1, _translate("dialog", "不需SVN更新", None))
        self.label_15.setToolTip(_translate("dialog", "<html><head/><body><p>远程路径 需要输入对应账号密码 获取路径权限</p></body></html>", None))
        self.label_15.setText(_translate("dialog", "账号/密码", None))
        self.label_14.setToolTip(_translate("dialog", "<html><head/><body><p>远程路径 需要输入对应账号密码 获取路径权限</p></body></html>", None))
        self.label_14.setText(_translate("dialog", "账号/密码", None))
        self.prostatus.setItemText(0, _translate("dialog", "正常", None))
        self.prostatus.setItemText(1, _translate("dialog", "停用", None))

