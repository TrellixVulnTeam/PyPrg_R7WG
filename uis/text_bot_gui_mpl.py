# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text_bot_gui_mpl.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1082, 803)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Main_text_window = QtWidgets.QTextEdit(self.centralwidget)
        self.Main_text_window.setObjectName("Main_text_window")
        self.verticalLayout.addWidget(self.Main_text_window)
        self.input_text_line = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_text_line.sizePolicy().hasHeightForWidth())
        self.input_text_line.setSizePolicy(sizePolicy)
        self.input_text_line.setMinimumSize(QtCore.QSize(0, 30))
        self.input_text_line.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input_text_line.setObjectName("input_text_line")
        self.verticalLayout.addWidget(self.input_text_line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_2.addWidget(self.horizontalSlider)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 30))
        self.lcdNumber.setMaximumSize(QtCore.QSize(40, 30))
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_2.addWidget(self.lcdNumber)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        self.label_path_openfile = QtWidgets.QLabel(self.centralwidget)
        self.label_path_openfile.setObjectName("label_path_openfile")
        self.verticalLayout_3.addWidget(self.label_path_openfile)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BtnOpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.BtnOpenFile.setMaximumSize(QtCore.QSize(100, 40))
        self.BtnOpenFile.setObjectName("BtnOpenFile")
        self.horizontalLayout_3.addWidget(self.BtnOpenFile)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1082, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextBot"))
        self.pushButton.setText(_translate("MainWindow", "Ответ"))
        self.label_path_openfile.setText(_translate("MainWindow", "TextLabel"))
        self.BtnOpenFile.setText(_translate("MainWindow", "Открыть файл"))
