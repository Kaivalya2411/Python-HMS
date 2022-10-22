# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'covid19.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from bs4 import BeautifulSoup as BS
import requests
import sys
import images.HMS
from About import Ui_AboutWindow


class Ui_CovidWindow(object):
    def openAbout(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def get_cases(self):
        index = self.comboBox.currentIndex()
        country_name = self.country[index]
        # creating url using country name
        url = "https://www.worldometers.info/coronavirus/country/" + country_name + "/"
        # getting the request from url
        data = requests.get(url)
        # converting the text
        soup = BS(data.text, 'html.parser')
        # finding meta info for cases
        cases = soup.find_all("div", class_="maincounter-number")
        # getting total cases number
        total = cases[0].text
        # filtering it
        total = total[1: len(total) - 2]
        # getting recovered cases number
        recovered = cases[2].text
        # filtering it
        recovered = recovered[1: len(recovered) - 1]
        # getting death cases number
        deaths = cases[1].text
        # filtering it
        deaths = deaths[1: len(deaths) - 1]
        # show data through labels
        self.label_total.setText("Total Cases : " + total)
        self.label_reco.setText("Recovered Cases : " + recovered)
        self.label_death.setText("Total Deaths : " + deaths)

    def setupUi(self, CovidWindow):
        CovidWindow.setObjectName("CovidWindow")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix4/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CovidWindow.setWindowIcon(icon)
        CovidWindow.resize(867, 667)
        CovidWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(CovidWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_icon = QtWidgets.QLabel(self.centralwidget)
        self.label_icon.setGeometry(QtCore.QRect(50, 0, 801, 281))
        self.label_icon.setStyleSheet("image: url(:/newPrefix4/COVID-19-ICON.png);")
        self.label_icon.setText("")
        self.label_icon.setObjectName("label_icon")


        self.country = ["india", "us", "spain", "china", "russia","pakistan", "nepal", "italy", "spain", "uk", "brazil"]
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        for i in self.country:
            i = i.upper()
            self.comboBox.addItem(i)

        self.comboBox.activated.connect(self.get_cases)
        self.comboBox.setGeometry(QtCore.QRect(320, 290, 251, 51))
        self.comboBox.setStyleSheet("background-color: rgb(27, 156, 252);\n"
"color: rgb(255, 255, 255);\n"
                                    "border-radius: 10px;")
        self.comboBox.setObjectName("comboBox")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.comboBox.setFont(font)


        self.label_total = QtWidgets.QLabel("Total Cases ",self.centralwidget)
        self.label_total.setGeometry(QtCore.QRect(200, 360, 461, 71))
        self.label_total.setStyleSheet("background-color: rgb(57, 57, 57);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius: 20px;")
        self.label_total.setText("")
        self.label_total.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_total.setFont(font)
        self.label_total.setObjectName("label_total")


        self.label_reco = QtWidgets.QLabel("Recovered Cases ",self.centralwidget)
        self.label_reco.setGeometry(QtCore.QRect(200, 450, 461, 71))
        self.label_reco.setStyleSheet("background-color: rgb(76, 209, 55);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius: 20px;")
        self.label_reco.setText("")
        self.label_reco.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_reco.setFont(font)
        self.label_reco.setObjectName("label_reco")



        self.label_death = QtWidgets.QLabel("Total Deaths ",self.centralwidget)
        self.label_death.setGeometry(QtCore.QRect(200, 540, 461, 71))
        self.label_death.setStyleSheet("background-color: rgb(232, 65, 24);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius: 20px;")
        self.label_death.setText("")
        self.label_death.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_death.setFont(font)
        self.label_death.setObjectName("label_death")

#-------------------------------------------------------------------
        CovidWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CovidWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 21))
        self.menubar.setObjectName("menubar")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        CovidWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CovidWindow)
        self.statusbar.setObjectName("statusbar")
        CovidWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(CovidWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(CovidWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuOption.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(CovidWindow)
        QtCore.QMetaObject.connectSlotsByName(CovidWindow)
        self.actionExit.triggered.connect(CovidWindow.close)
        self.actionAbout.triggered.connect(self.openAbout)

    def retranslateUi(self, CovidWindow):
        _translate = QtCore.QCoreApplication.translate
        CovidWindow.setWindowTitle(_translate("CovidWindow", "HMS - Covid 19"))
        self.menuOption.setTitle(_translate("CovidWindow", "Option"))
        self.menuHelp.setTitle(_translate("CovidWindow", "Help"))
        self.actionExit.setText(_translate("CovidWindow", "Exit"))
        self.actionAbout.setText(_translate("CovidWindow", "About"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CovidWindow = QtWidgets.QMainWindow()
    ui = Ui_CovidWindow()
    ui.setupUi(CovidWindow)
    CovidWindow.show()
    sys.exit(app.exec_())