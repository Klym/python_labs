# -*- coding: utf-8 -*-
import os, hashlib

tree = os.walk(u"d:/test");
dupls = []
for dirs in tree:
    for fname in dirs[2]:
        f = open(dirs[0] + "\\" + fname, "rb")
        data = f.read()
        f.close()
        checksum = hashlib.md5(data).hexdigest()
        dupls.append((dirs[0] + "\\" + fname, checksum))

for d in dupls:
    if d in dupls:
        dupls.remove(d)
    group = [d2[0] for d2 in dupls if d[1] == d2[1]]
    dupls = [d2 for d2 in dupls if d2[0] not in group]
    if len(group) > 0:
        group.insert(0, d[0])
    for g in group:
        print g
    if len(group) > 0:
        print