# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/convert/lrf_output.ui'
#
# Created: Thu Jul 19 23:32:30 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(588, 481)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.opt_autorotation = QtGui.QCheckBox(Form)
        self.opt_autorotation.setObjectName(_fromUtf8("opt_autorotation"))
        self.verticalLayout.addWidget(self.opt_autorotation)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.opt_wordspace = QtGui.QDoubleSpinBox(Form)
        self.opt_wordspace.setDecimals(1)
        self.opt_wordspace.setMinimum(1.0)
        self.opt_wordspace.setMaximum(20.0)
        self.opt_wordspace.setProperty("value", 2.5)
        self.opt_wordspace.setObjectName(_fromUtf8("opt_wordspace"))
        self.horizontalLayout.addWidget(self.opt_wordspace)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.opt_minimum_indent = QtGui.QDoubleSpinBox(Form)
        self.opt_minimum_indent.setDecimals(1)
        self.opt_minimum_indent.setObjectName(_fromUtf8("opt_minimum_indent"))
        self.horizontalLayout.addWidget(self.opt_minimum_indent)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.opt_render_tables_as_images = QtGui.QCheckBox(Form)
        self.opt_render_tables_as_images.setObjectName(_fromUtf8("opt_render_tables_as_images"))
        self.verticalLayout.addWidget(self.opt_render_tables_as_images)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.opt_text_size_multiplier_for_rendered_tables = QtGui.QDoubleSpinBox(Form)
        self.opt_text_size_multiplier_for_rendered_tables.setObjectName(_fromUtf8("opt_text_size_multiplier_for_rendered_tables"))
        self.horizontalLayout_2.addWidget(self.opt_text_size_multiplier_for_rendered_tables)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.opt_header = QtGui.QCheckBox(Form)
        self.opt_header.setObjectName(_fromUtf8("opt_header"))
        self.gridLayout.addWidget(self.opt_header, 0, 0, 1, 2)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 2)
        self.opt_header_separation = QtGui.QDoubleSpinBox(Form)
        self.opt_header_separation.setDecimals(1)
        self.opt_header_separation.setObjectName(_fromUtf8("opt_header_separation"))
        self.gridLayout.addWidget(self.opt_header_separation, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.opt_header_format = QtGui.QLineEdit(Form)
        self.opt_header_format.setObjectName(_fromUtf8("opt_header_format"))
        self.gridLayout.addWidget(self.opt_header_format, 2, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.opt_serif_family = QtGui.QComboBox(self.groupBox)
        self.opt_serif_family.setObjectName(_fromUtf8("opt_serif_family"))
        self.gridLayout_2.addWidget(self.opt_serif_family, 0, 1, 1, 1)
        self.opt_sans_family = QtGui.QComboBox(self.groupBox)
        self.opt_sans_family.setObjectName(_fromUtf8("opt_sans_family"))
        self.gridLayout_2.addWidget(self.opt_sans_family, 1, 1, 1, 1)
        self.opt_mono_family = QtGui.QComboBox(self.groupBox)
        self.opt_mono_family.setObjectName(_fromUtf8("opt_mono_family"))
        self.gridLayout_2.addWidget(self.opt_mono_family, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label.setBuddy(self.opt_wordspace)
        self.label_2.setBuddy(self.opt_minimum_indent)
        self.label_4.setBuddy(self.opt_header_separation)
        self.label_5.setBuddy(self.opt_header_format)
        self.label_6.setBuddy(self.opt_serif_family)
        self.label_7.setBuddy(self.opt_sans_family)
        self.label_8.setBuddy(self.opt_mono_family)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.opt_render_tables_as_images, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.opt_text_size_multiplier_for_rendered_tables.setEnabled)
        QtCore.QObject.connect(self.opt_header, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.opt_header_separation.setEnabled)
        QtCore.QObject.connect(self.opt_header, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.opt_header_format.setEnabled)
        QtCore.QObject.connect(self.opt_render_tables_as_images, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label_3.setEnabled)
        QtCore.QObject.connect(self.opt_header, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label_4.setEnabled)
        QtCore.QObject.connect(self.opt_header, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label_5.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.opt_autorotation.setText(_("Enable &autorotation of wide images"))
        self.label.setText(_("&Wordspace:"))
        self.opt_wordspace.setSuffix(_(" pt"))
        self.label_2.setText(_("Minimum para. &indent:"))
        self.opt_minimum_indent.setSuffix(_(" pt"))
        self.opt_render_tables_as_images.setText(_("Render &tables as images"))
        self.label_3.setText(_("Text size multiplier for text in rendered tables:"))
        self.opt_header.setText(_("Add &header"))
        self.label_4.setText(_("Header &separation:"))
        self.opt_header_separation.setSuffix(_(" pt"))
        self.label_5.setText(_("Header &format:"))
        self.groupBox.setTitle(_("&Embed fonts"))
        self.label_6.setText(_("&Serif font family:"))
        self.label_7.setText(_("S&ans-serif font family:"))
        self.label_8.setText(_("&Monospaced font family:"))

