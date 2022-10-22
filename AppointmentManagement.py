
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from About import Ui_AboutWindow
from AppointmentManagementDatabase import Ui_AppointmentManagementDatabase
import images.HMS
from PyQt5.QtWidgets import QMessageBox
from pymongo import MongoClient


class Ui_AppointmentManagement(object):
    def openAbout(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAppointmentManagementDatabase(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AppointmentManagementDatabase()
        self.ui.setupUi(self.window)
        self.window.show()


    def SubmitDatabase(self):
        client = MongoClient('localhost:27017')
        db = client.HSMD
        col = db.Appointment_DB

        DoctorID = self.AM_DI_TEXT.text().upper()
        DoctorName = self.AM_DN_TEXT.text().title()
        DcotorSpecial = self.AM_S_TEXT.text().title()
        WorkingDays = self.AM_WD_TEXT.text().title()
        WorkingHours = self.AM_WH_TEXT.text().title()
        FPatient = self.AM_FP_TEXT.text().title()
        SPatient = self.AM_SP_TEXT.text().title()
        TPatient = self.AM_TP_TEXT.text().title()

        col.insert_one(
        {
            "DOCTOR ID": DoctorID,
            "DOCTOR NAME": DoctorName,
            "SPECIALIZATION": DcotorSpecial,
            "WORKING DAYS": WorkingDays,
            "WORKING HOURS": WorkingHours,
            "1ST PATIENT NAME": FPatient,
            "2ND PATIENT NAME": SPatient,
            "3RD PATIENT NAME": TPatient
            })
        print ('\nData Inserted Successfully\n')
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix4/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setIcon(QMessageBox.Information)
        font = QtGui.QFont()
        font.setPointSize(10)
        msg.setFont(font)
        msg.setText("Data Inserted Successfully")
        msg.exec();

    def UpdateDatabase(self):
        client = MongoClient('localhost:27017')
        db = client.HSMD
        col = db.Appointment_DB

        DoctorID = self.AM_DI_TEXT.text().upper()
        DoctorName = self.AM_DN_TEXT.text().title()
        DcotorSpecial = self.AM_S_TEXT.text().title()
        WorkingDays = self.AM_WD_TEXT.text().title()
        WorkingHours = self.AM_WH_TEXT.text().title()
        FPatient = self.AM_FP_TEXT.text().title()
        SPatient = self.AM_SP_TEXT.text().title()
        TPatient = self.AM_TP_TEXT.text().title()

        col.update_one(
            {"DOCTOR ID": DoctorID},
            {"$set": {"DOCTOR NAME":DoctorName,"SPECIALIZATION":DcotorSpecial,"WORKING DAYS":WorkingDays,"WORKING HOURS":WorkingHours,"1ST PATIENT NAME":FPatient,"2ND PATIENT NAME":SPatient,"3RD PATIENT NAME":TPatient}})
        print ("\nRecord Updated Successfully\n")
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix4/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setIcon(QMessageBox.Information)
        font = QtGui.QFont()
        font.setPointSize(10)
        msg.setFont(font)
        msg.setText("Record Updated Successfully")
        msg.exec();

    def DeleteDatabase(self):
          client = MongoClient('localhost:27017')
          db = client.HSMD
          col = db.Appointment_DB
          
          DoctorID = self.AM_DI_TEXT.text().upper()
          col.delete_many({"DOCTOR ID": DoctorID})
          print ('\nRecord Deleted Successful\n')
          msg = QMessageBox()
          msg.setWindowTitle("Message")
          icon = QtGui.QIcon()
          icon.addPixmap(QtGui.QPixmap(":/newPrefix4/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
          msg.setWindowIcon(icon)
          msg.setIcon(QMessageBox.Information)
          font = QtGui.QFont()
          font.setPointSize(10)
          msg.setFont(font)
          msg.setText("Record Deleted Successfully")
          msg.exec();


    def setupUi(self, AppointmentManagement):
        AppointmentManagement.setObjectName("AppointmentManagement")
        AppointmentManagement.resize(1600, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix4/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AppointmentManagement.setWindowIcon(icon)
        AppointmentManagement.setStyleSheet("background-color: rgb(239, 243, 255);")
        self.centralwidget = QtWidgets.QWidget(AppointmentManagement)
        self.centralwidget.setObjectName("centralwidget")


        self.AM_back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.AM_back_btn.setGeometry(QtCore.QRect(1420, 30, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AM_back_btn.setFont(font)
        self.AM_back_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 68, 255);\n"
"border-radius: 20px;")
        self.AM_back_btn.clicked.connect(AppointmentManagement.close)
        self.AM_back_btn.setObjectName("AM_back_btn")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 81, 81))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"image: url(:/newPrefix4/icon.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(810, 170, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(810, 250, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(810, 330, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(810, 410, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(810, 570, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(810, 490, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(810, 650, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(810, 730, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("")
        self.label_10.setObjectName("label_10")
        self.AM_DI_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.AM_DI_TEXT.setGeometry(QtCore.QRect(1060, 170, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AM_DI_TEXT.setInputMask("IP")
        self.AM_DI_TEXT.setFont(font)
        self.AM_DI_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(0, 0, 255);\n"
"")
        self.AM_DI_TEXT.setObjectName("AM_DI_TEXT")
        self.AM_DN_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.AM_DN_TEXT.setGeometry(QtCore.QRect(1060, 250, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AM_DN_TEXT.setFont(font)
        self.AM_DN_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AM_DN_TEXT.setObjectName("AM_DN_TEXT")
        self.AM_S_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.AM_S_TEXT.setGeometry(QtCore.QRect(1060, 330, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AM_S_TEXT.setFont(font)
        self.AM_S_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AM_S_TEXT.setObjectName("AM_S_TEXT")
        self.AM_WD_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.AM_WD_TEXT.setGeometry(QtCore.QRect(1060, 410, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AM_WD_TEXT.setFont(font)
        self.AM_WD_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AM_WD_TEXT.setObjectName("AM_WD_TEXT")
        self.AM_WH_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.AM_WH_TEXT.setGeometry(QtCore.QRect(1060, 490, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AM_WH_TEXT.setFont(font)
        self.AM_WH_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AM_WH_TEXT.setObjectName("AM_WH_TEXT")
        self.AM_FP_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.AM_FP_TEXT.setGeometry(QtCore.QRect(1060, 570, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AM_FP_TEXT.setFont(font)
        self.AM_FP_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AM_FP_TEXT.setObjectName("AM_FP_TEXT")
        self.AM_SP_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.AM_SP_TEXT.setGeometry(QtCore.QRect(1060, 650, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AM_SP_TEXT.setFont(font)
        self.AM_SP_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AM_SP_TEXT.setObjectName("AM_SP_TEXT")
        self.AM_TP_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.AM_TP_TEXT.setGeometry(QtCore.QRect(1060, 730, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AM_TP_TEXT.setFont(font)
        self.AM_TP_TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AM_TP_TEXT.setObjectName("AM_TP_TEXT")

        self.AM_delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.AM_delete_btn.setGeometry(QtCore.QRect(1420, 440, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AM_delete_btn.setFont(font)
        self.AM_delete_btn.setStyleSheet("color: rgb(58, 134, 255);\n"
"background-color: white ;\n"
"border: 2px solid rgb(58, 134, 255);\n"
"border-radius: 20px;")
        self.AM_delete_btn.clicked.connect(self.DeleteDatabase)
        self.AM_delete_btn.setObjectName("AM_delete_btn")

        self.AM_update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.AM_update_btn.setGeometry(QtCore.QRect(1420, 330, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AM_update_btn.setFont(font)
        self.AM_update_btn.setStyleSheet("color: rgb(58, 134, 255);\n"
"background-color: white ;\n"
"border: 2px solid rgb(58, 134, 255);\n"
"border-radius: 20px;")
        self.AM_update_btn.clicked.connect(self.UpdateDatabase)
        self.AM_update_btn.setObjectName("AM_update_btn")

        self.AM_submit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.AM_submit_btn.setGeometry(QtCore.QRect(1420, 220, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AM_submit_btn.setFont(font)
        self.AM_submit_btn.setStyleSheet("color: rgb(58, 134, 255);\n"
"background-color: white ;\n"
"border: 2px solid rgb(58, 134, 255);\n"
"border-radius: 20px;")
        self.AM_submit_btn.clicked.connect(self.SubmitDatabase)
        self.AM_submit_btn.setObjectName("AM_submit_btn")

        self.AM_view_btn = QtWidgets.QPushButton(self.centralwidget)
        self.AM_view_btn.setGeometry(QtCore.QRect(1420, 550, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AM_view_btn.setFont(font)
        self.AM_view_btn.setStyleSheet("color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(112, 161, 255,1.0), stop:1 rgba(55, 66, 250,1.0));\n"
"    border-radius: 20px;")
        self.AM_view_btn.clicked.connect(self.openAppointmentManagementDatabase)
        self.AM_view_btn.setObjectName("AM_view_btn")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 50, 841, 831))
        self.label_11.setStyleSheet("image: url(:/newPrefix5/Appointment2.jpg);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_11.raise_()
        self.label.raise_()
        self.AM_back_btn.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.AM_DI_TEXT.raise_()
        self.AM_DN_TEXT.raise_()
        self.AM_S_TEXT.raise_()
        self.AM_WD_TEXT.raise_()
        self.AM_WH_TEXT.raise_()
        self.AM_FP_TEXT.raise_()
        self.AM_SP_TEXT.raise_()
        self.AM_TP_TEXT.raise_()
        self.AM_delete_btn.raise_()
        self.AM_update_btn.raise_()
        self.AM_submit_btn.raise_()
        self.AM_view_btn.raise_()
        AppointmentManagement.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AppointmentManagement)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 26))
        self.menubar.setObjectName("menubar")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        AppointmentManagement.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(AppointmentManagement)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(AppointmentManagement)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_2 = QtWidgets.QAction(AppointmentManagement)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.menuOption.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout_2)
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(AppointmentManagement)
        QtCore.QMetaObject.connectSlotsByName(AppointmentManagement)
        
        self.actionExit.triggered.connect(AppointmentManagement.close)
        self.actionAbout_2.triggered.connect(self.openAbout)

    def retranslateUi(self, AppointmentManagement):
        _translate = QtCore.QCoreApplication.translate
        AppointmentManagement.setWindowTitle(_translate("AppointmentManagement", "HMS - Appointment Management"))
        self.AM_back_btn.setText(_translate("AppointmentManagement", "Back"))
        self.label.setText(_translate("AppointmentManagement", "                    Appointment Management"))
        self.label_3.setText(_translate("AppointmentManagement", "Docter ID :"))
        self.label_4.setText(_translate("AppointmentManagement", "Docter Name :"))
        self.label_5.setText(_translate("AppointmentManagement", "Specialization :"))
        self.label_6.setText(_translate("AppointmentManagement", "Working Days :"))
        self.label_7.setText(_translate("AppointmentManagement", "1st Patient Name :"))
        self.label_8.setText(_translate("AppointmentManagement", "Working Hours :"))
        self.label_9.setText(_translate("AppointmentManagement", "2nd Patient Name :"))
        self.label_10.setText(_translate("AppointmentManagement", "3rd Patient Name :"))
        self.AM_DI_TEXT.setToolTip(_translate("AppointmentManagement", "<html><head/><body><p><span style=\" font-weight:600;\">Ex.DA00001</span></p></body></html>"))
        self.AM_DN_TEXT.setToolTip(_translate("AppointmentManagement", "<html><head/><body><p>Dr. ________ _________</p></body></html>"))
        self.AM_WD_TEXT.setToolTip(_translate("AppointmentManagement", "<html><head/><body><p>Ex. Wed - Fri , </p><p>Mon , Wed , Fri</p></body></html>"))
        self.AM_WH_TEXT.setToolTip(_translate("AppointmentManagement", "<html><head/><body><p>Ex. 11:00 AM to 6:00 PM</p></body></html>"))
        self.AM_delete_btn.setText(_translate("AppointmentManagement", "Delete"))
        self.AM_update_btn.setText(_translate("AppointmentManagement", "Update"))
        self.AM_submit_btn.setText(_translate("AppointmentManagement", "Submit"))
        self.AM_view_btn.setText(_translate("AppointmentManagement", "View"))
        self.menuOption.setTitle(_translate("AppointmentManagement", "Option"))
        self.menuHelp.setTitle(_translate("AppointmentManagement", "Help"))
        self.actionExit.setText(_translate("AppointmentManagement", "Exit"))
        self.actionAbout.setText(_translate("AppointmentManagement", "About"))
        self.actionAbout_2.setText(_translate("AppointmentManagement", "About"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AppointmentManagement = QtWidgets.QMainWindow()
    ui = Ui_AppointmentManagement()
    ui.setupUi(AppointmentManagement)
    AppointmentManagement.show()
    sys.exit(app.exec_())
