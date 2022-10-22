# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DoctorManagement.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
import images.HMS
from About import Ui_AboutWindow
from DoctorManagementDatabase import Ui_DoctorManagementDatabase
from pymongo import MongoClient
from datetime import datetime

class Ui_DoctorManagement(object):
    def openAbout(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openDoctorManagementDatabase(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DoctorManagementDatabase()
        self.ui.setupUi(self.window)
        self.window.show()

    def SubmitDatabase(self):
        client = MongoClient('localhost:27017')
        db = client.HSMD
        col = db.Doctor_DB

        

        DoctorId = self.DM_ID_TEXT.text().upper()
        DoctorName = self.DM_N_TEXT.text().title()
        DoctorSpecialization = self.DM_S_TEXT.text().title()
        DoctorContact = self.DM_C_TEXT.text()
        dt = datetime.now()
        d = dt.strftime("%B %d,%Y  %H:%M:%S")

        col.insert_one(
            {
                "ID": DoctorId,
                "NAME":DoctorName,
                "SPECIALIZATION":DoctorSpecialization,
                "CONTACT":DoctorContact,
                "DATE & TIME": d
                
                })
        print ('\nInserted data successfully\n')
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix4/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Record Inserted Successfully")
        msg.exec();

    def UpdateDatabase(self):
        client = MongoClient('localhost:27017')
        db = client.HSMD
        col = db.Doctor_DB

        DoctorId = self.DM_ID_TEXT.text().upper()
        DoctorName = self.DM_N_TEXT.text().title()
        DoctorSpecialization = self.DM_S_TEXT.text().title()
        DoctorContact = self.DM_C_TEXT.text()
        dt = datetime.now()
        d = dt.strftime("%B %d,%Y  %H:%M:%S")

        col.update_one(
	    {"ID": DoctorId},
	    {"$set": {"NAME":DoctorName,"SPECIALIZATION":DoctorSpecialization,"CONTACT":DoctorContact,"DATE & TIME": d}})
        print ("\nRecords updated successfully\n")
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix4/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Record Updated Successfully")
        msg.exec();

    def DeleteDatabase(self):
        client = MongoClient('localhost:27017')
        db = client.HSMD
        col = db.Doctor_DB

        DoctorId = self.DM_ID_TEXT.text().upper()
        col.delete_many({"ID":DoctorId})
        print ('\nDeletion successful\n')
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix4/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Record Deleted Successfully")
        msg.exec();


        
    def setupUi(self, DoctorManagement):
        DoctorManagement.setObjectName("DoctorManagement")
        DoctorManagement.resize(1600, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix4/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DoctorManagement.setWindowIcon(icon)
        DoctorManagement.setStyleSheet("background-color: rgb(193, 234, 254);")
        self.centralwidget = QtWidgets.QWidget(DoctorManagement)
        self.centralwidget.setObjectName("centralwidget")

        self.DMS_back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.DMS_back_btn.setGeometry(QtCore.QRect(1400, 20, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.DMS_back_btn.setFont(font)
        self.DMS_back_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 255);\n"
"border-radius: 20px;")
        self.DMS_back_btn.clicked.connect(DoctorManagement.close)
        self.DMS_back_btn.setObjectName("DMS_back_btn")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 81, 81))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"image: url(:/newPrefix4/icon.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1601, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(58, 68, 255);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(980, 210, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(980, 300, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(980, 390, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(980, 480, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.DM_ID_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.DM_ID_TEXT.setGeometry(QtCore.QRect(1210, 210, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DM_ID_TEXT.setFont(font)
        self.DM_ID_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DM_ID_TEXT.setObjectName("DM_ID_TEXT")
        self.DM_N_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.DM_N_TEXT.setGeometry(QtCore.QRect(1210, 300, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DM_N_TEXT.setFont(font)
        self.DM_N_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DM_N_TEXT.setObjectName("DM_N_TEXT")
        self.DM_S_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.DM_S_TEXT.setGeometry(QtCore.QRect(1210, 390, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DM_S_TEXT.setFont(font)
        self.DM_S_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DM_S_TEXT.setObjectName("DM_S_TEXT")
        self.DM_C_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.DM_C_TEXT.setGeometry(QtCore.QRect(1210, 480, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DM_C_TEXT.setFont(font)
        self.DM_C_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DM_C_TEXT.setObjectName("DM_C_TEXT")


        self.DMS_update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.DMS_update_btn.setGeometry(QtCore.QRect(1180, 590, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.DMS_update_btn.setFont(font)
        self.DMS_update_btn.setStyleSheet("color: rgb(58, 134, 255);\n"
"background-color: white ;\n"
"border: 2px solid rgb(58, 134, 255);\n"
"border-radius: 20px;")
        self.DMS_update_btn.clicked.connect(self.UpdateDatabase)
        self.DMS_update_btn.setObjectName("DMS_update_btn")


        self.DMS_delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.DMS_delete_btn.setGeometry(QtCore.QRect(1390, 590, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.DMS_delete_btn.setFont(font)
        self.DMS_delete_btn.setStyleSheet("color: rgb(58, 134, 255);\n"
"background-color: white ;\n"
"border: 2px solid rgb(58, 134, 255);\n"
"border-radius: 20px;")
        self.DMS_delete_btn.clicked.connect(self.DeleteDatabase)
        self.DMS_delete_btn.setObjectName("DMS_delete_btn")


        self.DMS_submit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.DMS_submit_btn.setGeometry(QtCore.QRect(970, 590, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.DMS_submit_btn.setFont(font)
        self.DMS_submit_btn.setStyleSheet("color: rgb(58, 134, 255);\n"
"background-color: white ;\n"
"border: 2px solid rgb(58, 134, 255);\n"
"border-radius: 20px;")
        self.DMS_submit_btn.clicked.connect(self.SubmitDatabase)
        self.DMS_submit_btn.setObjectName("DMS_submit_btn")


        self.DMS_view_btn = QtWidgets.QPushButton(self.centralwidget)
        self.DMS_view_btn.setGeometry(QtCore.QRect(1180, 700, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.DMS_view_btn.setFont(font)
        self.DMS_view_btn.setStyleSheet("color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(112, 161, 255,1.0), stop:1 rgba(55, 66, 250,1.0));\n"
"    border-radius: 20px;")
        self.DMS_view_btn.clicked.connect(self.openDoctorManagementDatabase)
        self.DMS_view_btn.setObjectName("DMS_view_btn")


        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 60, 1011, 821))
        self.label_7.setStyleSheet("image: url(:/newPrefix2/doctor.jpg);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.label.raise_()
        self.DMS_back_btn.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.DM_ID_TEXT.raise_()
        self.DM_N_TEXT.raise_()
        self.DM_S_TEXT.raise_()
        self.DM_C_TEXT.raise_()
        self.DMS_update_btn.raise_()
        self.DMS_delete_btn.raise_()
        self.DMS_submit_btn.raise_()
        self.DMS_view_btn.raise_()
        DoctorManagement.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DoctorManagement)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 26))
        self.menubar.setObjectName("menubar")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        DoctorManagement.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(DoctorManagement)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(DoctorManagement)
        self.actionAbout.setObjectName("actionAbout")
        self.menuOption.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(DoctorManagement)
        QtCore.QMetaObject.connectSlotsByName(DoctorManagement)

        self.actionAbout.triggered.connect(self.openAbout)
        self.actionExit.triggered.connect(DoctorManagement.close)

    def retranslateUi(self, DoctorManagement):
        _translate = QtCore.QCoreApplication.translate
        DoctorManagement.setWindowTitle(_translate("DoctorManagement", "HMS - Doctor Management"))
        self.DMS_back_btn.setText(_translate("DoctorManagement", "Back"))
        self.label.setText(_translate("DoctorManagement", "               Doctor Management Section"))
        self.label_2.setText(_translate("DoctorManagement", "ID :"))
        self.label_4.setText(_translate("DoctorManagement", "Name :"))
        self.label_5.setText(_translate("DoctorManagement", "Specialization :"))
        self.label_6.setText(_translate("DoctorManagement", "Contact :"))
        self.DM_ID_TEXT.setToolTip(_translate("DoctorManagement", "<html><head/><body><p>Ex. DK00001</p></body></html>"))
        self.DMS_update_btn.setText(_translate("DoctorManagement", "Update"))
        self.DMS_update_btn.setToolTip(_translate("DoctorManagement", "<html><head/><body><p>Use proper Id for update</p></body></html>"))
        self.DMS_delete_btn.setText(_translate("DoctorManagement", "Delete"))
        self.DMS_submit_btn.setText(_translate("DoctorManagement", "Submit"))
        self.DMS_view_btn.setText(_translate("DoctorManagement", "View"))
        self.menuOption.setTitle(_translate("DoctorManagement", "Option"))
        self.menuHelp.setTitle(_translate("DoctorManagement", "Help"))
        self.actionExit.setText(_translate("DoctorManagement", "Exit"))
        self.actionAbout.setText(_translate("DoctorManagement", "About"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DoctorManagement = QtWidgets.QMainWindow()
    ui = Ui_DoctorManagement()
    ui.setupUi(DoctorManagement)
    DoctorManagement.show()
    sys.exit(app.exec_())
