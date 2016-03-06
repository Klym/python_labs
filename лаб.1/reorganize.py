# -*- coding: utf-8 -*-
import sys, getopt, os, datetime

try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["source=", "days=", "size="]);
    if (len(opts) != 3):
        raise Exception("Invalid count of arguments")
except Exception as err:
    print str(err)
    sys.exit(2)

path, days, size = "", 0, 0
for key, val in opts:
    if key == "--source":
        path = val
    elif key == "--days":
        days = int(val)
    elif key == "--size":
        size = int(val)

isSmallExist = False
isArchiveExist = False
tree = os.walk(path)
for dirs in tree:
    for fname in dirs[2]:
        fileinfo = os.stat(path + "\\" + fname)
        lastModified = datetime.date.fromtimestamp(fileinfo.st_mtime)
        delta = datetime.date.today() - lastModified
        if delta.days > days:
            if isArchiveExist == False:
                os.mkdir(path + "\\Archive")
                isArchiveExist = True
            f = open(path + "\\" + fname, "rb")
            buf = f.read()
            f.close()
            newf = open(path + "\\Archive\\" + fname, "wb")
            newf.write(buf)
            newf.close()
        
        if fileinfo.st_size < size:
            if isSmallExist == False:
                os.mkdir(path + "\\Small")
                isSmallExist = True
            f = open(path + "\\" + fname, "rb")
            buf = f.read()
            f.close()
            newf = open(path + "\\Small\\" + fname, "wb")
            newf.write(buf)
            newf.close()
            #os.remove(path + "\\" + fname)