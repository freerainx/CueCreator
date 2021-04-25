# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(639, 652)
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(20, 25, 46, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.btnBrower = QtWidgets.QPushButton(Dialog)
        self.btnBrower.setGeometry(QtCore.QRect(550, 18, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.btnBrower.setFont(font)
        self.btnBrower.setObjectName("btnBrower")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 55, 46, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 85, 46, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.edtDir = QtWidgets.QLineEdit(Dialog)
        self.edtDir.setGeometry(QtCore.QRect(70, 20, 461, 20))
        self.edtDir.setObjectName("edtDir")
        self.edtAlbum = QtWidgets.QLineEdit(Dialog)
        self.edtAlbum.setGeometry(QtCore.QRect(70, 50, 461, 20))
        self.edtAlbum.setObjectName("edtAlbum")
        self.edtPerformer = QtWidgets.QLineEdit(Dialog)
        self.edtPerformer.setGeometry(QtCore.QRect(70, 80, 461, 20))
        self.edtPerformer.setObjectName("edtPerformer")
        self.btnCreate = QtWidgets.QPushButton(Dialog)
        self.btnCreate.setGeometry(QtCore.QRect(550, 50, 75, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.btnCreate.setFont(font)
        self.btnCreate.setObjectName("btnCreate")
        self.txtCue = QtWidgets.QPlainTextEdit(Dialog)
        self.txtCue.setGeometry(QtCore.QRect(10, 110, 621, 501))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.txtCue.setFont(font)
        self.txtCue.setReadOnly(True)
        self.txtCue.setObjectName("txtCue")
        self.btnClear = QtWidgets.QPushButton(Dialog)
        self.btnClear.setGeometry(QtCore.QRect(550, 620, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cue生成器"))
        self.label_1.setText(_translate("Dialog", "文件夹"))
        self.btnBrower.setText(_translate("Dialog", "浏览"))
        self.label_2.setText(_translate("Dialog", "专辑名"))
        self.label_3.setText(_translate("Dialog", "演唱者"))
        self.btnCreate.setText(_translate("Dialog", "生成"))
        self.btnClear.setText(_translate("Dialog", "清空"))

