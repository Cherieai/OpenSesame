# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/preferences_widget.ui'
#
# Created: Tue Nov 26 13:40:32 2013
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_preferences_widget(object):
    def setupUi(self, preferences_widget):
        preferences_widget.setObjectName(_fromUtf8("preferences_widget"))
        preferences_widget.resize(834, 842)
        self.verticalLayout = QtGui.QVBoxLayout(preferences_widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(preferences_widget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 820, 828))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.checkbox_immediately_rename = QtGui.QCheckBox(self.groupBox_2)
        self.checkbox_immediately_rename.setObjectName(_fromUtf8("checkbox_immediately_rename"))
        self.gridLayout_5.addWidget(self.checkbox_immediately_rename, 0, 0, 1, 1)
        self.checkbox_autoresponse = QtGui.QCheckBox(self.groupBox_2)
        self.checkbox_autoresponse.setObjectName(_fromUtf8("checkbox_autoresponse"))
        self.gridLayout_5.addWidget(self.checkbox_autoresponse, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_5 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setContentsMargins(0, 9, 0, 0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_8 = QtGui.QLabel(self.groupBox_5)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 2)
        self.label_2 = QtGui.QLabel(self.groupBox_5)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.combobox_style = QtGui.QComboBox(self.groupBox_5)
        self.combobox_style.setObjectName(_fromUtf8("combobox_style"))
        self.gridLayout_4.addWidget(self.combobox_style, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1)
        self.combobox_theme = QtGui.QComboBox(self.groupBox_5)
        self.combobox_theme.setObjectName(_fromUtf8("combobox_theme"))
        self.gridLayout_4.addWidget(self.combobox_theme, 2, 1, 1, 1)
        self.checkbox_small_toolbar = QtGui.QCheckBox(self.groupBox_5)
        self.checkbox_small_toolbar.setObjectName(_fromUtf8("checkbox_small_toolbar"))
        self.gridLayout_4.addWidget(self.checkbox_small_toolbar, 3, 0, 1, 2)
        self.checkbox_toolbar_text = QtGui.QCheckBox(self.groupBox_5)
        self.checkbox_toolbar_text.setObjectName(_fromUtf8("checkbox_toolbar_text"))
        self.gridLayout_4.addWidget(self.checkbox_toolbar_text, 4, 0, 1, 2)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setContentsMargins(0, 9, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.checkbox_enable_autosave = QtGui.QCheckBox(self.groupBox)
        self.checkbox_enable_autosave.setObjectName(_fromUtf8("checkbox_enable_autosave"))
        self.gridLayout_3.addWidget(self.checkbox_enable_autosave, 0, 0, 1, 1)
        self.label_autosave_interval = QtGui.QLabel(self.groupBox)
        self.label_autosave_interval.setObjectName(_fromUtf8("label_autosave_interval"))
        self.gridLayout_3.addWidget(self.label_autosave_interval, 1, 0, 1, 1)
        self.spinbox_autosave_interval = QtGui.QSpinBox(self.groupBox)
        self.spinbox_autosave_interval.setMinimum(1)
        self.spinbox_autosave_interval.setMaximum(1000)
        self.spinbox_autosave_interval.setSingleStep(10)
        self.spinbox_autosave_interval.setObjectName(_fromUtf8("spinbox_autosave_interval"))
        self.gridLayout_3.addWidget(self.spinbox_autosave_interval, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.spinbox_autosave_max_age = QtGui.QSpinBox(self.groupBox)
        self.spinbox_autosave_max_age.setMinimum(1)
        self.spinbox_autosave_max_age.setMaximum(365)
        self.spinbox_autosave_max_age.setObjectName(_fromUtf8("spinbox_autosave_max_age"))
        self.gridLayout_3.addWidget(self.spinbox_autosave_max_age, 2, 1, 1, 1)
        self.button_browse_autosave = QtGui.QPushButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/browse.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_browse_autosave.setIcon(icon)
        self.button_browse_autosave.setObjectName(_fromUtf8("button_browse_autosave"))
        self.gridLayout_3.addWidget(self.button_browse_autosave, 3, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.checkbox_auto_update_check = QtGui.QCheckBox(self.groupBox_3)
        self.checkbox_auto_update_check.setObjectName(_fromUtf8("checkbox_auto_update_check"))
        self.gridLayout_6.addWidget(self.checkbox_auto_update_check, 0, 0, 1, 1)
        self.button_update_check = QtGui.QPushButton(self.groupBox_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/update.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_update_check.setIcon(icon1)
        self.button_update_check.setObjectName(_fromUtf8("button_update_check"))
        self.gridLayout_6.addWidget(self.button_update_check, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout.setContentsMargins(0, 9, 0, 0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.combobox_runner = QtGui.QComboBox(self.groupBox_4)
        self.combobox_runner.setObjectName(_fromUtf8("combobox_runner"))
        self.combobox_runner.addItem(_fromUtf8(""))
        self.combobox_runner.addItem(_fromUtf8(""))
        self.combobox_runner.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.combobox_runner, 1, 0, 1, 2)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_6 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setContentsMargins(0, 9, 0, 0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_6 = QtGui.QLabel(self.groupBox_6)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)
        self.edit_plugin_folders = QtGui.QLineEdit(self.groupBox_6)
        self.edit_plugin_folders.setReadOnly(True)
        self.edit_plugin_folders.setObjectName(_fromUtf8("edit_plugin_folders"))
        self.gridLayout_7.addWidget(self.edit_plugin_folders, 0, 1, 1, 1)
        self.widget_plugin_list = QtGui.QWidget(self.groupBox_6)
        self.widget_plugin_list.setObjectName(_fromUtf8("widget_plugin_list"))
        self.layout_plugin_list = QtGui.QVBoxLayout(self.widget_plugin_list)
        self.layout_plugin_list.setMargin(0)
        self.layout_plugin_list.setObjectName(_fromUtf8("layout_plugin_list"))
        self.label_plugin_dummy = QtGui.QLabel(self.widget_plugin_list)
        self.label_plugin_dummy.setObjectName(_fromUtf8("label_plugin_dummy"))
        self.layout_plugin_list.addWidget(self.label_plugin_dummy)
        self.gridLayout_7.addWidget(self.widget_plugin_list, 1, 0, 1, 2)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(preferences_widget)
        QtCore.QObject.connect(self.checkbox_enable_autosave, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.spinbox_autosave_interval.setEnabled)
        QtCore.QObject.connect(self.checkbox_enable_autosave, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label_autosave_interval.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(preferences_widget)

    def retranslateUi(self, preferences_widget):
        preferences_widget.setWindowTitle(_translate("preferences_widget", "Form", None))
        self.groupBox_2.setTitle(_translate("preferences_widget", "Miscellaneous", None))
        self.checkbox_immediately_rename.setText(_translate("preferences_widget", "Offer to rename new items immediately", None))
        self.checkbox_autoresponse.setText(_translate("preferences_widget", "Enable auto-response", None))
        self.groupBox_5.setTitle(_translate("preferences_widget", "Appearance", None))
        self.label_8.setText(_translate("preferences_widget", "<small><i>Changes take effect the next time you start OpenSesame</i></small>\n"
"", None))
        self.label_2.setText(_translate("preferences_widget", "Interface style", None))
        self.label_7.setText(_translate("preferences_widget", "icon theme", None))
        self.checkbox_small_toolbar.setText(_translate("preferences_widget", "Small icons in toolbar", None))
        self.checkbox_toolbar_text.setText(_translate("preferences_widget", "Show text in toolbar", None))
        self.groupBox.setTitle(_translate("preferences_widget", "Backups", None))
        self.checkbox_enable_autosave.setText(_translate("preferences_widget", "Automatically create backups", None))
        self.label_autosave_interval.setText(_translate("preferences_widget", "Auto-save interval:", None))
        self.spinbox_autosave_interval.setSuffix(_translate("preferences_widget", " minute(s)", None))
        self.spinbox_autosave_interval.setPrefix(_translate("preferences_widget", "every ", None))
        self.label_3.setText(_translate("preferences_widget", "Clean backups after:", None))
        self.spinbox_autosave_max_age.setSuffix(_translate("preferences_widget", " day(s)", None))
        self.button_browse_autosave.setText(_translate("preferences_widget", "Open backup folder", None))
        self.groupBox_3.setTitle(_translate("preferences_widget", "Updates", None))
        self.checkbox_auto_update_check.setText(_translate("preferences_widget", "Check for updates on start-up", None))
        self.button_update_check.setText(_translate("preferences_widget", "Check for updates now", None))
        self.groupBox_4.setTitle(_translate("preferences_widget", "Runner", None))
        self.label.setText(_translate("preferences_widget", "<html><head/><body><p><span style=\" font-size:8pt; font-style:italic;\">The \'runner\' determines how your OpenSesame experiment is executed. For more information, please visit </span><a href=\"http://osdoc.cogsci.nl/miscellaneous/runners\"><span style=\" font-size:8pt; font-style:italic; text-decoration: underline; color:#0057ae;\">http://osdoc.cogsci.nl/miscellaneous/runners</span></a><span style=\" font-size:8pt; font-style:italic;\">.</span></p></body></html>", None))
        self.combobox_runner.setItemText(0, _translate("preferences_widget", "Run experiment in the same process (inprocess)", None))
        self.combobox_runner.setItemText(1, _translate("preferences_widget", "Run experiment in a separate process (multiprocess)", None))
        self.combobox_runner.setItemText(2, _translate("preferences_widget", "Run experiment with opensesamerun (external)", None))
        self.groupBox_6.setTitle(_translate("preferences_widget", "Plug-ins", None))
        self.label_6.setText(_translate("preferences_widget", "Plug-in folders:", None))
        self.label_plugin_dummy.setText(_translate("preferences_widget", "Installed plug-ins (requires restart):", None))
