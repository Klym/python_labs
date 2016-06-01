# -*- coding: utf-8 -*-

import sys, requests

import matplotlib.pyplot as plt

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
            self.finish_func(local_filename, self.getPercents(0))
    
    def getPercents(self, downloaded):
        r = requests.head(self.url, headers={'Accept-Encoding': 'identity'})
        filesize = int(r.headers['content-length'])
        self.percentage = downloaded * 100 / filesize
        return filesize

class DownloadForm(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.progressBar.setValue(0)
        self.ui.progressBar_2.setValue(0)
        self.ui.progressBar_3.setValue(0)
        self.files = []
        self.connect(self, SIGNAL('filesDownloaded'), self.showResults)

    def downloaded(self, name, size):
        name = name + '\n[' + str(round((float(size) / (1024 * 1024)), 1)) + 'mb]'
        self.files.append((name, size))
        self.emitSignal()
        
    def emitSignal(self):
        if len(self.files) == 3:
            self.ui.pushButton.setEnabled(True)
            self.emit(SIGNAL('filesDownloaded'), "downloaded")
    
    def showResults(self):
        data = [self.files[0][1], self.files[1][1], self.files[2][1]]
        plt.figure(num=1, figsize=(6, 6))
        plt.axes(aspect=1)
        plt.title('File size', size=14)
        plt.pie(data, labels=(self.files[0][0], self.files[1][0], self.files[2][0]))
        plt.show()
    
    def startDownload(self):
        self.dthread1 = DownloadThread('1', self.ui.lineEdit.text(), self.downloaded)
        self.dthread1.tick.connect(self.ui.progressBar.setValue)
        self.dthread1.start()

        self.dthread2 = DownloadThread('2', self.ui.lineEdit_2.text(), self.downloaded)
        self.dthread2.tick.connect(self.ui.progressBar_2.setValue)
        self.dthread2.start()
        
        self.dthread3 = DownloadThread('3', self.ui.lineEdit_3.text(), self.downloaded)
        self.dthread3.tick.connect(self.ui.progressBar_3.setValue)
        self.dthread3.start()        
        
        self.ui.pushButton.setDisabled(True)
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DownloadForm()
    form.show()
    
    sys.exit(app.exec_())