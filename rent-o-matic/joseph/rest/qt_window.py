# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from joseph.interface.interface import Interface


class Ui_MainWindow(object):

    def __init__(self):
        self.interface = Interface()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 619)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_start = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_start.setGeometry(QtCore.QRect(120, 385, 113, 21))
        self.lineEdit_start.setObjectName("lineEdit_start")
        self.lineEdit_step = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_step.setGeometry(QtCore.QRect(340, 385, 113, 21))
        self.lineEdit_step.setObjectName("lineEdit_step")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 385, 58, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 385, 58, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit_last = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_last.setGeometry(QtCore.QRect(30, 450, 681, 81))
        self.textEdit_last.setObjectName("textEdit_last")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(521, 380, 121, 32))
        self.pushButton_start.setObjectName("pushButton_start")
        # 绑定执行约瑟夫环点击事件
        self.pushButton_start.clicked.connect(self.push_button_start_clicked)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(190, 40, 131, 101))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton_csv = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_csv.setGeometry(QtCore.QRect(20, 40, 100, 20))
        self.radioButton_csv.setObjectName("radioButton_csv")
        self.radioButton_txt = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_txt.setGeometry(QtCore.QRect(20, 10, 100, 20))
        self.radioButton_txt.setObjectName("radioButton_txt")
        self.radioButton_zip = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_zip.setGeometry(QtCore.QRect(20, 70, 100, 20))
        self.radioButton_zip.setObjectName("radioButton_zip")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 60, 71, 41))
        self.label.setObjectName("label")
        self.pushButton_init = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_init.setGeometry(QtCore.QRect(351, 70, 121, 32))
        self.pushButton_init.setObjectName("pushButton_init")
        # 绑定初始化人员点击事件
        self.pushButton_init.clicked.connect(self.push_button_init_clicked)
        self.textEdit_list = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_list.setGeometry(QtCore.QRect(30, 180, 681, 171))
        self.textEdit_list.setObjectName("textEdit_list")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 76, 131, 16))
        self.label_4.setObjectName("label_4")
        self.label_length = QtWidgets.QLabel(self.centralwidget)
        self.label_length.setGeometry(QtCore.QRect(650, 76, 58, 16))
        self.label_length.setObjectName("label_length")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 160, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 430, 101, 16))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "约瑟夫环"))
        self.label_2.setText(_translate("MainWindow", "起点："))
        self.label_3.setText(_translate("MainWindow", "间隔："))
        self.pushButton_start.setText(_translate("MainWindow", "执行约瑟夫环"))
        self.radioButton_csv.setText(_translate("MainWindow", "people.csv"))
        self.radioButton_txt.setText(_translate("MainWindow", "people.txt"))
        self.radioButton_zip.setText(_translate("MainWindow", "people.zip"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">选择文件：</span></p></body></html>"))
        self.pushButton_init.setText(_translate("MainWindow", "生成人员列表"))
        self.label_4.setText(_translate("MainWindow", "生成人员列表长度为："))
        self.label_length.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "当前人员列表："))
        self.label_7.setText(_translate("MainWindow", "最后剩余人员："))

    def push_button_init_clicked(self):
        people_list = []
        if self.radioButton_txt.isChecked():
            people_list = self.interface.get_people_from_file("/Users/huangliang/Documents/python/PythonProject/python_study/rent-o-matic/data/people.txt")
        elif self.radioButton_csv.isChecked():
            people_list = self.interface.get_people_from_file("/Users/huangliang/Documents/python/PythonProject/python_study/rent-o-matic/data/people.csv")
        self.label_length.setText(str(len(people_list)))
        # TODO:将人员列表展示在TEXT框中

    def push_button_start_clicked(self):
        print("pushButton_start_clicked")