# -*- coding: utf-8 -*-

link = raw_input("Введите ссылку:\n");
result = ""
if (link[:3] == "www"):
    result += "http://"
    result += link
    if (link[-4:] != ".com"):
        result += ".com"
    print result