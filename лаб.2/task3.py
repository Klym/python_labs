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
        self.openLogFile()
    
    def __del__(self):
        self.log.close()
    
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
        try:
            filesize = self.formatBytes(os.path.getsize(filename))
        except WindowsError:
            return
        self.fillList(filename)
        self.statusLabel.setText(u"Обработан файл " + filename);
        self.bytesCountLabel.setText(filesize + u" байт")
    
    def parseFile(self, filename):
        with open(filename, "rb") as f:
            buf = f.readlines()
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

    def writeFile(self):
        filename = QFileDialog.getSaveFileName(self, 'Write to file', '')
        filename = unicode(filename)
        try:
            with open(filename, "wt") as f:
                lines = self.readFromList()
                f.writelines(lines)
        except IOError:
            return
        self.statusLabel.setText(u"Сохранено: " + filename);
        filesize = self.formatBytes(os.path.getsize(filename))
        self.bytesCountLabel.setText(filesize + u" байт")

    def openLogFile(self):
        try:
            with open("script18.log", "rb") as log:    
                self.log = log
        except IOError:
            self.showDialogLogCreate()
            self.createLogFile()
    
    def createLogFile(self):
        self.log = open("script18.log", "wt")
    
    def writeLog(self):
        if self.log.closed:
            self.log = open("script18.log", "a")
        lines = self.readFromList()
        self.log.writelines(lines)
        self.statusLabel.setText(u"Данные сохранены в лог");
        self.log.close()
    
    def readFromList(self):
        buff = []
        model = self.ui.listView.model()
        for index in range(model.rowCount()):
            item = model.item(index).text() + '\n'
            buff.append(item.encode("utf-8"))
        return buff
    
    def readLog(self):
        model = self.ui.listView.model()
        try:
            count = model.rowCount()
            if count != 0:
                result = self.showDialogLogOpen()
                if result != 1:
                    return
                model.removeRows(0, count)
        except AttributeError:
            pass
        with open("script18.log", "rb") as log:
            lines = log.readlines()
            for line in lines:
                item = QStandardItem(line[:-1].decode("utf-8"))
                self.listModel.appendRow(item)
            self.ui.listView.setModel(self.listModel)
        filesize = self.formatBytes(os.path.getsize("script18.log"))
        self.statusLabel.setText(u"Открыт лог");
        self.bytesCountLabel.setText(filesize + u" байт")
                
    def showDialogLogCreate(self):
        dialog = QDialog()
        label = QLabel(dialog)
        label.setText(u"Файл лога не найден. Файл будет создан автоматически")
        label.move(5, 30)
        okBtn = QPushButton(u"Ок", dialog)
        okBtn.move(220, 70)
        dialog.connect(okBtn, SIGNAL('clicked()'), dialog.close)
        dialog.setFixedSize(QSize(300, 100))
        dialog.setWindowTitle(u"Создан файл лога")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()
        
    def showDialogLogOpen(self):
        dialog = QDialog()
        label = QLabel(dialog)
        label.setText(u"Вы действительно хотите открыть лог?\nДанные последних поисков будут потеряны!")
        label.move(35, 20)
        okBtn = QPushButton(u"Ок", dialog)
        okBtn.move(140, 70)
        cancelBtn = QPushButton(u"Отмена", dialog)
        cancelBtn.move(220, 70)
        dialog.connect(okBtn, SIGNAL('clicked()'), dialog.accept)
        dialog.connect(cancelBtn, SIGNAL('clicked()'), dialog.reject)
        dialog.setFixedSize(QSize(300, 100))
        dialog.setWindowTitle(u"Открыть лог?")
        dialog.setWindowModality(Qt.ApplicationModal)
        result = dialog.exec_()
        return result
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = StringFinderForm()
    form.show()    
    
    sys.exit(app.exec_())
