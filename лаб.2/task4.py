# -*- coding: utf-8 -*-
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from StringFormatter import StringFormatter
from GUIStringFormatter import Ui_Form

class StringFormatterForm(QWidget):
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
    def enableSorting(self):
        if self.ui.checkBox_4.isChecked():
            self.ui.radioButton.setEnabled(True)
            self.ui.radioButton_2.setEnabled(True)
        else:
            self.ui.radioButton.setEnabled(False)
            self.ui.radioButton_2.setEnabled(False)
            
    def formatString(self):
        formatter = StringFormatter(unicode(self.ui.lineEdit_2.text()))
        if self.ui.checkBox.isChecked():
            formatter.delSmallWords(int(self.ui.spinBox.text()))
        if self.ui.checkBox_4.isChecked():
            if self.ui.radioButton.isChecked():
                formatter.sortWordsBySize()
            else:
                formatter.sortWordsLexicographically()
        if self.ui.checkBox_2.isChecked():
            formatter.replaceDigits()
        if self.ui.checkBox_3.isChecked():
            formatter.insertSpaces()

        self.ui.lineEdit.setText(formatter.getString())
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = StringFormatterForm()
    form.show()
    
    sys.exit(app.exec_())