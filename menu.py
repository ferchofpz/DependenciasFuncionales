# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(220, 10, 421, 20))
        self.labelTitle.setObjectName("labelTitle")
        self.buttonOpen = QtWidgets.QPushButton(self.centralwidget)
        self.buttonOpen.setGeometry(QtCore.QRect(410, 70, 75, 23))
        self.buttonOpen.setObjectName("buttonOpen")
        self.comboBoxMain = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxMain.setGeometry(QtCore.QRect(50, 70, 351, 22))
        self.comboBoxMain.setObjectName("comboBoxMain")
        self.comboBoxMain.addItem("")
        self.comboBoxMain.addItem("")
        self.comboBoxMain.addItem("")
        self.comboBoxMain.addItem("")
        self.comboBoxMain.addItem("")
        self.labelMenu = QtWidgets.QLabel(self.centralwidget)
        self.labelMenu.setGeometry(QtCore.QRect(30, 50, 131, 16))
        self.labelMenu.setObjectName("labelMenu")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(10, 120, 831, 431))
        self.mdiArea.setObjectName("mdiArea")
        self.subwindow_one = QtWidgets.QWidget()
        self.subwindow_one.setObjectName("subwindow_one")
        self.labelTittle_one = QtWidgets.QLabel(self.subwindow_one)
        self.labelTittle_one.setGeometry(QtCore.QRect(280, 10, 281, 20))
        self.labelTittle_one.setObjectName("labelTittle_one")
        self.buttonUploadFile_one = QtWidgets.QPushButton(self.subwindow_one)
        self.buttonUploadFile_one.setGeometry(QtCore.QRect(20, 80, 75, 23))
        self.buttonUploadFile_one.setObjectName("buttonUploadFile_one")
        self.labelFile_one = QtWidgets.QLabel(self.subwindow_one)
        self.labelFile_one.setGeometry(QtCore.QRect(100, 80, 331, 16))
        self.labelFile_one.setObjectName("labelFile_one")
        self.buttonClousureCalculate_one = QtWidgets.QPushButton(self.subwindow_one)
        self.buttonClousureCalculate_one.setGeometry(QtCore.QRect(280, 340, 75, 23))
        self.buttonClousureCalculate_one.setObjectName("buttonClousureCalculate_one")
        self.scrollArea = QtWidgets.QScrollArea(self.subwindow_one)
        self.scrollArea.setGeometry(QtCore.QRect(460, 70, 341, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 339, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEditL_one = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEditL_one.setObjectName("plainTextEditL_one")
        self.gridLayout.addWidget(self.plainTextEditL_one, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.labelBelong_one = QtWidgets.QLabel(self.subwindow_one)
        self.labelBelong_one.setGeometry(QtCore.QRect(460, 40, 71, 16))
        self.labelBelong_one.setObjectName("labelBelong_one")
        self.label_11 = QtWidgets.QLabel(self.subwindow_one)
        self.label_11.setGeometry(QtCore.QRect(30, 220, 21, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.subwindow_one)
        self.label_12.setGeometry(QtCore.QRect(30, 150, 21, 16))
        self.label_12.setObjectName("label_12")
        self.labelSubTitle_two_6 = QtWidgets.QLabel(self.subwindow_one)
        self.labelSubTitle_two_6.setGeometry(QtCore.QRect(20, 120, 221, 16))
        self.labelSubTitle_two_6.setObjectName("labelSubTitle_two_6")
        self.viewT1 = QtWidgets.QPlainTextEdit(self.subwindow_one)
        self.viewT1.setGeometry(QtCore.QRect(50, 150, 381, 31))
        self.viewT1.setObjectName("viewT1")
        self.viewL1 = QtWidgets.QPlainTextEdit(self.subwindow_one)
        self.viewL1.setGeometry(QtCore.QRect(50, 220, 381, 91))
        self.viewL1.setObjectName("viewL1")
        self.buttonSave_one = QtWidgets.QPushButton(self.subwindow_one)
        self.buttonSave_one.setGeometry(QtCore.QRect(140, 340, 75, 23))
        self.buttonSave_one.setObjectName("buttonSave_one")
        self.labelTittle_one.raise_()
        self.buttonUploadFile_one.raise_()
        self.labelFile_one.raise_()
        self.buttonClousureCalculate_one.raise_()
        self.scrollArea.raise_()
        self.labelBelong_one.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.labelSubTitle_two_6.raise_()
        self.viewT1.raise_()
        self.viewL1.raise_()
        self.buttonSave_one.raise_()
        self.subwindow_two = QtWidgets.QWidget()
        self.subwindow_two.setObjectName("subwindow_two")
        self.labelTittle_two = QtWidgets.QLabel(self.subwindow_two)
        self.labelTittle_two.setGeometry(QtCore.QRect(270, 10, 301, 20))
        self.labelTittle_two.setObjectName("labelTittle_two")
        self.labelBelong_two = QtWidgets.QLabel(self.subwindow_two)
        self.labelBelong_two.setGeometry(QtCore.QRect(90, 190, 71, 16))
        self.labelBelong_two.setObjectName("labelBelong_two")
        self.lineEditT = QtWidgets.QLineEdit(self.subwindow_two)
        self.lineEditT.setGeometry(QtCore.QRect(70, 70, 631, 20))
        self.lineEditT.setObjectName("lineEditT")
        self.lineEditL = QtWidgets.QLineEdit(self.subwindow_two)
        self.lineEditL.setGeometry(QtCore.QRect(70, 120, 631, 20))
        self.lineEditL.setObjectName("lineEditL")
        self.label_9 = QtWidgets.QLabel(self.subwindow_two)
        self.label_9.setGeometry(QtCore.QRect(50, 70, 21, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.subwindow_two)
        self.label_10.setGeometry(QtCore.QRect(50, 120, 21, 16))
        self.label_10.setObjectName("label_10")
        self.buttonClousureCalculate_two = QtWidgets.QPushButton(self.subwindow_two)
        self.buttonClousureCalculate_two.setGeometry(QtCore.QRect(350, 160, 75, 23))
        self.buttonClousureCalculate_two.setObjectName("buttonClousureCalculate_two")
        self.labelSubTitle_two = QtWidgets.QLabel(self.subwindow_two)
        self.labelSubTitle_two.setGeometry(QtCore.QRect(30, 40, 221, 16))
        self.labelSubTitle_two.setObjectName("labelSubTitle_two")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.subwindow_two)
        self.scrollArea_2.setGeometry(QtCore.QRect(100, 210, 601, 191))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 599, 189))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEditClousure = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEditClousure.setObjectName("plainTextEditClousure")
        self.gridLayout_2.addWidget(self.plainTextEditClousure, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.labelSubTitle_two_2 = QtWidgets.QLabel(self.subwindow_two)
        self.labelSubTitle_two_2.setGeometry(QtCore.QRect(70, 90, 221, 16))
        self.labelSubTitle_two_2.setObjectName("labelSubTitle_two_2")
        self.labelSubTitle_two_3 = QtWidgets.QLabel(self.subwindow_two)
        self.labelSubTitle_two_3.setGeometry(QtCore.QRect(70, 140, 221, 16))
        self.labelSubTitle_two_3.setObjectName("labelSubTitle_two_3")
        self.subwindow_three = QtWidgets.QWidget()
        self.subwindow_three.setObjectName("subwindow_three")
        self.labelTittle_three = QtWidgets.QLabel(self.subwindow_three)
        self.labelTittle_three.setGeometry(QtCore.QRect(320, 10, 191, 20))
        self.labelTittle_three.setObjectName("labelTittle_three")
        self.buttonUploadFile_three = QtWidgets.QPushButton(self.subwindow_three)
        self.buttonUploadFile_three.setGeometry(QtCore.QRect(60, 50, 75, 23))
        self.buttonUploadFile_three.setObjectName("buttonUploadFile_three")
        self.label_6 = QtWidgets.QLabel(self.subwindow_three)
        self.label_6.setGeometry(QtCore.QRect(150, 320, 81, 16))
        self.label_6.setObjectName("label_6")
        self.labelResult = QtWidgets.QLabel(self.subwindow_three)
        self.labelResult.setGeometry(QtCore.QRect(580, 330, 141, 21))
        self.labelResult.setObjectName("labelResult")
        self.label_8 = QtWidgets.QLabel(self.subwindow_three)
        self.label_8.setGeometry(QtCore.QRect(350, 320, 81, 16))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.subwindow_three)
        self.label_7.setGeometry(QtCore.QRect(290, 340, 47, 13))
        self.label_7.setObjectName("label_7")
        self.lineEditDeterminant = QtWidgets.QLineEdit(self.subwindow_three)
        self.lineEditDeterminant.setGeometry(QtCore.QRect(150, 340, 113, 20))
        self.lineEditDeterminant.setObjectName("lineEditDeterminant")
        self.lineEditDetermined = QtWidgets.QLineEdit(self.subwindow_three)
        self.lineEditDetermined.setGeometry(QtCore.QRect(350, 340, 113, 20))
        self.lineEditDetermined.setObjectName("lineEditDetermined")
        self.labelFile_three = QtWidgets.QLabel(self.subwindow_three)
        self.labelFile_three.setGeometry(QtCore.QRect(140, 50, 591, 16))
        self.labelFile_three.setObjectName("labelFile_three")
        self.labelSubTitle_two_7 = QtWidgets.QLabel(self.subwindow_three)
        self.labelSubTitle_two_7.setGeometry(QtCore.QRect(170, 100, 221, 16))
        self.labelSubTitle_two_7.setObjectName("labelSubTitle_two_7")
        self.label_13 = QtWidgets.QLabel(self.subwindow_three)
        self.label_13.setGeometry(QtCore.QRect(180, 130, 21, 16))
        self.label_13.setObjectName("label_13")
        self.buttonSave_three = QtWidgets.QPushButton(self.subwindow_three)
        self.buttonSave_three.setGeometry(QtCore.QRect(600, 130, 75, 23))
        self.buttonSave_three.setObjectName("buttonSave_three")
        self.label_14 = QtWidgets.QLabel(self.subwindow_three)
        self.label_14.setGeometry(QtCore.QRect(180, 200, 21, 16))
        self.label_14.setObjectName("label_14")
        self.viewL3 = QtWidgets.QPlainTextEdit(self.subwindow_three)
        self.viewL3.setGeometry(QtCore.QRect(200, 200, 381, 91))
        self.viewL3.setObjectName("viewL3")
        self.viewT3 = QtWidgets.QPlainTextEdit(self.subwindow_three)
        self.viewT3.setGeometry(QtCore.QRect(200, 130, 381, 31))
        self.viewT3.setObjectName("viewT3")
        self.buttonCalculate_three = QtWidgets.QPushButton(self.subwindow_three)
        self.buttonCalculate_three.setGeometry(QtCore.QRect(600, 200, 75, 23))
        self.buttonCalculate_three.setObjectName("buttonCalculate_three")
        self.subwindow_four = QtWidgets.QWidget()
        self.subwindow_four.setObjectName("subwindow_four")
        self.labelTittle_four = QtWidgets.QLabel(self.subwindow_four)
        self.labelTittle_four.setGeometry(QtCore.QRect(290, 10, 241, 20))
        self.labelTittle_four.setObjectName("labelTittle_four")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.subwindow_four)
        self.scrollArea_3.setGeometry(QtCore.QRect(480, 90, 301, 281))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 299, 279))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.plainTextEditL_four = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.plainTextEditL_four.setObjectName("plainTextEditL_four")
        self.gridLayout_3.addWidget(self.plainTextEditL_four, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.buttonUploadFile_four = QtWidgets.QPushButton(self.subwindow_four)
        self.buttonUploadFile_four.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.buttonUploadFile_four.setObjectName("buttonUploadFile_four")
        self.labelFile_four = QtWidgets.QLabel(self.subwindow_four)
        self.labelFile_four.setGeometry(QtCore.QRect(110, 60, 361, 16))
        self.labelFile_four.setObjectName("labelFile_four")
        self.buttonMinimalCoating_four = QtWidgets.QPushButton(self.subwindow_four)
        self.buttonMinimalCoating_four.setGeometry(QtCore.QRect(280, 340, 75, 23))
        self.buttonMinimalCoating_four.setObjectName("buttonMinimalCoating_four")
        self.labelBelong_one_2 = QtWidgets.QLabel(self.subwindow_four)
        self.labelBelong_one_2.setGeometry(QtCore.QRect(480, 60, 71, 16))
        self.labelBelong_one_2.setObjectName("labelBelong_one_2")
        self.labelSubTitle_two_8 = QtWidgets.QLabel(self.subwindow_four)
        self.labelSubTitle_two_8.setGeometry(QtCore.QRect(30, 120, 221, 16))
        self.labelSubTitle_two_8.setObjectName("labelSubTitle_two_8")
        self.label_15 = QtWidgets.QLabel(self.subwindow_four)
        self.label_15.setGeometry(QtCore.QRect(40, 150, 21, 16))
        self.label_15.setObjectName("label_15")
        self.buttonSave_four = QtWidgets.QPushButton(self.subwindow_four)
        self.buttonSave_four.setGeometry(QtCore.QRect(150, 340, 75, 23))
        self.buttonSave_four.setObjectName("buttonSave_four")
        self.label_16 = QtWidgets.QLabel(self.subwindow_four)
        self.label_16.setGeometry(QtCore.QRect(40, 220, 21, 16))
        self.label_16.setObjectName("label_16")
        self.viewL4 = QtWidgets.QPlainTextEdit(self.subwindow_four)
        self.viewL4.setGeometry(QtCore.QRect(60, 220, 381, 91))
        self.viewL4.setObjectName("viewL4")
        self.viewT4 = QtWidgets.QPlainTextEdit(self.subwindow_four)
        self.viewT4.setGeometry(QtCore.QRect(60, 150, 381, 31))
        self.viewT4.setObjectName("viewT4")
        self.subwindow_five = QtWidgets.QWidget()
        self.subwindow_five.setObjectName("subwindow_five")
        self.buttonCalculateKeys = QtWidgets.QPushButton(self.subwindow_five)
        self.buttonCalculateKeys.setGeometry(QtCore.QRect(280, 340, 75, 23))
        self.buttonCalculateKeys.setObjectName("buttonCalculateKeys")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.subwindow_five)
        self.scrollArea_5.setGeometry(QtCore.QRect(530, 50, 271, 101))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 269, 99))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plainTextEditL_five = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_4)
        self.plainTextEditL_five.setObjectName("plainTextEditL_five")
        self.gridLayout_4.addWidget(self.plainTextEditL_five, 0, 0, 1, 1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_4)
        self.labelBelong_one_3 = QtWidgets.QLabel(self.subwindow_five)
        self.labelBelong_one_3.setGeometry(QtCore.QRect(470, 50, 61, 16))
        self.labelBelong_one_3.setObjectName("labelBelong_one_3")
        self.buttonUploadFile_five = QtWidgets.QPushButton(self.subwindow_five)
        self.buttonUploadFile_five.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.buttonUploadFile_five.setObjectName("buttonUploadFile_five")
        self.labelFile_five = QtWidgets.QLabel(self.subwindow_five)
        self.labelFile_five.setGeometry(QtCore.QRect(120, 60, 341, 16))
        self.labelFile_five.setObjectName("labelFile_five")
        self.labelTittle_five = QtWidgets.QLabel(self.subwindow_five)
        self.labelTittle_five.setGeometry(QtCore.QRect(230, 10, 371, 20))
        self.labelTittle_five.setObjectName("labelTittle_five")
        self.labelBelong_one_4 = QtWidgets.QLabel(self.subwindow_five)
        self.labelBelong_one_4.setGeometry(QtCore.QRect(480, 170, 41, 16))
        self.labelBelong_one_4.setObjectName("labelBelong_one_4")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.subwindow_five)
        self.scrollArea_6.setGeometry(QtCore.QRect(530, 170, 271, 211))
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 269, 209))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.plainTextEditL_keys = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.plainTextEditL_keys.setObjectName("plainTextEditL_keys")
        self.gridLayout_5.addWidget(self.plainTextEditL_keys, 0, 0, 1, 1)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_5)
        self.labelSubTitle_two_9 = QtWidgets.QLabel(self.subwindow_five)
        self.labelSubTitle_two_9.setGeometry(QtCore.QRect(30, 120, 221, 16))
        self.labelSubTitle_two_9.setObjectName("labelSubTitle_two_9")
        self.buttonSave_five = QtWidgets.QPushButton(self.subwindow_five)
        self.buttonSave_five.setGeometry(QtCore.QRect(150, 340, 75, 23))
        self.buttonSave_five.setObjectName("buttonSave_five")
        self.label_17 = QtWidgets.QLabel(self.subwindow_five)
        self.label_17.setGeometry(QtCore.QRect(40, 150, 21, 16))
        self.label_17.setObjectName("label_17")
        self.viewL5 = QtWidgets.QPlainTextEdit(self.subwindow_five)
        self.viewL5.setGeometry(QtCore.QRect(60, 220, 381, 91))
        self.viewL5.setObjectName("viewL5")
        self.viewT5 = QtWidgets.QPlainTextEdit(self.subwindow_five)
        self.viewT5.setGeometry(QtCore.QRect(60, 150, 381, 31))
        self.viewT5.setObjectName("viewT5")
        self.label_18 = QtWidgets.QLabel(self.subwindow_five)
        self.label_18.setGeometry(QtCore.QRect(40, 220, 21, 16))
        self.label_18.setObjectName("label_18")
        self.labelMenu_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelMenu_2.setGeometry(QtCore.QRect(730, 30, 131, 16))
        self.labelMenu_2.setObjectName("labelMenu_2")
        self.labelMenu_3 = QtWidgets.QLabel(self.centralwidget)
        self.labelMenu_3.setGeometry(QtCore.QRect(730, 50, 131, 16))
        self.labelMenu_3.setObjectName("labelMenu_3")
        self.labelMenu_4 = QtWidgets.QLabel(self.centralwidget)
        self.labelMenu_4.setGeometry(QtCore.QRect(730, 70, 131, 16))
        self.labelMenu_4.setObjectName("labelMenu_4")
        self.labelMenu_5 = QtWidgets.QLabel(self.centralwidget)
        self.labelMenu_5.setGeometry(QtCore.QRect(730, 90, 131, 16))
        self.labelMenu_5.setObjectName("labelMenu_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBoxMain.currentIndexChanged['int'].connect(self.lineEditL.clear)
        self.comboBoxMain.currentIndexChanged['int'].connect(self.lineEditT.clear)
        self.comboBoxMain.currentIndexChanged['int'].connect(self.plainTextEditL_one.clear)
        self.comboBoxMain.currentIndexChanged['int'].connect(self.plainTextEditClousure.clear)
        self.comboBoxMain.currentIndexChanged['int'].connect(self.plainTextEditL_four.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">BASES DE DATOS I</span></p></body></html>"))
        self.buttonOpen.setText(_translate("MainWindow", "Abrir"))
        self.comboBoxMain.setItemText(0, _translate("MainWindow", "1. Calcular cierre L+ desde archivo JSON"))
        self.comboBoxMain.setItemText(1, _translate("MainWindow", "2. Calcular cierre L+ desde entrada manual"))
        self.comboBoxMain.setItemText(2, _translate("MainWindow", "3. Indicar si una DF pertenece a L+"))
        self.comboBoxMain.setItemText(3, _translate("MainWindow", "4. Calcular recubrimiento mínimo"))
        self.comboBoxMain.setItemText(4, _translate("MainWindow", "5. Calculo de llaves"))
        self.labelMenu.setText(_translate("MainWindow", "Seleccione una opción"))
        self.subwindow_one.setWindowTitle(_translate("MainWindow", "Cierre de L+"))
        self.labelTittle_one.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">CALCULAR CIERRE DE L+ (ARCHIVO JSON)</span></p></body></html>"))
        self.buttonUploadFile_one.setText(_translate("MainWindow", "Cargar L"))
        self.labelFile_one.setText(_translate("MainWindow", "buscar archivo JSON"))
        self.buttonClousureCalculate_one.setText(_translate("MainWindow", "Calcular"))
        self.labelBelong_one.setText(_translate("MainWindow", "Resultado:"))
        self.label_11.setText(_translate("MainWindow", "L:"))
        self.label_12.setText(_translate("MainWindow", "T:"))
        self.labelSubTitle_two_6.setText(_translate("MainWindow", "Sea el esquema de relacion R(T,L) donde:"))
        self.buttonSave_one.setText(_translate("MainWindow", "Guardar"))
        self.subwindow_two.setWindowTitle(_translate("MainWindow", "CIERRE DE L+ MANUAL"))
        self.labelTittle_two.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">CALCULAR CIERRE DE L+ (ENTRADA MANUAL)</span></p></body></html>"))
        self.labelBelong_two.setText(_translate("MainWindow", "Resultado:"))
        self.label_9.setText(_translate("MainWindow", "T:"))
        self.label_10.setText(_translate("MainWindow", "L:"))
        self.buttonClousureCalculate_two.setText(_translate("MainWindow", "Calcular"))
        self.labelSubTitle_two.setText(_translate("MainWindow", "Sea el esquema de relacion R(T,L) donde:"))
        self.labelSubTitle_two_2.setText(_translate("MainWindow", "A,B,C,D,E,F,G"))
        self.labelSubTitle_two_3.setText(_translate("MainWindow", "A->B,D;C->F;F->A;C,D->A;A,C->E"))
        self.subwindow_three.setWindowTitle(_translate("MainWindow", "DF pertenece a L+"))
        self.labelTittle_three.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">DF PERTENECE AL CIERRE L+</span></p></body></html>"))
        self.buttonUploadFile_three.setText(_translate("MainWindow", "Cargar L"))
        self.label_6.setText(_translate("MainWindow", "IMPLICANTE"))
        self.labelResult.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Resultado</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "IMPLICADO"))
        self.label_7.setText(_translate("MainWindow", "==>"))
        self.labelFile_three.setText(_translate("MainWindow", "Buscar archivo JSON"))
        self.labelSubTitle_two_7.setText(_translate("MainWindow", "Sea el esquema de relacion R(T,L) donde:"))
        self.label_13.setText(_translate("MainWindow", "T:"))
        self.buttonSave_three.setText(_translate("MainWindow", "Guardar"))
        self.label_14.setText(_translate("MainWindow", "L:"))
        self.buttonCalculate_three.setText(_translate("MainWindow", "Calcular"))
        self.subwindow_four.setWindowTitle(_translate("MainWindow", "Recubrimiento mínimo"))
        self.labelTittle_four.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">RECUBRIMIENTO MÍNIMO</span></p></body></html>"))
        self.buttonUploadFile_four.setText(_translate("MainWindow", "Cargar L"))
        self.labelFile_four.setText(_translate("MainWindow", "buscar archivo JSON"))
        self.buttonMinimalCoating_four.setText(_translate("MainWindow", "Calcular"))
        self.labelBelong_one_2.setText(_translate("MainWindow", "Resultado:"))
        self.labelSubTitle_two_8.setText(_translate("MainWindow", "Sea el esquema de relacion R(T,L) donde:"))
        self.label_15.setText(_translate("MainWindow", "T:"))
        self.buttonSave_four.setText(_translate("MainWindow", "Guardar"))
        self.label_16.setText(_translate("MainWindow", "L:"))
        self.subwindow_five.setWindowTitle(_translate("MainWindow", "Subwindow"))
        self.buttonCalculateKeys.setText(_translate("MainWindow", "Calcular"))
        self.labelBelong_one_3.setText(_translate("MainWindow", "Resultado:"))
        self.buttonUploadFile_five.setText(_translate("MainWindow", "Cargar L"))
        self.labelFile_five.setText(_translate("MainWindow", "Buscar archivo JSON"))
        self.labelTittle_five.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">CALCULO DE LLAVES</span></p></body></html>"))
        self.labelBelong_one_4.setText(_translate("MainWindow", "Llaves:"))
        self.labelSubTitle_two_9.setText(_translate("MainWindow", "Sea el esquema de relacion R(T,L) donde:"))
        self.buttonSave_five.setText(_translate("MainWindow", "Guardar"))
        self.label_17.setText(_translate("MainWindow", "T:"))
        self.label_18.setText(_translate("MainWindow", "L:"))
        self.labelMenu_2.setText(_translate("MainWindow", "Oscar Rodriguez"))
        self.labelMenu_3.setText(_translate("MainWindow", "Jose Rojas"))
        self.labelMenu_4.setText(_translate("MainWindow", "Edwin Monroy"))
        self.labelMenu_5.setText(_translate("MainWindow", "Fernando Perez"))

