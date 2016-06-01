# -*- coding: utf-8 -*-

import sys, threading, time

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from GUIDownload import Ui_Form

class DownloadThread(threading.Thread):

    def __init__(self, threadname, func):
        threading.Thread.__init__(self)
        self.daemon = True
        self.name = threadname
        self.percentage = 0
        self.updateFunc = func
        #self.finishFunc = func_finish
        
        
    """ thread main function """
    def run(self):
        while self.percentage <= 100:
            time.sleep(0.04)
            self.percentage += 1
            self.updateFunc()
        
        #self.finishFunc(self.name)

class DownloadForm(QWidget):
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.progressBar.setValue(0)
        self.ui.progressBar_2.setValue(0)
        self.ui.progressBar_3.setValue(0)
        
    def startDownload1(self):
        self.dthread1 = DownloadThread('1', self.updateProgressBar1)
        self.dthread1.start()
        
    def updateProgressBar1(self):
        self.ui.progressBar.setValue(self.dthread1.percentage)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DownloadForm()
    form.show()
    
    sys.exit(app.exec_())