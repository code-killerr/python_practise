# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 22:17:55 2018

@author: Administrator
"""

import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import numpy
import pydicom
from matplotlib import pyplot as plt
#from PyQt5.QtCore import QcoreApplication
class Wiget(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
    def UI(self):
        self.textEdit = QTextEdit(self)  
        self.textEdit.setFocus()  
        self.textEdit.setReadOnly(True)
        self.Button()
    def Button(self):
        changeButton = QPushButton("造影")
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(changeButton)
        
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
    def CloseMessage(self,event):#关闭QWidget提示
        imf=QMessageBox.question(self,'警告','您确定要关闭吗?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if imf == QMessageBox.Yes:
            event.accept()
        else: 
            event.ignore()
class ViewSight(QMainWindow):#主窗口组件
    
    def __init__(self):
        super().__init__()
        self.UI()
    
    def UI(self):
        self.textEdit = QTextEdit(self)  
        self.textEdit.setFocus()  
        self.textEdit.setReadOnly(True)
        self.setCentralWidget(self.textEdit)
        
        self.resize(300,300)#设置长宽move设置位置setGeometry复合位置宽高
        self.setWindowTitle('pydicomview')#标题
        self.center()#设置居中方法
        self.Menu()#菜单栏
        self.subwidget = Wiget()#设置内嵌wiget
        self.setCentralWidget(self.subwidget)
        self.show()#窗口展示方法
    
    
    def Menu(self):
        
        openAction = QAction('&打开',self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('打开文件')
        openAction.triggered.connect(self.openFile)
        exitAction = QAction('&关闭', self)  
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('关闭当前程序')
        exitAction.triggered.connect(qApp.quit)
        
        #openAction.triggered.connect()

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&文件')#菜单栏标题
        fileMenu.addAction(openAction)#菜单栏组件
        fileMenu.addAction(exitAction)
        self.statusBar().showMessage('准备就绪')

        #self.toolbar = self.addToolBar('Exit')#横向工具栏
        #self.toolbar.addAction(exitAction)#横向工具栏组件
    
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def openFile(self):  
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))  
  
        fh = ''  
  
        if QFile.exists(filename):  
            fh = QFile(filename)  
  
        if not fh.open(QFile.ReadOnly):  
            QtGui.qApp.quit()  
  
        tmp = ('dcm: %s' % filename)  
        self.setWindowTitle(tmp)
        #data=self.loadFileInformation(filename)
        data = fh.readAll()
        codec = QTextCodec.codecForUtfText(data)
        unistr = codec.toUnicode(data)  
        self.textEdit.setText(unistr)
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
if __name__ == '__main__':
     
     app = QApplication(sys.argv)
     app.aboutToQuit.connect(app.deleteLater)#崩溃问题解决方法
     v=ViewSight()
     sys.exit(app.exec_())