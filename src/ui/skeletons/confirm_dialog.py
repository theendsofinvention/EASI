# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\DEV\EASI\EASIv0.0.11\src\ui\skeletons\confirm_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(300, 100)
        Dialog.setMinimumSize(QtCore.QSize(300, 100))
        Dialog.setMaximumSize(QtCore.QSize(300, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/app.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/pic/question.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))

from src.ui.resources import qt_resource_rc
