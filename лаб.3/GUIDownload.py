# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIDownload.ui'
#
# Created: Thu Jun 02 01:00:58 2016
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(524, 426)
        Form.setMinimumSize(QtCore.QSize(524, 426))
        Form.setMaximumSize(QtCore.QSize(524, 426))
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(20, 70, 491, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar_2 = QtGui.QProgressBar(Form)
        self.progressBar_2.setGeometry(QtCore.QRect(20, 190, 491, 31))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.progressBar_3 = QtGui.QProgressBar(Form)
        self.progressBar_3.setGeometry(QtCore.QRect(20, 310, 491, 31))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName(_fromUtf8("progressBar_3"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 451, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 160, 451, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 280, 451, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 370, 481, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.startDownload)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Загрузка файлов", None))
        self.pushButton.setText(_translate("Form", "Загрузить", None))
        self.label.setText(_translate("Form", "URL 1:", None))
        self.label_2.setText(_translate("Form", "URL 2:", None))
        self.label_3.setText(_translate("Form", "URL 3:", None))

