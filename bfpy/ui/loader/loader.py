# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 388)
        MainWindow.setAutoFillBackground(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("background-color: rgb(63, 63, 63);\n"
                                         "border-color: rgb(217, 217, 217);")
        self.centralWidget.setObjectName("centralWidget")

        self.CanvasPlaceholder = QtWidgets.QWidget(self.centralWidget)
        self.CanvasPlaceholder.setGeometry(QtCore.QRect(10, 30, 301, 301))
        self.CanvasPlaceholder.setStyleSheet("border-color: rgb(190, 190, 190);\n"
                                             "background-color: rgb(99, 99, 99);")
        self.CanvasPlaceholder.setObjectName("CanvasPlaceholder")

        self.chooseButton = QtWidgets.QPushButton(self.centralWidget)
        self.chooseButton.setGeometry(QtCore.QRect(340, 30, 91, 22))
        self.chooseButton.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.chooseButton.setObjectName("chooseButton")

        self.activeFile = QtWidgets.QLabel(self.centralWidget)
        self.activeFile.setGeometry(QtCore.QRect(20, 10, 411, 16))
        self.activeFile.setStyleSheet("color: rgb(217, 217, 217);")
        self.activeFile.setObjectName("activeFile")

        self.roiFrame = QtWidgets.QFrame(self.centralWidget)
        self.roiFrame.setGeometry(QtCore.QRect(320, 60, 131, 141))
        self.roiFrame.setStyleSheet("background-color: rgb(99, 99, 99);\n"
                                    "border-color: rgb(217, 217, 217);")
        self.roiFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.roiFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roiFrame.setLineWidth(1)
        self.roiFrame.setMidLineWidth(1)
        self.roiFrame.setObjectName("roiFrame")

        self.spinBox = QtWidgets.QSpinBox(self.roiFrame)
        self.spinBox.setGeometry(QtCore.QRect(60, 10, 61, 22))
        self.spinBox.setStyleSheet("background-color: rgb(224, 224, 224);")
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.roiFrame)
        self.spinBox_2.setGeometry(QtCore.QRect(60, 40, 61, 22))
        self.spinBox_2.setStyleSheet("background-color: rgb(224, 224, 224);")
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.roiFrame)
        self.spinBox_3.setGeometry(QtCore.QRect(60, 70, 61, 22))
        self.spinBox_3.setStyleSheet("background-color: rgb(224, 224, 224);")
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.roiFrame)
        self.spinBox_4.setGeometry(QtCore.QRect(60, 100, 61, 22))
        self.spinBox_4.setStyleSheet("background-color: rgb(224, 224, 224);")
        self.spinBox_4.setObjectName("spinBox_4")
        self.label = QtWidgets.QLabel(self.roiFrame)
        self.label.setGeometry(QtCore.QRect(10, 13, 47, 21))
        self.label.setStyleSheet("color: rgb(217, 217, 217);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.roiFrame)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 47, 21))
        self.label_2.setStyleSheet("color: rgb(217, 217, 217);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.roiFrame)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 51, 21))
        self.label_3.setStyleSheet("color: rgb(217, 217, 217);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.roiFrame)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 47, 21))
        self.label_4.setStyleSheet("color: rgb(217, 217, 217);")
        self.label_4.setObjectName("label_4")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(380, 220, 62, 22))
        self.doubleSpinBox.setStyleSheet("background-color: rgb(224, 224, 224);")
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(330, 220, 47, 21))
        self.label_5.setStyleSheet("color: rgb(217, 217, 217);")
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(380, 250, 65, 22))
        self.comboBox.setStyleSheet("background-color: rgb(224, 224, 224);")
        self.comboBox.setObjectName("comboBox")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(330, 250, 47, 21))
        self.label_6.setStyleSheet("color: rgb(217, 217, 217);")
        self.label_6.setObjectName("label_6")
        self.loadButton = QtWidgets.QPushButton(self.centralWidget)
        self.loadButton.setGeometry(QtCore.QRect(340, 300, 91, 22))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.loadButton.setFont(font)
        self.loadButton.setStyleSheet("background-color: rgb(247, 186, 0);\n"
                                      "color: rgb(63, 63, 63);\n"
                                      "font: 75 8pt \"MS Shell Dlg 2\";")
        self.loadButton.setObjectName("loadButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 461, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chooseButton.setText(_translate("MainWindow", "Choose File"))
        self.activeFile.setText(_translate("MainWindow", "No file loaded"))
        self.label.setText(_translate("MainWindow", "Center H"))
        self.label_2.setText(_translate("MainWindow", "Center W"))
        self.label_3.setText(_translate("MainWindow", "Sel. H"))
        self.label_4.setText(_translate("MainWindow", "Sel. W"))
        self.label_5.setText(_translate("MainWindow", "NA"))
        self.label_6.setText(_translate("MainWindow", "Pol. Type"))
        self.loadButton.setText(_translate("MainWindow", "Load Data"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    mainwindow = QtWidgets.QMainWindow()
    main = Ui_MainWindow()
    main.setupUi(mainwindow)
    mainwindow.show()

    sys.exit(app.exec_())