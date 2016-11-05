# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\DEV\EASI\EASIv0.0.11\src\ui\skeletons\config_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.setWindowModality(QtCore.Qt.ApplicationModal)
        Settings.resize(1024, 768)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Settings.setWindowIcon(icon)
        Settings.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Settings)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_general = QtWidgets.QWidget()
        self.tab_general.setObjectName("tab_general")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_general)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.grp_path = QtWidgets.QGroupBox(self.tab_general)
        self.grp_path.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.grp_path.setObjectName("grp_path")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.grp_path)
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.layout_paths = QtWidgets.QGridLayout()
        self.layout_paths.setObjectName("layout_paths")
        self.btn_cache = QtWidgets.QToolButton(self.grp_path)
        self.btn_cache.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_cache.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btn_cache.setAutoRaise(True)
        self.btn_cache.setArrowType(QtCore.Qt.DownArrow)
        self.btn_cache.setObjectName("btn_cache")
        self.layout_paths.addWidget(self.btn_cache, 1, 2, 1, 1)
        self.cache_line_edit = QtWidgets.QLineEdit(self.grp_path)
        self.cache_line_edit.setObjectName("cache_line_edit")
        self.layout_paths.addWidget(self.cache_line_edit, 1, 1, 1, 1)
        self.labelcache = QtWidgets.QLabel(self.grp_path)
        self.labelcache.setObjectName("labelcache")
        self.layout_paths.addWidget(self.labelcache, 1, 0, 1, 1)
        self.btn_sg = QtWidgets.QToolButton(self.grp_path)
        self.btn_sg.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_sg.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btn_sg.setAutoRaise(True)
        self.btn_sg.setArrowType(QtCore.Qt.DownArrow)
        self.btn_sg.setObjectName("btn_sg")
        self.layout_paths.addWidget(self.btn_sg, 0, 2, 1, 1)
        self.sg_label = QtWidgets.QLabel(self.grp_path)
        self.sg_label.setObjectName("sg_label")
        self.layout_paths.addWidget(self.sg_label, 0, 0, 1, 1)
        self.sg_line_edit = QtWidgets.QLineEdit(self.grp_path)
        self.sg_line_edit.setObjectName("sg_line_edit")
        self.layout_paths.addWidget(self.sg_line_edit, 0, 1, 1, 1)
        self.labelkdiff = QtWidgets.QLabel(self.grp_path)
        self.labelkdiff.setObjectName("labelkdiff")
        self.layout_paths.addWidget(self.labelkdiff, 2, 0, 1, 1)
        self.kdiff_line_edit = QtWidgets.QLineEdit(self.grp_path)
        self.kdiff_line_edit.setObjectName("kdiff_line_edit")
        self.layout_paths.addWidget(self.kdiff_line_edit, 2, 1, 1, 1)
        self.btn_kdiff = QtWidgets.QToolButton(self.grp_path)
        self.btn_kdiff.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_kdiff.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btn_kdiff.setAutoRaise(True)
        self.btn_kdiff.setArrowType(QtCore.Qt.DownArrow)
        self.btn_kdiff.setObjectName("btn_kdiff")
        self.layout_paths.addWidget(self.btn_kdiff, 2, 2, 1, 1)
        self.verticalLayout_8.addLayout(self.layout_paths)
        self.verticalLayout_2.addWidget(self.grp_path)
        self.grp_mod_Creator_mode = QtWidgets.QGroupBox(self.tab_general)
        self.grp_mod_Creator_mode.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.grp_mod_Creator_mode.setObjectName("grp_mod_Creator_mode")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.grp_mod_Creator_mode)
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.author_mode = QtWidgets.QCheckBox(self.grp_mod_Creator_mode)
        self.author_mode.setObjectName("author_mode")
        self.verticalLayout_9.addWidget(self.author_mode)
        self.verticalLayout_2.addWidget(self.grp_mod_Creator_mode)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.grp_easi_update = QtWidgets.QGroupBox(self.tab_general)
        self.grp_easi_update.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.grp_easi_update.setObjectName("grp_easi_update")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.grp_easi_update)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.update_auto = QtWidgets.QCheckBox(self.grp_easi_update)
        self.update_auto.setEnabled(False)
        self.update_auto.setChecked(True)
        self.update_auto.setObjectName("update_auto")
        self.verticalLayout_3.addWidget(self.update_auto)
        self.subscribe_to_test_versions = QtWidgets.QCheckBox(self.grp_easi_update)
        self.subscribe_to_test_versions.setObjectName("subscribe_to_test_versions")
        self.verticalLayout_3.addWidget(self.subscribe_to_test_versions)
        self.btn_update_check = QtWidgets.QPushButton(self.grp_easi_update)
        self.btn_update_check.setObjectName("btn_update_check")
        self.verticalLayout_3.addWidget(self.btn_update_check)
        self.verticalLayout_2.addWidget(self.grp_easi_update)
        self.tabWidget.addTab(self.tab_general, "")
        self.tab_credentials = QtWidgets.QWidget()
        self.tab_credentials.setObjectName("tab_credentials")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_credentials)
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_encrypt = QtWidgets.QGroupBox(self.tab_credentials)
        self.groupBox_encrypt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_encrypt.setObjectName("groupBox_encrypt")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_encrypt)
        self.verticalLayout_5.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(40)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.groupBox_encrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(32, 32))
        self.label.setMaximumSize(QtCore.QSize(32, 32))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/pic/key.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_encrypt = QtWidgets.QLabel(self.groupBox_encrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_encrypt.sizePolicy().hasHeightForWidth())
        self.label_encrypt.setSizePolicy(sizePolicy)
        self.label_encrypt.setWordWrap(True)
        self.label_encrypt.setObjectName("label_encrypt")
        self.verticalLayout_6.addWidget(self.label_encrypt)
        self.check_box_encrypt = QtWidgets.QCheckBox(self.groupBox_encrypt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_box_encrypt.sizePolicy().hasHeightForWidth())
        self.check_box_encrypt.setSizePolicy(sizePolicy)
        self.check_box_encrypt.setObjectName("check_box_encrypt")
        self.verticalLayout_6.addWidget(self.check_box_encrypt)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addWidget(self.groupBox_encrypt)
        self.grp_github = QtWidgets.QGroupBox(self.tab_credentials)
        self.grp_github.setObjectName("grp_github")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.grp_github)
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_4.addWidget(self.grp_github)
        self.verticalGroupBox = QtWidgets.QGroupBox(self.tab_credentials)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_12.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(40)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_dropbox_pic = QtWidgets.QLabel(self.verticalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dropbox_pic.sizePolicy().hasHeightForWidth())
        self.label_dropbox_pic.setSizePolicy(sizePolicy)
        self.label_dropbox_pic.setMinimumSize(QtCore.QSize(32, 32))
        self.label_dropbox_pic.setMaximumSize(QtCore.QSize(32, 32))
        self.label_dropbox_pic.setText("")
        self.label_dropbox_pic.setPixmap(QtGui.QPixmap(":/pic/dropbox.png"))
        self.label_dropbox_pic.setScaledContents(True)
        self.label_dropbox_pic.setObjectName("label_dropbox_pic")
        self.horizontalLayout_4.addWidget(self.label_dropbox_pic)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSpacing(7)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_db_create_account = QtWidgets.QLabel(self.verticalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_db_create_account.sizePolicy().hasHeightForWidth())
        self.label_db_create_account.setSizePolicy(sizePolicy)
        self.label_db_create_account.setObjectName("label_db_create_account")
        self.verticalLayout_13.addWidget(self.label_db_create_account)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_db_status_static = QtWidgets.QLabel(self.verticalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_db_status_static.sizePolicy().hasHeightForWidth())
        self.label_db_status_static.setSizePolicy(sizePolicy)
        self.label_db_status_static.setObjectName("label_db_status_static")
        self.horizontalLayout_5.addWidget(self.label_db_status_static)
        self.label_db_status = QtWidgets.QLabel(self.verticalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_db_status.sizePolicy().hasHeightForWidth())
        self.label_db_status.setSizePolicy(sizePolicy)
        self.label_db_status.setObjectName("label_db_status")
        self.horizontalLayout_5.addWidget(self.label_db_status)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_13.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_db_validation_code_static = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_db_validation_code_static.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_db_validation_code_static.sizePolicy().hasHeightForWidth())
        self.label_db_validation_code_static.setSizePolicy(sizePolicy)
        self.label_db_validation_code_static.setObjectName("label_db_validation_code_static")
        self.horizontalLayout.addWidget(self.label_db_validation_code_static)
        self.line_edit_db_validation_code = QtWidgets.QLineEdit(self.verticalGroupBox)
        self.line_edit_db_validation_code.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_db_validation_code.sizePolicy().hasHeightForWidth())
        self.line_edit_db_validation_code.setSizePolicy(sizePolicy)
        self.line_edit_db_validation_code.setObjectName("line_edit_db_validation_code")
        self.horizontalLayout.addWidget(self.line_edit_db_validation_code)
        self.btn_db_check_code = QtWidgets.QPushButton(self.verticalGroupBox)
        self.btn_db_check_code.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_db_check_code.sizePolicy().hasHeightForWidth())
        self.btn_db_check_code.setSizePolicy(sizePolicy)
        self.btn_db_check_code.setObjectName("btn_db_check_code")
        self.horizontalLayout.addWidget(self.btn_db_check_code)
        self.btn_db_create = QtWidgets.QPushButton(self.verticalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_db_create.sizePolicy().hasHeightForWidth())
        self.btn_db_create.setSizePolicy(sizePolicy)
        self.btn_db_create.setMinimumSize(QtCore.QSize(120, 0))
        self.btn_db_create.setObjectName("btn_db_create")
        self.horizontalLayout.addWidget(self.btn_db_create)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_13.addLayout(self.horizontalLayout)
        self.label_db_tokens_http_link = QtWidgets.QLabel(self.verticalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_db_tokens_http_link.sizePolicy().hasHeightForWidth())
        self.label_db_tokens_http_link.setSizePolicy(sizePolicy)
        self.label_db_tokens_http_link.setTextFormat(QtCore.Qt.RichText)
        self.label_db_tokens_http_link.setOpenExternalLinks(True)
        self.label_db_tokens_http_link.setObjectName("label_db_tokens_http_link")
        self.verticalLayout_13.addWidget(self.label_db_tokens_http_link)
        self.horizontalLayout_4.addLayout(self.verticalLayout_13)
        self.verticalLayout_12.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addWidget(self.verticalGroupBox)
        self.tabWidget.addTab(self.tab_credentials, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Settings)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.grp_path.setTitle(_translate("Settings", "Paths"))
        self.btn_cache.setText(_translate("Settings", "...  "))
        self.labelcache.setText(_translate("Settings", "Cache"))
        self.btn_sg.setText(_translate("Settings", "...  "))
        self.sg_label.setText(_translate("Settings", "Saved Games"))
        self.labelkdiff.setText(_translate("Settings", "KDiff3"))
        self.btn_kdiff.setText(_translate("Settings", "...  "))
        self.grp_mod_Creator_mode.setTitle(_translate("Settings", "Author mode"))
        self.author_mode.setText(_translate("Settings", "Enable author mode"))
        self.grp_easi_update.setTitle(_translate("Settings", "EASI updates"))
        self.update_auto.setText(_translate("Settings", "Automatically update EASI during startup (this feature cannot be turned off at the time being)"))
        self.subscribe_to_test_versions.setText(_translate("Settings", "Update to experimental versions of EASI (for testing purposes only)"))
        self.btn_update_check.setText(_translate("Settings", "Check now"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), _translate("Settings", "General"))
        self.groupBox_encrypt.setTitle(_translate("Settings", "Encryption"))
        self.label_encrypt.setText(_translate("Settings", "<html><head/><body><p>If you so desire, you can further protect your credentials by encrypting the fil in which EASI writes them. Note that the encryption will be <span style=\" font-weight:600;\">linked to the current Windows installation</span> and will not be retrievable if you lose access to this machine.</p></body></html>"))
        self.check_box_encrypt.setText(_translate("Settings", "Encrypt my credentials"))
        self.grp_github.setTitle(_translate("Settings", "Github"))
        self.verticalGroupBox.setTitle(_translate("Settings", "Dropbox"))
        self.label_db_create_account.setText(_translate("Settings", "<html><head/><body><p>Don\'t have a Dropbox account ? <a href=\"https://www.dropbox.com/login\"><span style=\" text-decoration: underline; color:#0000ff;\">Create one here</span></a></p></body></html>"))
        self.label_db_status_static.setText(_translate("Settings", "Status: "))
        self.label_db_status.setText(_translate("Settings", "TextLabel"))
        self.label_db_validation_code_static.setText(_translate("Settings", "Validation code:"))
        self.btn_db_check_code.setText(_translate("Settings", "Check code"))
        self.btn_db_create.setText(_translate("Settings", "Create token"))
        self.label_db_tokens_http_link.setText(_translate("Settings", "<html><head/><body><p>You can see your active Dropbox tokens at: <a href=\"https://www.dropbox.com/account#security\"><span style=\" text-decoration: underline; color:#0000ff;\">https://www.dropbox.com/account#security</span></a></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_credentials), _translate("Settings", "Credentials"))

from src.ui.resources import qt_resource_rc
