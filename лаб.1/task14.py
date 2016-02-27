# -*- coding: utf-8 -*-

string = raw_input("Введите строку:\n");
symbols = {}
for ch in string:
    if ch not in symbols:
        symbols[ch] = 1
    else:
        symbols[ch] += 1
for ch in symbols:
    if symbols[ch] == 1:
        print ch
