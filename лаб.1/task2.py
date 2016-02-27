# -*- coding: utf-8 -*-

day = int(raw_input("Введите день: "))
while (day < 0 or day > 31):
    day = int(raw_input("Ошибка! Введите день: "))

month = int(raw_input("Введите месяц: "))
while (month < 0 or month > 12):
    month = int(raw_input("Ошибка! Введите месяц: "))

year = int(raw_input("Введите год: "))
while (year < 0):
    year = int(raw_input("Ошибка! Введите год: "))
    
res = ""
if (day in range(1,10)):
    res += "0"
res += day.__str__() + "/"
if (month in range(1,10)):
    res += "0"
res += month.__str__() + "/"
res += year.__str__()
print res