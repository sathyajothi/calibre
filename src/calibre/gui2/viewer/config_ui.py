# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/viewer/config.ui'
#
# Created: Thu Jul 19 23:32:29 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(839, 630)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("config.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_4 = QtGui.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_4.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.tabs = QtGui.QTabWidget(Dialog)
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.serif_family = QtGui.QFontComboBox(self.groupBox)
        self.serif_family.setObjectName(_fromUtf8("serif_family"))
        self.gridLayout.addWidget(self.serif_family, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.sans_family = QtGui.QFontComboBox(self.groupBox)
        self.sans_family.setObjectName(_fromUtf8("sans_family"))
        self.gridLayout.addWidget(self.sans_family, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.mono_family = QtGui.QFontComboBox(self.groupBox)
        self.mono_family.setObjectName(_fromUtf8("mono_family"))
        self.gridLayout.addWidget(self.mono_family, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.default_font_size = QtGui.QSpinBox(self.groupBox)
        self.default_font_size.setMinimum(8)
        self.default_font_size.setMaximum(40)
        self.default_font_size.setObjectName(_fromUtf8("default_font_size"))
        self.gridLayout.addWidget(self.default_font_size, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.mono_font_size = QtGui.QSpinBox(self.groupBox)
        self.mono_font_size.setMinimum(8)
        self.mono_font_size.setMaximum(50)
        self.mono_font_size.setObjectName(_fromUtf8("mono_font_size"))
        self.gridLayout.addWidget(self.mono_font_size, 4, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.standard_font = QtGui.QComboBox(self.groupBox)
        self.standard_font.setObjectName(_fromUtf8("standard_font"))
        self.standard_font.addItem(_fromUtf8(""))
        self.standard_font.addItem(_fromUtf8(""))
        self.standard_font.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.standard_font, 5, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.hyphenate = QtGui.QCheckBox(self.tab)
        self.hyphenate.setObjectName(_fromUtf8("hyphenate"))
        self.gridLayout_2.addWidget(self.hyphenate, 5, 0, 1, 2)
        self.hyphenate_default_lang = QtGui.QComboBox(self.tab)
        self.hyphenate_default_lang.setObjectName(_fromUtf8("hyphenate_default_lang"))
        self.gridLayout_2.addWidget(self.hyphenate_default_lang, 6, 1, 1, 1)
        self.hyphenate_label = QtGui.QLabel(self.tab)
        self.hyphenate_label.setObjectName(_fromUtf8("hyphenate_label"))
        self.gridLayout_2.addWidget(self.hyphenate_label, 6, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 4, 0, 1, 1)
        self.opt_page_flip_duration = QtGui.QDoubleSpinBox(self.tab)
        self.opt_page_flip_duration.setDecimals(1)
        self.opt_page_flip_duration.setMinimum(0.1)
        self.opt_page_flip_duration.setMaximum(3.0)
        self.opt_page_flip_duration.setSingleStep(0.1)
        self.opt_page_flip_duration.setProperty("value", 0.5)
        self.opt_page_flip_duration.setObjectName(_fromUtf8("opt_page_flip_duration"))
        self.gridLayout_2.addWidget(self.opt_page_flip_duration, 4, 1, 1, 1)
        self.max_fs_width = QtGui.QSpinBox(self.tab)
        self.max_fs_width.setMinimum(100)
        self.max_fs_width.setMaximum(10000)
        self.max_fs_width.setObjectName(_fromUtf8("max_fs_width"))
        self.gridLayout_2.addWidget(self.max_fs_width, 3, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)
        self.opt_font_mag_step = QtGui.QSpinBox(self.tab)
        self.opt_font_mag_step.setObjectName(_fromUtf8("opt_font_mag_step"))
        self.gridLayout_2.addWidget(self.opt_font_mag_step, 0, 1, 1, 1)
        self.opt_fit_images = QtGui.QCheckBox(self.tab)
        self.opt_fit_images.setObjectName(_fromUtf8("opt_fit_images"))
        self.gridLayout_2.addWidget(self.opt_fit_images, 7, 0, 1, 1)
        self.opt_remember_window_size = QtGui.QCheckBox(self.tab)
        self.opt_remember_window_size.setObjectName(_fromUtf8("opt_remember_window_size"))
        self.gridLayout_2.addWidget(self.opt_remember_window_size, 8, 0, 1, 1)
        self.opt_wheel_flips_pages = QtGui.QCheckBox(self.tab)
        self.opt_wheel_flips_pages.setObjectName(_fromUtf8("opt_wheel_flips_pages"))
        self.gridLayout_2.addWidget(self.opt_wheel_flips_pages, 7, 1, 1, 1)
        self.opt_remember_current_page = QtGui.QCheckBox(self.tab)
        self.opt_remember_current_page.setObjectName(_fromUtf8("opt_remember_current_page"))
        self.gridLayout_2.addWidget(self.opt_remember_current_page, 8, 1, 1, 1)
        self.opt_line_scrolling_stops_on_pagebreaks = QtGui.QCheckBox(self.tab)
        self.opt_line_scrolling_stops_on_pagebreaks.setObjectName(_fromUtf8("opt_line_scrolling_stops_on_pagebreaks"))
        self.gridLayout_2.addWidget(self.opt_line_scrolling_stops_on_pagebreaks, 9, 0, 1, 1)
        self.opt_fullscreen_clock = QtGui.QCheckBox(self.tab)
        self.opt_fullscreen_clock.setObjectName(_fromUtf8("opt_fullscreen_clock"))
        self.gridLayout_2.addWidget(self.opt_fullscreen_clock, 9, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.tabs.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout.addWidget(self.label_9)
        self.tabs.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_10 = QtGui.QLabel(self.tab_3)
        self.label_10.setWordWrap(True)
        self.label_10.setOpenExternalLinks(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_3.addWidget(self.label_10)
        self.css = QtGui.QPlainTextEdit(self.tab_3)
        self.css.setObjectName(_fromUtf8("css"))
        self.verticalLayout_3.addWidget(self.css)
        self.tabs.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.tabs, 0, 0, 1, 1)
        self.label.setBuddy(self.serif_family)
        self.label_2.setBuddy(self.sans_family)
        self.label_3.setBuddy(self.mono_family)
        self.label_4.setBuddy(self.default_font_size)
        self.label_5.setBuddy(self.mono_font_size)
        self.label_6.setBuddy(self.standard_font)
        self.hyphenate_label.setBuddy(self.hyphenate_default_lang)
        self.label_11.setBuddy(self.opt_page_flip_duration)
        self.label_7.setBuddy(self.max_fs_width)
        self.label_12.setBuddy(self.opt_font_mag_step)

        self.retranslateUi(Dialog)
        self.tabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.hyphenate, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.hyphenate_default_lang.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.serif_family, self.sans_family)
        Dialog.setTabOrder(self.sans_family, self.mono_family)
        Dialog.setTabOrder(self.mono_family, self.max_fs_width)
        Dialog.setTabOrder(self.max_fs_width, self.opt_remember_window_size)
        Dialog.setTabOrder(self.opt_remember_window_size, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Configure Ebook viewer"))
        self.groupBox.setTitle(_("&Font options"))
        self.label.setText(_("Se&rif family:"))
        self.label_2.setText(_("&Sans family:"))
        self.label_3.setText(_("&Monospace family:"))
        self.label_4.setText(_("&Default font size:"))
        self.default_font_size.setSuffix(_(" px"))
        self.label_5.setText(_("Monospace &font size:"))
        self.mono_font_size.setSuffix(_(" px"))
        self.label_6.setText(_("S&tandard font:"))
        self.standard_font.setItemText(0, _("Serif"))
        self.standard_font.setItemText(1, _("Sans-serif"))
        self.standard_font.setItemText(2, _("Monospace"))
        self.hyphenate.setText(_("H&yphenate (break line in the middle of large words)"))
        self.hyphenate_default_lang.setToolTip(_("The default language to use for hyphenation rules. If the book does not specify a language, this will be used."))
        self.hyphenate_label.setText(_("Default &language for hyphenation:"))
        self.label_11.setText(_("Page flip &duration:"))
        self.opt_page_flip_duration.setSpecialValueText(_("disabled"))
        self.opt_page_flip_duration.setSuffix(_(" secs"))
        self.max_fs_width.setToolTip(_("Set the maximum width that the book\'s text and pictures will take when in fullscreen mode. This allows you to read the book text without it becoming too wide."))
        self.max_fs_width.setSuffix(_(" px"))
        self.label_7.setText(_("Maximum text width in &fullscreen:"))
        self.label_12.setText(_("Font &magnification step size:"))
        self.opt_font_mag_step.setToolTip(_("The amount by which the font size is increased/decreased\n"
" when you click the font size larger/smaller buttons"))
        self.opt_font_mag_step.setSuffix(_("%"))
        self.opt_fit_images.setText(_("&Resize images larger than the viewer window (needs restart)"))
        self.opt_remember_window_size.setText(_("Remember last used &window size and layout"))
        self.opt_wheel_flips_pages.setText(_("Mouse &wheel flips pages"))
        self.opt_remember_current_page.setText(_("Remember the &current page when quitting"))
        self.opt_line_scrolling_stops_on_pagebreaks.setText(_("Line &scrolling stops at page breaks"))
        self.opt_fullscreen_clock.setText(_("Show &clock in full screen mode"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), _("&General"))
        self.label_9.setText(_("Double click to change a keyboard shortcut"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), _("&Keyboard shortcuts"))
        self.label_10.setText(_("<p>A CSS stylesheet that can be used to control the look and feel of books. For examples, click <a href=\"http://www.mobileread.com/forums/showthread.php?t=51500\">here</a>."))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_3), _("User &Stylesheet"))


