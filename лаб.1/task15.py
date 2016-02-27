# -*- coding: utf-8 -*-
import re

string = raw_input("Введите строку:\n");
res = re.findall(r'\b[A-Z][a-z]*\d{2}\b', string)
for r in res:
    print r