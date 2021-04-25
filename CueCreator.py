import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import PyQt5.sip
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QMessageBox, QGridLayout, QLabel, QPushButton, QFrame
from MainUI import Ui_Dialog
from Cue import cueFile


class mainWindow (QtWidgets.QWidget, Ui_Dialog):
    CueDir ='F:\\Music\\Collections\\'
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.btnBrower.clicked.connect(self.BrowseDir)
        self.btnCreate.clicked.connect(self.CreatCue)
        self.btnClear.clicked.connect(self.ClearText)

    def BrowseDir(self):
        self.CueDir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Open Directory',self.CueDir, QtWidgets.QFileDialog.ShowDirsOnly)
        print(self.CueDir)
        self.edtDir.setText(self.CueDir)

    def ClearText(self):
        self.txtCue.setPlainText("")

    def CreatCue(self):
        desDir=self.edtDir.text()
        print(desDir)
        if desDir[len(desDir)-1] != '/':
            desDir += '/'
        print(desDir)

        myCue = cueFile("CD.cue")

        if len(self.edtAlbum.text()) > 0:
            myCue.SetTitle(self.edtAlbum.text())
        if len(self.edtPerformer.text()) >0:
            myCue.SetPerformer(self.edtPerformer.text())

        myCue.CueFromDir(desDir)

        cuetext=""
        for str1 in myCue.GetContent():
            cuetext += (str1 + "\r\n")
        self.txtCue.setPlainText(cuetext)


        QMessageBox.information(self, "信息", "Cue文件生成完毕！！！")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myDialog = mainWindow()
    myDialog.show()
    sys.exit(app.exec_())
