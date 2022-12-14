# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PatientDataForm.ui'
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
from PatientDatabase import Ui_PatientDatabase
from pymongo import MongoClient


class Ui_PatientDataForm(object):
    def openAbout(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openPatientDatabase(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PatientDatabase()
        self.ui.setupUi(self.window)
        self.window.show()

    def SubmitDatabase(self):
        client = MongoClient('localhost:27017')
        db = client.HSMD
        col = db.Patient_DB

        PatientId = self.PDF_PI_TEXT.text().upper()
        PatientName = self.PDF_PN_TEXT.text().title()
        PatientAge = self.PDF_PA_TEXT.text()
        PatientAddress = self.PDF_A_TEXT.text().title()
        PatientGender = self.PDF_G_TEXT.text().title()
        PatientPhoneno = self.PDF_PNO_TEXT.text()
        PatientDisease = self.PDF_D_TEXT.text().title()
        PatientStatus = self.PDF_ST_TEXT.text().title()
        PaymentId = self.PDF_PYID_TEXT_2.text().upper()

        col.insert_one(
        {
            "PATIENT ID": PatientId,    # patient id
            "PATIENT NAME": PatientName,
            "AGE": PatientAge,
            "ADDRESS": PatientAddress,
            "GENDER": PatientGender,
            "PHONE NO": PatientPhoneno,
            "DISEASE":PatientDisease,
            "HEALTH STATUS": PatientStatus,
            "PAYMENT ID": PaymentId
            
            })
        print ('\nInserted data successfully\n')
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix4/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Record Inserted Successfully")

    def UpdateDatabase(self):
        client = MongoClient('localhost:27017')
        db = client.HSMD
        col = db.Patient_DB

        PatientId = self.PDF_PI_TEXT.text().upper()
        PatientName = self.PDF_PN_TEXT.text().title()
        PatientAge = self.PDF_PA_TEXT.text()
        PatientAddress = self.PDF_A_TEXT.text().title()
        PatientGender = self.PDF_G_TEXT.text().title()
        PatientPhoneno = self.PDF_PNO_TEXT.text()
        PatientDisease = self.PDF_D_TEXT.text().title()
        PatientStatus = self.PDF_ST_TEXT.text().title()
        PaymentId = self.PDF_PYID_TEXT_2.text().upper()

        col.update_one(
	{"PATIENT ID":  PatientId},
	{"$set": {"PATIENT NAME": PatientName,"AGE": PatientAge,"ADDRESS":PatientAddress,"GENDER":PatientGender,"PHONE NO":PatientPhoneno,"DISEASE":PatientDisease,"HEALTH STATUS":PatientStatus,"PAYMENT ID":PaymentId}})
        print ("\nRecords updated successfully\n")
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix4/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Record Updated Successfully")
        

    def DeleteDatabase(self):
        client = MongoClient('localhost:27017')
        db = client.HSMD
        col = db.Patient_DB
          
        PatientId = self.PDF_PI_TEXT.text().upper()
        col.delete_many({"PATIENT ID":PatientId})
        print ('\nDeletion successful\n')
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix4/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Record Deleted Successfully")
        msg.exec();


    def setupUi(self, PatientDataForm):
        PatientDataForm.setObjectName("PatientDataForm")
        PatientDataForm.resize(1600, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix4/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PatientDataForm.setWindowIcon(icon)
        PatientDataForm.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(243, 251, 254);")
        self.centralwidget = QtWidgets.QWidget(PatientDataForm)
        self.centralwidget.setObjectName("centralwidget")


        self.PDF_back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.PDF_back_btn.setGeometry(QtCore.QRect(1420, 20, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PDF_back_btn.setFont(font)
        self.PDF_back_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 68, 255);\n"
"border-radius: 20px;")
        self.PDF_back_btn.clicked.connect(PatientDataForm.close)
        self.PDF_back_btn.setObjectName("PDF_back_btn")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1601, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(58, 68, 255);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 81, 81))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"image: url(:/newPrefix4/icon.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(810, 210, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(810, 290, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(810, 370, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(810, 450, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(810, 530, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(810, 610, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(810, 690, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(810, 130, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.PDF_PN_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.PDF_PN_TEXT.setGeometry(QtCore.QRect(1010, 210, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PDF_PN_TEXT.setFont(font)
        self.PDF_PN_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PDF_PN_TEXT.setObjectName("PDF_PN_TEXT")
        self.PDF_PA_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.PDF_PA_TEXT.setGeometry(QtCore.QRect(1010, 290, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PDF_PA_TEXT.setFont(font)
        self.PDF_PA_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PDF_PA_TEXT.setObjectName("PDF_PA_TEXT")
        self.PDF_A_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.PDF_A_TEXT.setGeometry(QtCore.QRect(1010, 370, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PDF_A_TEXT.setFont(font)
        self.PDF_A_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PDF_A_TEXT.setObjectName("PDF_A_TEXT")
        self.PDF_G_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.PDF_G_TEXT.setGeometry(QtCore.QRect(1010, 450, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PDF_G_TEXT.setFont(font)
        self.PDF_G_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PDF_G_TEXT.setObjectName("PDF_G_TEXT")
        self.PDF_PNO_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.PDF_PNO_TEXT.setGeometry(QtCore.QRect(1010, 530, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PDF_PNO_TEXT.setFont(font)
        self.PDF_PNO_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PDF_PNO_TEXT.setObjectName("PDF_PNO_TEXT")
        self.PDF_D_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.PDF_D_TEXT.setGeometry(QtCore.QRect(1010, 610, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PDF_D_TEXT.setFont(font)
        self.PDF_D_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PDF_D_TEXT.setObjectName("PDF_D_TEXT")
        self.PDF_ST_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.PDF_ST_TEXT.setGeometry(QtCore.QRect(1010, 690, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PDF_ST_TEXT.setFont(font)
        self.PDF_ST_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PDF_ST_TEXT.setObjectName("PDF_ST_TEXT")

        self.PDF_PI_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.PDF_PI_TEXT.setGeometry(QtCore.QRect(1010, 130, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PDF_PI_TEXT.setFont(font)
        self.PDF_PI_TEXT.setInputMask("PI_0000")
        self.PDF_PI_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PDF_PI_TEXT.setObjectName("PDF_PI_TEXT")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(-10, 100, 831, 771))
        self.label_11.setStyleSheet("image: url(:/newPrefix5/Patient3.png);\n"
"background-color: rgb(243, 251, 254);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")


        self.PDF_submit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.PDF_submit_btn.setGeometry(QtCore.QRect(1420, 220, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PDF_submit_btn.setFont(font)
        self.PDF_submit_btn.setStyleSheet("color: rgb(58, 134, 255);\n"
"background-color: white ;\n"
"border: 2px solid rgb(58, 134, 255);\n"
"border-radius: 20px;")
        self.PDF_submit_btn.clicked.connect(self.SubmitDatabase)
        self.PDF_submit_btn.setObjectName("PDF_submit_btn")


        self.PDF_update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.PDF_update_btn.setGeometry(QtCore.QRect(1420, 330, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PDF_update_btn.setFont(font)
        self.PDF_update_btn.setStyleSheet("color: rgb(58, 134, 255);\n"
"background-color: white ;\n"
"border: 2px solid rgb(58, 134, 255);\n"
"border-radius: 20px;")
        self.PDF_update_btn.clicked.connect(self.UpdateDatabase)
        self.PDF_update_btn.setObjectName("PDF_update_btn")


        self.PDF_delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.PDF_delete_btn.setGeometry(QtCore.QRect(1420, 440, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PDF_delete_btn.setFont(font)
        self.PDF_delete_btn.setStyleSheet("color: rgb(58, 134, 255);\n"
"background-color: white ;\n"
"border: 2px solid rgb(58, 134, 255);\n"
"border-radius: 20px;")
        self.PDF_delete_btn.clicked.connect(self.DeleteDatabase)
        self.PDF_delete_btn.setObjectName("PDF_delete_btn")


        self.PDF_view_btn = QtWidgets.QPushButton(self.centralwidget)
        self.PDF_view_btn.setGeometry(QtCore.QRect(1420, 550, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PDF_view_btn.setFont(font)
        self.PDF_view_btn.setStyleSheet("color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(112, 161, 255,1.0), stop:1 rgba(55, 66, 250,1.0));\n"
"    border-radius: 20px;")
        self.PDF_view_btn.clicked.connect(self.openPatientDatabase)
        self.PDF_view_btn.setObjectName("PDF_view_btn")


        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(810, 770, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.PDF_PYID_TEXT_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.PDF_PYID_TEXT_2.setGeometry(QtCore.QRect(1010, 770, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PDF_PYID_TEXT_2.setFont(font)
        self.PDF_PYID_TEXT_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PDF_PYID_TEXT_2.setObjectName("PDF_PYID_TEXT_2")
        self.label_11.raise_()
        self.label.raise_()
        self.PDF_back_btn.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.PDF_PN_TEXT.raise_()
        self.PDF_PA_TEXT.raise_()
        self.PDF_A_TEXT.raise_()
        self.PDF_G_TEXT.raise_()
        self.PDF_PNO_TEXT.raise_()
        self.PDF_D_TEXT.raise_()
        self.PDF_ST_TEXT.raise_()
        self.PDF_PI_TEXT.raise_()
        self.PDF_submit_btn.raise_()
        self.PDF_update_btn.raise_()
        self.PDF_delete_btn.raise_()
        self.PDF_view_btn.raise_()
        self.label_12.raise_()
        self.PDF_PYID_TEXT_2.raise_()
        PatientDataForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PatientDataForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 26))
        self.menubar.setObjectName("menubar")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        PatientDataForm.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(PatientDataForm)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(PatientDataForm)
        self.actionAbout.setObjectName("actionAbout")
        self.menuOption.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(PatientDataForm)
        QtCore.QMetaObject.connectSlotsByName(PatientDataForm)

        self.actionAbout.triggered.connect(self.openAbout)
        self.actionExit.triggered.connect(PatientDataForm.close)

    def retranslateUi(self, PatientDataForm):
        _translate = QtCore.QCoreApplication.translate
        PatientDataForm.setWindowTitle(_translate("PatientDataForm", "HMS - Patient Data Form"))
        self.PDF_back_btn.setText(_translate("PatientDataForm", "Back"))
        self.label.setText(_translate("PatientDataForm", "                       Patient Data From"))
        self.label_3.setText(_translate("PatientDataForm", "Patient Name :"))
        self.label_4.setText(_translate("PatientDataForm", "Age :"))
        self.label_5.setText(_translate("PatientDataForm", "Address :"))
        self.label_6.setText(_translate("PatientDataForm", "Gender :"))
        self.label_7.setText(_translate("PatientDataForm", "Phone No :"))
        self.label_8.setText(_translate("PatientDataForm", "Disease :"))
        self.label_9.setText(_translate("PatientDataForm", "Status :"))
        self.label_10.setText(_translate("PatientDataForm", "Patient Id :"))
        self.PDF_submit_btn.setText(_translate("PatientDataForm", "Submit"))
        self.PDF_update_btn.setText(_translate("PatientDataForm", "Update"))
        self.PDF_delete_btn.setText(_translate("PatientDataForm", "Delete"))
        self.PDF_view_btn.setText(_translate("PatientDataForm", "View"))
        self.label_12.setText(_translate("PatientDataForm", "Payment Id :"))
        self.menuOption.setTitle(_translate("PatientDataForm", "Option"))
        self.menuHelp.setTitle(_translate("PatientDataForm", "Help"))
        self.actionExit.setText(_translate("PatientDataForm", "Exit"))
        self.actionAbout.setText(_translate("PatientDataForm", "About"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PatientDataForm = QtWidgets.QMainWindow()
    ui = Ui_PatientDataForm()
    ui.setupUi(PatientDataForm)
    PatientDataForm.show()
    sys.exit(app.exec_())
