# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 17:51:20 2018

@author: Administrator
"""
import pydicom
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lb1 = QLabel(self)
        #qle = QLineEdit(self)

        #qle.move(60, 100)
        self.lb1.move(60, 40)

        #qle.textChanged[str].connect(self.onChanged)
        self.onChanged()
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('单行文本')        
        self.show()

    def onChanged(self):
        #text=self.loadFileInformation('D:\\python\\tool\\vhm.a.dcm')
        self.lb1.setText(self.loadFileInformation('D:\\python\\tool\\vhm.a.dcm'))
        self.lb1.adjustSize()
    def loadFileInformation(self,filename):
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
    app.aboutToQuit.connect(app.deleteLater)
    ex = Example()
    sys.exit(app.exec_())