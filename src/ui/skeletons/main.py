# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\DEV\EASI\EASIv0.0.11\src\ui\skeletons\main.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.group_active_dcs_installation = QtWidgets.QGroupBox(self.centralwidget)
        self.group_active_dcs_installation.setObjectName("group_active_dcs_installation")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.group_active_dcs_installation)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.group_active_dcs_installation)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.combo_active_dcs_installation = QtWidgets.QComboBox(self.group_active_dcs_installation)
        self.combo_active_dcs_installation.setMinimumSize(QtCore.QSize(0, 20))
        self.combo_active_dcs_installation.setMaximumSize(QtCore.QSize(16777215, 20))
        self.combo_active_dcs_installation.setObjectName("combo_active_dcs_installation")
        self.horizontalLayout_2.addWidget(self.combo_active_dcs_installation)
        self.btn_active_dcs_installation_open_in_explorer = QtWidgets.QToolButton(self.group_active_dcs_installation)
        self.btn_active_dcs_installation_open_in_explorer.setMinimumSize(QtCore.QSize(0, 20))
        self.btn_active_dcs_installation_open_in_explorer.setMaximumSize(QtCore.QSize(16777215, 20))
        self.btn_active_dcs_installation_open_in_explorer.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_active_dcs_installation_open_in_explorer.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btn_active_dcs_installation_open_in_explorer.setAutoRaise(True)
        self.btn_active_dcs_installation_open_in_explorer.setArrowType(QtCore.Qt.DownArrow)
        self.btn_active_dcs_installation_open_in_explorer.setObjectName("btn_active_dcs_installation_open_in_explorer")
        self.horizontalLayout_2.addWidget(self.btn_active_dcs_installation_open_in_explorer)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_dcs_version_static = QtWidgets.QLabel(self.group_active_dcs_installation)
        self.label_dcs_version_static.setObjectName("label_dcs_version_static")
        self.horizontalLayout_2.addWidget(self.label_dcs_version_static)
        self.label_dcs_version = QtWidgets.QLabel(self.group_active_dcs_installation)
        self.label_dcs_version.setText("")
        self.label_dcs_version.setObjectName("label_dcs_version")
        self.horizontalLayout_2.addWidget(self.label_dcs_version)
        self.verticalLayout.addWidget(self.group_active_dcs_installation)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_mods = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mods.sizePolicy().hasHeightForWidth())
        self.btn_mods.setSizePolicy(sizePolicy)
        self.btn_mods.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_mods.setCheckable(True)
        self.btn_mods.setAutoExclusive(True)
        self.btn_mods.setAutoRaise(True)
        self.btn_mods.setObjectName("btn_mods")
        self.horizontalLayout_4.addWidget(self.btn_mods)
        self.btn_repos = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_repos.sizePolicy().hasHeightForWidth())
        self.btn_repos.setSizePolicy(sizePolicy)
        self.btn_repos.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_repos.setCheckable(True)
        self.btn_repos.setAutoExclusive(True)
        self.btn_repos.setAutoRaise(True)
        self.btn_repos.setObjectName("btn_repos")
        self.horizontalLayout_4.addWidget(self.btn_repos)
        self.btn_editor = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_editor.sizePolicy().hasHeightForWidth())
        self.btn_editor.setSizePolicy(sizePolicy)
        self.btn_editor.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_editor.setCheckable(True)
        self.btn_editor.setAutoExclusive(True)
        self.btn_editor.setAutoRaise(True)
        self.btn_editor.setObjectName("btn_editor")
        self.horizontalLayout_4.addWidget(self.btn_editor)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.verticalLayout.addLayout(self.main_layout)
        self.verticalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuMod_authoring = QtWidgets.QMenu(self.menubar)
        self.menuMod_authoring.setObjectName("menuMod_authoring")
        self.menuTesting = QtWidgets.QMenu(self.menubar)
        self.menuTesting.setObjectName("menuTesting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName("actionExit")
        self.actionEASI_Settings = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pic/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEASI_Settings.setIcon(icon1)
        self.actionEASI_Settings.setObjectName("actionEASI_Settings")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionFeedback = QtWidgets.QAction(MainWindow)
        self.actionFeedback.setObjectName("actionFeedback")
        self.actionTest_dialog = QtWidgets.QAction(MainWindow)
        self.actionTest_dialog.setObjectName("actionTest_dialog")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionEASI_Settings)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionFeedback)
        self.menuTesting.addAction(self.actionTest_dialog)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuMod_authoring.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuTesting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.group_active_dcs_installation.setTitle(_translate("MainWindow", "Active DCS installation: "))
        self.btn_active_dcs_installation_open_in_explorer.setText(_translate("MainWindow", "Show in explorer"))
        self.label_dcs_version_static.setText(_translate("MainWindow", "Version of DCS: "))
        self.btn_mods.setText(_translate("MainWindow", "Mods"))
        self.btn_repos.setText(_translate("MainWindow", "Repositories"))
        self.btn_editor.setText(_translate("MainWindow", "Mod editor"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuMod_authoring.setTitle(_translate("MainWindow", "Mod authoring"))
        self.menuTesting.setTitle(_translate("MainWindow", "Testing"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))
        self.actionEASI_Settings.setText(_translate("MainWindow", "EASI settings"))
        self.actionEASI_Settings.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionFeedback.setText(_translate("MainWindow", "Feedback"))
        self.actionTest_dialog.setText(_translate("MainWindow", "Test dialog"))

from src.ui.resources import qt_resource_rc
