# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 03:25:29 2018

@author: Administrator
"""

import sys  
import os  
from PyQt5.QtCore import *  
from PyQt5.QtWidgets import *  
  
class Notepad(QMainWindow):  
    def __init__(self):  
        super().__init__()  
        self.initUI()  
  
    def initUI(self):  
        openAction = QAction('Open', self)  
        openAction.setShortcut('Ctrl+O')  
        openAction.setStatusTip('Open a file')  
        openAction.triggered.connect(self.openFile)  
  
        closeAction = QAction('Close', self)  
        closeAction.setShortcut('Ctrl+Q')  
        closeAction.setStatusTip('Close Notepad')  
        closeAction.triggered.connect(self.close)  
  
        menubar = self.menuBar()  
        fileMenu = menubar.addMenu('&File')  
        fileMenu.addAction(openAction)  
        fileMenu.addAction(closeAction)  
  
        self.textEdit = QTextEdit(self)  
        self.textEdit.setFocus()  
        self.textEdit.setReadOnly(True)  
  
        self.resize(700, 800)  
        self.setWindowTitle('Notepad')  
        self.setCentralWidget(self.textEdit)  
        self.show()  
  
    def openFile(self):  
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))  
  
        fh = ''  
  
        if QFile.exists(filename):  
            fh = QFile(filename)  
  
        if not fh.open(QFile.ReadOnly):  
            QtGui.qApp.quit()  
  
        data = fh.readAll()
        data=self.loadFileInformation(filename)
        #codec = QTextCodec.codecForUtfText(data)  
        #unistr = codec.toUnicode(data) 
        self.textEdit.setText(data)
        self.textEdit.adjustSize()
  
        tmp = ('Notepad: %s' % filename)  
        self.setWindowTitle(tmp)  
  
        #self.textEdit.setText(unistr)  
    def loadFileInformation(filename):
     information = {}
     ds = pydicom.read_file(filename)
     information['PatientID'] = ds.PatientID
     information['PatientName'] = ds.PatientName
     information['PatientBirthDate'] = ds.PatientBirthDate
     information['PatientSex'] = ds.PatientSex
     information['StudyID'] = ds.StudyID
     information['StudyDate'] = ds.StudyDate
     information['StudyTime'] = ds.StudyTime
     information['InstitutionName'] = ds.InstitutionName
     information['Manufacturer'] = ds.Manufacturer
     return information        
def main():  
    app = QApplication(sys.argv) 
    app.aboutToQuit.connect(app.deleteLater)
    notepad = Notepad()  
    sys.exit(app.exec_())  
  
if __name__ == '__main__':  
    main()  