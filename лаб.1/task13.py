# -*- coding: utf-8 -*-
import re

string = raw_input("Введите строку:\n");
words = re.split('[,. -]', string)
words = [w for w in words if w != ""]
result_str = ""
i = 1
for word in words:
    start = string.index(word) + len(word)
    if (i != len(words)):
        end = string.index(words[i])
    else:
        end = len(string)
    result_str += word + "(" + str(i) + ")" + string[start:end]
    i = i + 1
print result_str