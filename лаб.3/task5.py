# -*- coding: utf-8 -*-

import sys, requests

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from GUIDownload import Ui_Form

class DownloadThread(QThread):

    tick = pyqtSignal(int, name="changed")

    def __init__(self, threadname, url, finish_func):
        QThread.__init__(self)
        self.name = threadname
        self.url = url
        self.percentage = 0
        self.finish_func = finish_func
        
    #def run(self):
    #    while self.percentage <= 100:
    #        time.sleep(0.04)
    #        self.percentage += 1
    #        self.tick.emit(self.percentage)
    #    self.finish_func()
        
    def run(self):
        local_filename = self.url.split('/')[-1]        
        r = requests.get(self.url, stream = True)
        with open(local_filename, 'wb') as f:
            i = 0
            for chunk in r.iter_content(chunk_size = 4096):
                if chunk:
                    i += 1
                    self.getPercents(i * 4096)
                    f.write(chunk)
                    self.tick.emit(self.percentage)
            self.finish_func()
    
    def getPercents(self, downloaded):
        r = requests.head(self.url, headers={'Accept-Encoding': 'identity'})
        filesize = int(r.headers['content-length'])
        self.percentage = downloaded * 100 / filesize

class DownloadForm(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.progressBar.setValue(0)
        self.ui.progressBar_2.setValue(0)
        self.ui.progressBar_3.setValue(0)

    def enableButton1(self):
        self.ui.pushButton.setEnabled(True)

    def enableButton2(self):
        self.ui.pushButton_2.setEnabled(True)
        
    def enableButton3(self):
        self.ui.pushButton_3.setEnabled(True)
    
    def startDownload1(self):
        self.dthread1 = DownloadThread('1', self.ui.lineEdit.text(), self.enableButton1)
        self.dthread1.tick.connect(self.ui.progressBar.setValue)
        self.dthread1.start()
        self.ui.pushButton.setDisabled(True)
        
    def startDownload2(self):
        self.dthread2 = DownloadThread('2', self.ui.lineEdit_2.text(), self.enableButton2)
        self.dthread2.tick.connect(self.ui.progressBar_2.setValue)
        self.dthread2.start()
        self.ui.pushButton_2.setDisabled(True)
    
    def startDownload3(self):
        self.dthread3 = DownloadThread('3', self.ui.lineEdit_3.text(), self.enableButton3)
        self.dthread3.tick.connect(self.ui.progressBar_3.setValue)
        self.dthread3.start()
        self.ui.pushButton_3.setDisabled(True)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DownloadForm()
    form.show()
    
    sys.exit(app.exec_())