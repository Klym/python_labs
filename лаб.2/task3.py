# -*- coding: utf-8 -*-
import sys, re, os
from datetime import datetime

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from GUIStringFinder import Ui_MainWindow

class StringFinderForm(QMainWindow):
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.listModel = QStandardItemModel(self)
        self.statusLabel = QLabel(u"Готово")
        self.bytesCountLabel = QLabel(u"0 байт")
        self.statusBar().addWidget(self.statusLabel, 3)
        self.statusBar().addWidget(self.bytesCountLabel, 1)
    
    def formatBytes(self, size):
        size = str(size)
        spaces = [i for i in range(len(size), 0, -3)]
        spaces.append(0)
        result = ""
        for sp in range(len(spaces) - 1, 0, -1):
            result += size[spaces[sp]:spaces[sp-1]] + " "
        return result
    
    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', '')
        filename = unicode(filename)
        filesize = self.formatBytes(os.path.getsize(filename))
        self.fillList(filename)
        self.statusLabel.setText(u"Обработан файл " + filename);
        self.bytesCountLabel.setText(filesize + u" байт")
    
    def parseFile(self, filename):
        f = open(filename, "rb")
        buf = f.readlines()
        f.close()
        result = []
        i = 1
        for line in buf:
            matches = re.findall(u"(?:int|short|byte)\s\w+\s=\s\d+", line)
            if matches:
                for match in matches:
                    result.append((i, line.index(match), match))
            i = i + 1
        return result
        
    def fillList(self, filename):
        result = self.parseFile(filename)
        now = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
        info = u"Файл " + filename + u" был обработан " + now + ":\n"
        self.listModel.appendRow(QStandardItem(info))
        for r in result:
            out = u"Строка %s, позиция %s : найдено «%s»" % r
            item = QStandardItem(out)
            self.listModel.appendRow(item)
        self.listModel.appendRow(QStandardItem(""))
        self.ui.listView.setModel(self.listModel)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = StringFinderForm()
    form.show()    
    
    sys.exit(app.exec_())
