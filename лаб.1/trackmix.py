# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 23:07:23 2016

@author: Максим
"""

import subprocess

p = subprocess.check_output(['ffmpeg.exe', '-ss', '20', '-t', '25', '-i', u'Дигга.mp3'.encode("cp866").decode("utf-8"), '-acodec', 'copy', 'temp.mp3'])
print p