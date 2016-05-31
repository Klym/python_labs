# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIStringFormatter.ui'
#
# Created: Tue May 31 13:34:00 2016
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
        Form.setEnabled(True)
        Form.resize(457, 308)
        Form.setMinimumSize(QtCore.QSize(457, 308))
        Form.setMaximumSize(QtCore.QSize(457, 308))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 30, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(80, 70, 191, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.spinBox = QtGui.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(280, 70, 61, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 70, 51, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.checkBox_2 = QtGui.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(80, 90, 161, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(80, 110, 231, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(80, 130, 181, 17))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.radioButton = QtGui.QRadioButton(Form)
        self.radioButton.setEnabled(False)
        self.radioButton.setGeometry(QtCore.QRect(100, 160, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Form)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QtCore.QRect(100, 180, 121, 16))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 210, 361, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 270, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 270, 361, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 30, 361, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.checkBox_4, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), Form.enableSorting)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.formatString)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Форматирование строк", None))
        self.label.setText(_translate("Form", "Строка:", None))
        self.checkBox.setText(_translate("Form", "Удалить слова размером меньше", None))
        self.label_2.setText(_translate("Form", "букв", None))
        self.checkBox_2.setText(_translate("Form", "Заменить все цифры на *", None))
        self.checkBox_3.setText(_translate("Form", "Вставить по пробелу между символами", None))
        self.checkBox_4.setText(_translate("Form", "Сортировать слова в строке", None))
        self.radioButton.setText(_translate("Form", "по размеру", None))
        self.radioButton_2.setText(_translate("Form", "лексикографически", None))
        self.pushButton.setText(_translate("Form", "Форматировать", None))
        self.label_3.setText(_translate("Form", "Результат:", None))

