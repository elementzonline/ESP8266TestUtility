# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SMS_Bot.ui'
#
# Created: Fri Jun 24 16:55:17 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(590, 320)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/AIbEiAIAAABECP2Iptyl4PzmnAEiC3ZjYXJkX3Bob3RvKihiMjczYWVlNWQ1ZWVlNjYyY2U2NzA5YWUwNzgzMjE2MmZkMGYxN2Q5MAFyoVXTDsx0nC3OGfmWE7vsTYpe9Q.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("QDialog{background-image: url(:/background/Icons/background.jpg);background-repeat: repeat;}\n"
"\n"
"QToolBar{background:blue;}\n"
"\n"
"QTabWidget{background-color:blue;}\n"
"\n"
"QWidget#scrollArea{background-color: blue;}\n"
"QTabBar::tab { background: darkblue; color: white; padding: 10px; border: 2px solid blue;}\n"
"QTabBar::tab:selected {background: rgb(217, 217, 0);  color: black; }\n"
"QTabBar::tab:!selected {background:darkblue;  color: white;}\n"
"/*QTabBar {background-color: blue;} */\n"
"QTabBar::tab:hover{color:#ccc;    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.517, y2:1, stop:0 rgba(45, 45, 45, 255), stop:0.505682 rgba(45, 45, 45, 255), stop:1 rgba(29, 29, 29, 255));    border-color:#2d89ef;border-width:2px;}\n"
"\n"
"QPushButton{border-style:solid;background-color:darkblue;color:white;border-radius:3px;font: 12pt \"MS Shell Dlg 2\";}\n"
"QPushButton:hover{color:#ccc;    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.517, y2:1, stop:0 rgba(45, 45, 45, 255), stop:0.505682 rgba(45, 45, 45, 255), stop:1 rgba(29, 29, 29, 255));    border-color:#2d89ef;border-width:2px;}\n"
"QPushButton:pressed{background-color: lightblue;}\n"
"QPushButton:disabled{background-color: rgb(176, 176, 176);}\n"
"\n"
"QPushButton#connectButton{ background-color: darkred;}\n"
"QPushButton#connectButton:hover{color:#ccc;    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.517, y2:1, stop:0 rgba(45, 45, 45, 255), stop:0.505682 rgba(45, 45, 45, 255), stop:1 rgba(29, 29, 29, 255));    border-color:#2d89ef;border-width:2px;}\n"
"QPushButton#connectButton:pressed{background-color: lightblue;}\n"
"QPushButton#connectButton:disabled{background-color: rgb(176, 176, 176);}\n"
"\n"
"QComboBox{border-style:solid;background-color:darkblue;color:white;border-radius:3px;font: 12pt \"MS Shell Dlg 2\"; padding: 10px}\n"
"QComboBox:hover{color:#ccc;    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.517, y2:1, stop:0 rgba(45, 45, 45, 255), stop:0.505682 rgba(45, 45, 45, 255), stop:1 rgba(29, 29, 29, 255));    border-color:#2d89ef;border-width:2px;}\n"
"QComboBox:pressed{background-color: lightblue;}\n"
"\n"
"QLineEdit {border:4px outset; border-radius: 8px; border-color: blue; color:rgb(0, 0, 0);  background-color: rgb(235, 235, 235); padding:10px;font: 75 12pt \"MS Shell Dlg 2\";}\n"
"/*QLineEdit { border-radius: 8px;  color:black;background-color: white; } */\n"
"QLineEdit:focus {  border:4px outset; border-radius: 8px; border-color: rgb(41, 237, 215); color:rgb(0, 0, 0);  background-color: rgb(240, 204, 204); }\n"
"\n"
"QLabel {border:4px outset; border-radius: 0px; border-color: blue; color:white;  background-color: darkblue; padding:5px;font: 75 12pt \"MS Shell Dlg 2\";}\n"
"QPlainTextEdit {border:4px outset; border-radius: 0px; border-color: blue; color:black;  background-color: rgb(235, 235, 235);; padding:5px;font: 75 12pt \"MS Shell Dlg 2\";}"))
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(210, 70))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(139, 0, 0);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 0, 4, 1, 1)
        self.Connection_no_Chat = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Connection_no_Chat.sizePolicy().hasHeightForWidth())
        self.Connection_no_Chat.setSizePolicy(sizePolicy)
        self.Connection_no_Chat.setMinimumSize(QtCore.QSize(30, 0))
        self.Connection_no_Chat.setObjectName(_fromUtf8("Connection_no_Chat"))
        self.gridLayout_2.addWidget(self.Connection_no_Chat, 14, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.SEND_DATA = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SEND_DATA.sizePolicy().hasHeightForWidth())
        self.SEND_DATA.setSizePolicy(sizePolicy)
        self.SEND_DATA.setMinimumSize(QtCore.QSize(130, 50))
        self.SEND_DATA.setStyleSheet(_fromUtf8("background-color: rgb(0, 85, 0);"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/Telegram (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SEND_DATA.setIcon(icon1)
        self.SEND_DATA.setIconSize(QtCore.QSize(32, 32))
        self.SEND_DATA.setObjectName(_fromUtf8("SEND_DATA"))
        self.gridLayout_2.addWidget(self.SEND_DATA, 15, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 14, 2, 1, 1)
        self.Server_PlaintextEdit = QtGui.QPlainTextEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Server_PlaintextEdit.sizePolicy().hasHeightForWidth())
        self.Server_PlaintextEdit.setSizePolicy(sizePolicy)
        self.Server_PlaintextEdit.setMinimumSize(QtCore.QSize(210, 0))
        self.Server_PlaintextEdit.setReadOnly(True)
        self.Server_PlaintextEdit.setObjectName(_fromUtf8("Server_PlaintextEdit"))
        self.gridLayout_2.addWidget(self.Server_PlaintextEdit, 1, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 14, 4, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 14, 5, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 14, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 5, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem5, 16, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 1, 5, 1, 1)
        self.TCPUDP_Message = QtGui.QPlainTextEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TCPUDP_Message.sizePolicy().hasHeightForWidth())
        self.TCPUDP_Message.setSizePolicy(sizePolicy)
        self.TCPUDP_Message.setMinimumSize(QtCore.QSize(220, 0))
        self.TCPUDP_Message.setObjectName(_fromUtf8("TCPUDP_Message"))
        self.gridLayout_2.addWidget(self.TCPUDP_Message, 1, 1, 1, 1)
        self.Close_pushButton = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Close_pushButton.sizePolicy().hasHeightForWidth())
        self.Close_pushButton.setSizePolicy(sizePolicy)
        self.Close_pushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.Close_pushButton.setStyleSheet(_fromUtf8("background-color: rgb(139, 0, 0);"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/45420.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Close_pushButton.setIcon(icon2)
        self.Close_pushButton.setIconSize(QtCore.QSize(32, 32))
        self.Close_pushButton.setObjectName(_fromUtf8("Close_pushButton"))
        self.gridLayout_2.addWidget(self.Close_pushButton, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Elementz ESP Interactive Window", None))
        self.pushButton.setText(_translate("Dialog", " Status : Inactive", None))
        self.SEND_DATA.setText(_translate("Dialog", "Send", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">Connection:</p></body></html>", None))
        self.Close_pushButton.setText(_translate("Dialog", "Close Chat BOX", None))

import ESP_Resource_rc
