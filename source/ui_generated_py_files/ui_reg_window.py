# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_reg_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 313)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: #040c0e;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 40px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    color: #be9063;\n"
"    font-weight: normal;\n"
"    text-decoration: none;\n"
"    font-style: normal;\n"
"    font-variant: small-caps;\n"
"    text-transform: lowercase;\n"
"}\n"
"QLabel:hover {\n"
"    font-size: 40px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    color: #F3E0D2;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    font-variant: small-caps;\n"
"    text-transform: lowercase;\n"
"    background-color: #132226;\n"
"    color: #a4978e;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #525b56;\n"
"    color: #a4978e;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #525b56;\n"
"    color: #a4978e;\n"
"    border-radius: 20px;\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    opacity: 0.6;\n"
"    padding: 5px\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: #828a86;\n"
"    color: #132226;\n"
"    opacity: 1;\n"
"}\n"
"\n"
"QFrame#frame {\n"
"    background-color: #132226;\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 2)
        self.enter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.enter_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.enter_btn.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.enter_btn.setFont(font)
        self.enter_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enter_btn.setObjectName("enter_btn")
        self.gridLayout_2.addWidget(self.enter_btn, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.register_btn = QtWidgets.QPushButton(self.centralwidget)
        self.register_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.register_btn.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.register_btn.setFont(font)
        self.register_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register_btn.setCheckable(False)
        self.register_btn.setObjectName("register_btn")
        self.gridLayout_2.addWidget(self.register_btn, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 150))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.login_le = QtWidgets.QLineEdit(self.frame)
        self.login_le.setMinimumSize(QtCore.QSize(400, 40))
        self.login_le.setAutoFillBackground(False)
        self.login_le.setText("")
        self.login_le.setFrame(True)
        self.login_le.setCursorPosition(0)
        self.login_le.setClearButtonEnabled(True)
        self.login_le.setObjectName("login_le")
        self.gridLayout.addWidget(self.login_le, 0, 1, 1, 1)
        self.login_lbl = QtWidgets.QLabel(self.frame)
        self.login_lbl.setStyleSheet("font-family: Verdana, Geneva, sans-serif;\n"
"font-size: 30px;\n"
"letter-spacing: 2px;\n"
"word-spacing: 6px;\n"
"color: #525b56;\n"
"font-weight: normal;\n"
"text-decoration: none;\n"
"font-style: normal;\n"
"font-variant: small-caps;\n"
"text-transform: lowercase;")
        self.login_lbl.setObjectName("login_lbl")
        self.gridLayout.addWidget(self.login_lbl, 0, 0, 1, 1)
        self.pwd_lbl = QtWidgets.QLabel(self.frame)
        self.pwd_lbl.setStyleSheet("font-family: Verdana, Geneva, sans-serif;\n"
"font-size: 30px;\n"
"letter-spacing: 2px;\n"
"word-spacing: 6px;\n"
"color: #525b56;\n"
"font-weight: normal;\n"
"text-decoration: none;\n"
"font-style: normal;\n"
"font-variant: small-caps;\n"
"text-transform: lowercase;")
        self.pwd_lbl.setObjectName("pwd_lbl")
        self.gridLayout.addWidget(self.pwd_lbl, 2, 0, 1, 1)
        self.pwd_le = QtWidgets.QLineEdit(self.frame)
        self.pwd_le.setMinimumSize(QtCore.QSize(400, 40))
        self.pwd_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd_le.setClearButtonEnabled(True)
        self.pwd_le.setObjectName("pwd_le")
        self.gridLayout.addWidget(self.pwd_le, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.remember_btn = QtWidgets.QPushButton(self.frame)
        self.remember_btn.setStyleSheet("QPushButton {\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    color: #a4978e;\n"
"    font-variant: small-caps;\n"
"    text-transform: lowercase;\n"
"    opacity: 50%;\n"
"    border-radius: 10px;\n"
"    background-color: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #828a86;\n"
"    color: #132226;\n"
"    opacity: 1;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #828a86;\n"
"    color: #132226;\n"
"    opacity: 1;\n"
"}")
        self.remember_btn.setCheckable(True)
        self.remember_btn.setObjectName("remember_btn")
        self.verticalLayout.addWidget(self.remember_btn)
        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вход"))
        self.enter_btn.setText(_translate("MainWindow", "войти"))
        self.label.setText(_translate("MainWindow", "авторизация"))
        self.register_btn.setText(_translate("MainWindow", "зарегистрировать пользователя"))
        self.login_lbl.setText(_translate("MainWindow", "логин"))
        self.pwd_lbl.setText(_translate("MainWindow", "пароль"))
        self.remember_btn.setText(_translate("MainWindow", "запомнить меня"))
