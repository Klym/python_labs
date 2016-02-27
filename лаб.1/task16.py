# -*- coding: utf-8 -*-
import re

f = open("d:\smbs.txt", "rb")
smbs = {}
string = f.read()
f.close()
for i in range(0, len(string)):
    if re.match("\w", string[i]):
        smbs[str.lower(string[i])] = smbs.get(str.lower(string[i]), 0) + 1
for ch in sorted(smbs, key = lambda x: smbs[x], reverse = True):
    print ch + ": " + str(smbs[ch])