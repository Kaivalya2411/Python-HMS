# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import images.HMS


class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("AboutWindow")
        AboutWindow.resize(1600, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix4/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutWindow.setWindowIcon(icon)
        AboutWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(AboutWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 90, 1601, 791))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(870, 90, 721, 571))
        self.textBrowser.setObjectName("textBrowser")

        self.A_exit_btn = QtWidgets.QPushButton(self.groupBox)
        self.A_exit_btn.setGeometry(QtCore.QRect(740, 680, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.A_exit_btn.setFont(font)
        self.A_exit_btn.setStyleSheet("background-color: rgb(58, 68, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius : 20px")
        self.A_exit_btn.clicked.connect(AboutWindow.close)
        self.A_exit_btn.setObjectName("A_exit_btn")

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 851, 651))
        self.label_3.setStyleSheet("image: url(:/newPrefix4/ThankYou.png);\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.textBrowser.raise_()
        self.A_exit_btn.raise_()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1601, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 68, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 0, 91, 91))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"image: url(:/newPrefix4/icon.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        AboutWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(AboutWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1600, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuOption = QtWidgets.QMenu(self.menuBar)
        self.menuOption.setObjectName("menuOption")
        AboutWindow.setMenuBar(self.menuBar)
        self.actionExit = QtWidgets.QAction(AboutWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit_2 = QtWidgets.QAction(AboutWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionExit_3 = QtWidgets.QAction(AboutWindow)
        self.actionExit_3.setObjectName("actionExit_3")
        self.actionExit_3.triggered.connect(AboutWindow.close)
        self.menuOption.addAction(self.actionExit_3)
        self.menuBar.addAction(self.menuOption.menuAction())

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "HMS - About Window"))
        self.groupBox.setTitle(_translate("AboutWindow", "About"))
        self.textBrowser.setHtml(_translate("AboutWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:36px; font-size:8.25pt; background-color:#f8f9fa;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:36px; background-color:#f8f9fa;\"><a name=\"tw-target-text\"></a><span style=\" font-family:\'inherit\'; font-size:20pt; font-weight:600; color:#ff0000;\">T</span><span style=\" font-family:\'inherit\'; font-size:20pt; font-weight:600; color:#ff0000;\">his Software is Created For             Purpose of Mini-Project for College In Department of Computer Engineering By Students</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:36px; font-family:\'inherit\'; font-size:20pt; font-weight:600; color:#202124; background-color:#f8f9fa;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:36px; background-color:#f8f9fa;\"><a name=\"tw-target-text\"></a><span style=\" font-family:\'inherit\'; font-size:20pt; font-weight:600; color:#202124;\"> </span><span style=\" font-family:\'inherit\'; font-size:20pt; font-weight:600; color:#202124;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:36px; background-color:#f8f9fa;\"><span style=\" font-family:\'inherit\'; font-size:20pt; font-weight:600; color:#202124;\"> </span><span style=\" font-family:\'inherit\'; font-size:20pt; font-weight:600; color:#3a44ff;\">Made With</span><span style=\" font-family:\'inherit\'; font-size:20pt; font-weight:600; color:#202124;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:36px; background-color:#f8f9fa;\"><span style=\" font-family:\'inherit\'; font-size:20pt; color:#202124;\">1. Python 3.6</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:36px; background-color:#f8f9fa;\"><span style=\" font-family:\'inherit\'; font-size:20pt; color:#202124;\">2. PyQt5</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:-2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:36px; background-color:#f8f9fa;\"><span style=\" font-family:\'inherit\'; font-size:20pt; color:#202124;\">3. MongoDB</span></p></body></html>"))
        self.A_exit_btn.setText(_translate("AboutWindow", "Exit"))
        self.label.setText(_translate("AboutWindow", "  Hospital Management System"))
        self.menuOption.setTitle(_translate("AboutWindow", "Option"))
        self.actionExit.setText(_translate("AboutWindow", "Main Menu"))
        self.actionExit_2.setText(_translate("AboutWindow", "Exit"))
        self.actionExit_3.setText(_translate("AboutWindow", "Exit"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutWindow = QtWidgets.QMainWindow()
    ui = Ui_AboutWindow()
    ui.setupUi(AboutWindow)
    AboutWindow.show()
    sys.exit(app.exec_())