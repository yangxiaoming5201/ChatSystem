# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(604, 385)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWhatsThis("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 80, 388, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("QLabel{\n"
"color: rgb(158, 2, 255);\n"
"\n"
"    background-color: rgb(255, 230, 230);\n"
"border-radius:35px;\n"
"border:2px solid #F3F5F5;\n"
"\n"
"font-size:15pt; \n"
"font-family: Roman times;\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.uesrname_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uesrname_edit.sizePolicy().hasHeightForWidth())
        self.uesrname_edit.setSizePolicy(sizePolicy)
        self.uesrname_edit.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #A0A0A0; /* 边框宽度为1px，颜色为#A0A0A0 */\n"
"    border-radius: 5px; /* 边框圆角 */\n"
"    padding-left: 5px; /* 文本距离左边界有5px */\n"
"    background-color: #F2F2F2; /* 背景颜色 */\n"
"    color: #A0A0A0; /* 文本颜色 */\n"
"    selection-background-color: #A0A0A0; /* 选中文本的背景颜色 */\n"
"    selection-color: #F2F2F2; /* 选中文本的颜色 */\n"
"    font-family: \"Microsoft YaHei\"; /* 文本字体族 */\n"
"    font-size: 10pt; /* 文本字体大小 */\n"
"}\n"
"\n"
"QLineEdit:hover { /* 鼠标悬浮在QLineEdit时的状态 */\n"
"    border: 2px solid #298DFF;\n"
"    border-radius: 5px;\n"
"    background-color: #F2F2F2;\n"
"    color: #298DFF;\n"
"    selection-background-color: #298DFF;\n"
"    selection-color: #F2F2F2;\n"
"}\n"
"\n"
"QLineEdit[echoMode=\"2\"] { /* QLineEdit有输入掩码时的状态 */\n"
"    lineedit-password-character: 9679;\n"
"    lineedit-password-mask-delay: 2000;\n"
"}\n"
"")
        self.uesrname_edit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.uesrname_edit.setObjectName("uesrname_edit")
        self.horizontalLayout.addWidget(self.uesrname_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("QLabel{\n"
"color: rgb(158, 2, 255);\n"
"background-color: rgb(255, 230, 230);\n"
"border-radius:35px;\n"
"border:2px solid #F3F5F5;\n"
"font-size:15pt; \n"
"font-family: Roman times;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.password_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_edit.sizePolicy().hasHeightForWidth())
        self.password_edit.setSizePolicy(sizePolicy)
        self.password_edit.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #A0A0A0; /* 边框宽度为1px，颜色为#A0A0A0 */\n"
"    border-radius: 5px; /* 边框圆角 */\n"
"    padding-left: 5px; /* 文本距离左边界有5px */\n"
"    background-color: #F2F2F2; /* 背景颜色 */\n"
"    color: #A0A0A0; /* 文本颜色 */\n"
"    selection-background-color: #A0A0A0; /* 选中文本的背景颜色 */\n"
"    selection-color: #F2F2F2; /* 选中文本的颜色 */\n"
"    font-family: \"Microsoft YaHei\"; /* 文本字体族 */\n"
"    font-size: 10pt; /* 文本字体大小 */\n"
"}\n"
"\n"
"QLineEdit:hover { /* 鼠标悬浮在QLineEdit时的状态 */\n"
"    border: 2px solid #298DFF;\n"
"    border-radius: 5px;\n"
"    background-color: #F2F2F2;\n"
"    color: #298DFF;\n"
"    selection-background-color: #298DFF;\n"
"    selection-color: #F2F2F2;\n"
"}\n"
"\n"
"QLineEdit[echoMode=\"2\"] { /* QLineEdit有输入掩码时的状态 */\n"
"    lineedit-password-character: 9679;\n"
"    lineedit-password-mask-delay: 2000;\n"
"}\n"
"")
        self.password_edit.setObjectName("password_edit")
        self.horizontalLayout_3.addWidget(self.password_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.login_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy)
        self.login_button.setStyleSheet("QPushButton{\n"
"    padding: 5px 25px;\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-right-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-width: 2px;\n"
"    border-radius: 8px;\n"
"    color: #616161;\n"
"    font-weight: bold;\n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    \n"
"    \n"
"}\n"
"QPushButton::default, QToolButton::default, QCommandLinkButton::default{\n"
"    border: 2px solid transparent;\n"
"    color: #FFFFFF;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);\n"
"}\n"
"QPushButton:hover, QToolButton:hover, QCommandLinkButton:hover{\n"
"    \n"
"    color: rgb(255, 79, 147);\n"
"}\n"
"QPushButton:pressed, QToolButton:pressed, QCommandLinkButton:pressed{\n"
"    color: #aeaeae;\n"
"    background-color:grey;\n"
"}")
        self.login_button.setObjectName("login_button")
        self.horizontalLayout_2.addWidget(self.login_button)
        self.register_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_button.sizePolicy().hasHeightForWidth())
        self.register_button.setSizePolicy(sizePolicy)
        self.register_button.setStyleSheet("QPushButton{\n"
"    padding: 5px 25px;\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-right-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-width: 2px;\n"
"    border-radius: 8px;\n"
"    color: #616161;\n"
"    font-weight: bold;\n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    \n"
"    \n"
"}\n"
"QPushButton::default, QToolButton::default, QCommandLinkButton::default{\n"
"    border: 2px solid transparent;\n"
"    color: #FFFFFF;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);\n"
"}\n"
"QPushButton:hover, QToolButton:hover, QCommandLinkButton:hover{\n"
"    \n"
"    color: rgb(255, 79, 147);\n"
"}\n"
"QPushButton:pressed, QToolButton:pressed, QCommandLinkButton:pressed{\n"
"    color: #aeaeae;\n"
"    background-color:grey;\n"
"}")
        self.register_button.setObjectName("register_button")
        self.horizontalLayout_2.addWidget(self.register_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 601, 351))
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(175, 255, 103, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: rgb(0, 0, 127);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.notice_label = QtWidgets.QLabel(self.centralwidget)
        self.notice_label.setGeometry(QtCore.QRect(200, 280, 301, 20))
        self.notice_label.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 9pt \"宋体\";")
        self.notice_label.setText("")
        self.notice_label.setObjectName("notice_label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 20, 221, 41))
        self.label_4.setStyleSheet("font: 9pt \"黑体\";\n"
"color: rgb(0, 0, 127);\n"
"background-color: rgb(226, 252, 255);\n"
"font-size:35px;\n"
"font-family:Roman times;")
        self.label_4.setObjectName("label_4")
        self.label_3.raise_()
        self.verticalLayoutWidget.raise_()
        self.notice_label.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "聊天系统"))
        self.label.setText(_translate("MainWindow", "用户名"))
        self.uesrname_edit.setPlaceholderText(_translate("MainWindow", "请输入用户名"))
        self.label_2.setText(_translate("MainWindow", "密码  "))
        self.password_edit.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.login_button.setText(_translate("MainWindow", "登录"))
        self.register_button.setText(_translate("MainWindow", "注册"))
        self.label_4.setText(_translate("MainWindow", "在线聊天系统"))
