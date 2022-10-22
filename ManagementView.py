# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManagementView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import images.HMS
from About import Ui_AboutWindow
from covid19 import Ui_CovidWindow
from DoctorManagement import Ui_DoctorManagement
from AppointmentManagement import Ui_AppointmentManagement
from PatientDatabase import Ui_PatientDatabase
from PharmacistManagement import Ui_PharmacistManagement
from AdminDatabase import Ui_AdminDatabase


class Ui_ManagementView(object):
    def openAbout(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openDoctorManagement(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DoctorManagement()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAppointmentManagement(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AppointmentManagement()
        self.ui.setupUi(self.window)
        self.window.show()

    def openPatientDatabase(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PatientDatabase()
        self.ui.setupUi(self.window)
        self.window.show()

    def openPharmacistManagement(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PharmacistManagement()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAdminDatabase(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AdminDatabase()
        self.ui.setupUi(self.window)
        self.window.show()

    def openCovid(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CovidWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def logout(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix4/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setIcon(QMessageBox.Information)
        font = QtGui.QFont()
        font.setPointSize(10)
        msg.setFont(font)
        msg.setText("Management Admin Successfully Loged Out")
        msg.exec();
        
        
    def setupUi(self, ManagementView):
        ManagementView.setObjectName("ManagementView")
        ManagementView.resize(1600, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix4/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ManagementView.setWindowIcon(icon)
        ManagementView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(ManagementView)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1601, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(58, 68, 255);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")


        self.MVS_logout_btn = QtWidgets.QPushButton(self.centralwidget)
        self.MVS_logout_btn.setGeometry(QtCore.QRect(1430, 20, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.MVS_logout_btn.setFont(font)
        self.MVS_logout_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 68, 255);\n"
"border-radius: 20px;")
        self.MVS_logout_btn.clicked.connect(ManagementView.close)
        self.MVS_logout_btn.clicked.connect(self.logout)
        self.MVS_logout_btn.setObjectName("MVS_logout_btn")

        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 81, 81))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"image: url(:/newPrefix4/icon.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 80, 911, 801))
        self.label_3.setStyleSheet("\n"
"image: url(:/newPrefix5/Management.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")


        self.MVS_covid_btn = QtWidgets.QPushButton(self.centralwidget)
        self.MVS_covid_btn.setGeometry(QtCore.QRect(1510, 800, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MVS_covid_btn.setFont(font)
        self.MVS_covid_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        self.MVS_covid_btn.clicked.connect(self.openCovid)
        self.MVS_covid_btn.setObjectName("MVS_covid_btn")


        self.MVS_doctor_btn = QtWidgets.QPushButton(self.centralwidget)
        self.MVS_doctor_btn.setGeometry(QtCore.QRect(900, 140, 271, 241))
        self.MVS_doctor_btn.setStyleSheet("image: url(:/newPrefix3/mvdbtn.PNG);\n"
"border-radius: 20px;")
        self.MVS_doctor_btn.setText("")
        self.MVS_doctor_btn.clicked.connect(self.openDoctorManagement)
        self.MVS_doctor_btn.setObjectName("MVS_doctor_btn")


        self.MVS_patient_btn = QtWidgets.QPushButton(self.centralwidget)
        self.MVS_patient_btn.setGeometry(QtCore.QRect(1200, 120, 311, 301))
        self.MVS_patient_btn.setStyleSheet("image: url(:/newPrefix3/mvpbtn.PNG);\n"
"border-radius: 20px;")
        self.MVS_patient_btn.setText("")
        self.MVS_patient_btn.clicked.connect(self.openPatientDatabase)
        self.MVS_patient_btn.setObjectName("MVS_patient_btn")


        self.MVS_appointment_btn = QtWidgets.QPushButton(self.centralwidget)
        self.MVS_appointment_btn.setGeometry(QtCore.QRect(890, 420, 301, 291))
        self.MVS_appointment_btn.setStyleSheet("image: url(:/newPrefix3/mvabtn.PNG);\n"
"border-radius: 20px;")
        self.MVS_appointment_btn.setText("")
        self.MVS_appointment_btn.clicked.connect(self.openAppointmentManagement)
        self.MVS_appointment_btn.setObjectName("MVS_appointment_btn")


        self.MVS_pharmacy_btn = QtWidgets.QPushButton(self.centralwidget)
        self.MVS_pharmacy_btn.setGeometry(QtCore.QRect(1220, 430, 291, 261))
        self.MVS_pharmacy_btn.setStyleSheet("image: url(:/newPrefix3/mvprbtn.PNG);\n"
"border-radius: 20px;")
        self.MVS_pharmacy_btn.setText("")
        self.MVS_pharmacy_btn.clicked.connect(self.openPharmacistManagement)
        self.MVS_pharmacy_btn.setObjectName("MVS_pharmacy_btn")


        self.MVS_AD_btn = QtWidgets.QPushButton(self.centralwidget)
        self.MVS_AD_btn.setGeometry(QtCore.QRect(1050, 730, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MVS_AD_btn.setFont(font)
        self.MVS_AD_btn.setStyleSheet("color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(112, 161, 255,1.0), stop:1 rgba(55, 66, 250,1.0));\n"
"    border-radius: 20px;\n"
"border-radius: 20px;")
        self.MVS_AD_btn.clicked.connect(self.openAdminDatabase)
        self.MVS_AD_btn.setObjectName("MVS_AD_btn")


        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.MVS_logout_btn.raise_()
        self.MVS_covid_btn.raise_()
        self.MVS_doctor_btn.raise_()
        self.MVS_patient_btn.raise_()
        self.MVS_appointment_btn.raise_()
        self.MVS_pharmacy_btn.raise_()
        self.MVS_AD_btn.raise_()
        ManagementView.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(ManagementView)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1600, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuOption = QtWidgets.QMenu(self.menuBar)
        self.menuOption.setObjectName("menuOption")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        ManagementView.setMenuBar(self.menuBar)
        self.actionExit = QtWidgets.QAction(ManagementView)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(ManagementView)
        self.actionAbout.setObjectName("actionAbout")
        self.menuOption.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuOption.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(ManagementView)
        QtCore.QMetaObject.connectSlotsByName(ManagementView)

        self.actionAbout.triggered.connect(self.openAbout)
        self.actionExit.triggered.connect(ManagementView.close)

    def retranslateUi(self, ManagementView):
        _translate = QtCore.QCoreApplication.translate
        ManagementView.setWindowTitle(_translate("ManagementView", "HMS-ManagementView"))
        self.label.setText(_translate("ManagementView", "                Management View Section"))
        self.MVS_logout_btn.setText(_translate("ManagementView", "Logout"))
        self.MVS_covid_btn.setToolTip(_translate("ManagementView", "<html><head/><body><p><span style=\" font-weight:400;\">Check The Status of Covid-19</span></p></body></html>"))
        self.MVS_covid_btn.setText(_translate("ManagementView", "!"))
        self.MVS_AD_btn.setText(_translate("ManagementView", "Admin Database"))
        self.menuOption.setTitle(_translate("ManagementView", "Option"))
        self.menuHelp.setTitle(_translate("ManagementView", "Help"))
        self.actionExit.setText(_translate("ManagementView", "Exit"))
        self.actionAbout.setText(_translate("ManagementView", "About"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManagementView = QtWidgets.QMainWindow()
    ui = Ui_ManagementView()
    ui.setupUi(ManagementView)
    ManagementView.show()
    sys.exit(app.exec_())