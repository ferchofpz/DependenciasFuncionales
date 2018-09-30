# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 15:18:01 2018

@author: Oscar,Fernando
"""
import sys
from menu import *
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QFileDialog
from PyQt5 import QtCore
from Funciones import selectTypeInput,getInputFromFile,getDeterminants,getAttributes,setOutputToFile,belongsFD,getClosureL,getClosure,calculateMinimalCoating,fCalculateKeys
import itertools
import json

class Main(QMainWindow, Ui_MainWindow):
        
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)    
        
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_one)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_two)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_three)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_four)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_five)

        self.ui.buttonOpen.clicked.connect(self.showComboBox)
        
        self.ui.buttonClousureCalculate_one.clicked.connect(self.calculateClousureL)        
        self.ui.buttonClousureCalculate_two.clicked.connect(self.calculateClousureLManual)
        self.ui.buttonCalculate_three.clicked.connect(self.belongsToClousure)                
        self.ui.buttonMinimalCoating_four.clicked.connect(self.calculateMinimalCoating)
        self.ui.buttonCalculateKeys.clicked.connect(self.calculateKeys)

               
        self.ui.buttonUploadFile_one.clicked.connect(self.openFile1)   
        self.ui.buttonSave_one.clicked.connect(self.saveFile1)   
        
        self.ui.buttonUploadFile_three.clicked.connect(self.openFile3)   
        self.ui.buttonSave_three.clicked.connect(self.saveFile3)   
        
        self.ui.buttonUploadFile_four.clicked.connect(self.openFile4)   
        self.ui.buttonSave_four.clicked.connect(self.saveFile4)   
        
        self.ui.buttonUploadFile_five.clicked.connect(self.openFile5)   
        self.ui.buttonSave_five.clicked.connect(self.saveFile5)   

        self.ui.mdiArea.hide()
        
    def showComboBox(self):
        option = self.ui.comboBoxMain.currentIndex()        
        self.ui.mdiArea.show()

        if option == 0:
            self.closeAllWindows()            
            self.ui.subwindow_one.showMaximized()
        elif option == 1:
            self.closeAllWindows()
            self.ui.subwindow_two.showMaximized()
        elif option == 2:
            self.closeAllWindows()
            self.ui.subwindow_three.showMaximized()
        elif option == 3:
            self.closeAllWindows()
            self.ui.subwindow_four.showMaximized()
        elif option == 4:
            self.closeAllWindows()
            self.ui.subwindow_five.showMaximized()

    def closeAllWindows(self):
        self.ui.labelFile_one.setText("buscar archivo JSON")
        self.ui.labelFile_three.setText("buscar archivo JSON")
        self.ui.subwindow_one.hide()
        self.ui.subwindow_two.hide()
        self.ui.subwindow_three.hide()
        self.ui.subwindow_four.hide()
        self.ui.subwindow_five.hide()
    
    def openFile1(self):        
        fileRoute, _ = QFileDialog.getOpenFileName(self, 'Buscar Archivo', QtCore.QDir.homePath(), "All Files (*.json)")
        if fileRoute:            
            self.ui.labelFile_one.setText(fileRoute)
            jsonInput = getInputFromFile(fileRoute)
            self.ui.viewT1.appendPlainText(';'.join(jsonInput['T']))
            self.ui.viewL1.appendPlainText(';'.join(jsonInput['L']))

    def openFile3(self):        
        fileRoute, _ = QFileDialog.getOpenFileName(self, 'Buscar Archivo', QtCore.QDir.homePath(), "All Files (*.json)")
        if fileRoute:            
            self.ui.labelFile_three.setText(fileRoute)
            jsonInput = getInputFromFile(fileRoute)
            self.ui.viewT3.appendPlainText(';'.join(jsonInput['T']))
            self.ui.viewL3.appendPlainText(';'.join(jsonInput['L']))
            
    def openFile4(self):        
        fileRoute, _ = QFileDialog.getOpenFileName(self, 'Buscar Archivo', QtCore.QDir.homePath(), "All Files (*.json)")
        if fileRoute:            
            self.ui.labelFile_four.setText(fileRoute)
            jsonInput = getInputFromFile(fileRoute)
            self.ui.viewT4.appendPlainText(';'.join(jsonInput['T']))
            self.ui.viewL4.appendPlainText(';'.join(jsonInput['L']))

    def openFile5(self):        
        fileRoute, _ = QFileDialog.getOpenFileName(self, 'Buscar Archivo', QtCore.QDir.homePath(), "All Files (*.json)")
        if fileRoute:            
            self.ui.labelFile_five.setText(fileRoute)
            jsonInput = getInputFromFile(fileRoute)
            self.ui.viewT5.appendPlainText(';'.join(jsonInput['T']))
            self.ui.viewL5.appendPlainText(';'.join(jsonInput['L']))
            
    def saveFile1(self):
        with open(self.ui.labelFile_one.text(), 'w') as file:
            json.dump({
            "T":self.ui.viewT1.toPlainText().split(';'),
            "L":self.ui.viewL1.toPlainText().split(';')
            }, file)
    
    def saveFile3(self):
        with open(self.ui.labelFile_three.text(), 'w') as file:
            json.dump({
            "T":self.ui.viewT3.toPlainText().split(';'),
            "L":self.ui.viewL3.toPlainText().split(';')
            }, file)
    
    def saveFile4(self):
        with open(self.ui.labelFile_four.text(), 'w') as file:
            json.dump({
            "T":self.ui.viewT4.toPlainText().split(';'),
            "L":self.ui.viewL4.toPlainText().split(';')
            }, file)

    def saveFile5(self):
        with open(self.ui.labelFile_five.text(), 'w') as file:
            json.dump({
            "T":self.ui.viewT5.toPlainText().split(';'),
            "L":self.ui.viewL5.toPlainText().split(';')
            }, file)
    
    def calculateClousureL(self):
        jsonInput = getInputFromFile(self.ui.labelFile_one.text())
        self.ui.plainTextEditL_one.clear()
        setOutputToFile('','W')
        
        if jsonInput is not None:
            determinants = getDeterminants(jsonInput['L'])
            attributes = getAttributes(jsonInput)
            result = getClosureL(attributes, determinants)
            strResult = '\n'.join([str(i) for i in result])
            self.ui.plainTextEditL_one.appendPlainText(strResult)
    
    def calculateClousureLManual(self):
        setOutputToFile('','W')
        self.ui.plainTextEditClousure.clear()
        attributes = self.ui.lineEditT.text()
        determinants = self.ui.lineEditL.text() 
        determinants = getDeterminants(determinants.split(';'))
        result = getClosureL(attributes.split(','), determinants)
        strResult = '\n'.join([str(i) for i in result])
        self.ui.plainTextEditClousure.appendPlainText(strResult)     
        
    def belongsToClousure(self):
        #self.openFile()
        setOutputToFile('','W')
        jsonInput = getInputFromFile(self.ui.labelFile_three.text())
        determinant =self.ui.lineEditDeterminant.text()
        determinant = determinant.strip()
        determined = self.ui.lineEditDetermined.text()
        determined = determined.strip() 
        determinants = getDeterminants(jsonInput['L'])       
        closure = getClosure(determinant.split(','), determinants);
        result = belongsFD(determined, closure)
        
        if result:
            self.ui.labelResult.setText("La dependencia pertenece al cierre L+")
        else:
            self.ui.labelResult.setText("La dependencia no pertenece al cierre L+")

    def calculateMinimalCoating(self):
        setOutputToFile('','W')
        jsonInput = getInputFromFile(self.ui.labelFile_four.text())
        self.ui.plainTextEditL_four.clear()
        determinants = getDeterminants(jsonInput['L'])       
        result = calculateMinimalCoating(determinants)
        for df in result:
            self.ui.plainTextEditL_four.appendPlainText(','.join(df['determinant'])+'->'+','.join(df['determinated'])+'\n')     

    def calculateKeys(self):
        setOutputToFile('','W')
        jsonInput = getInputFromFile(self.ui.labelFile_five.text())
        self.ui.plainTextEditL_five.clear()
        self.ui.plainTextEditL_keys.clear()
        
        if jsonInput is not None:
            determinants = getDeterminants(jsonInput['L'])
            attributes = getAttributes(jsonInput)
            result,M2=fCalculateKeys(attributes,determinants)
            self.ui.plainTextEditL_five.appendPlainText(result)
            for m in M2:
                self.ui.plainTextEditL_keys.appendPlainText(','.join(m)+'\n')
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = Main()
    application.show()
    sys.exit(app.exec_())
        