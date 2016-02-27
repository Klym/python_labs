# -*- coding: utf-8 -*-
import re

f = open(u"d:/regex.txt", "rb")
buf = f.readlines()
f.close()
result = []
i = 1
for line in buf:
    matches = re.findall(u"(?:int|short|byte)\s\w+\s=\s\d+", line)
    if matches:
        for match in matches:            
            result.append((i, line.index(match), match))
    i = i + 1
for r in result:
    print u"Строка %s, позиция %s : найдено «%s»" % r