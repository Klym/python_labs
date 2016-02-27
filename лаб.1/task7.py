# -*- coding: utf-8 -*-

num = raw_input("Введите номер карты:\n")
while (len(num) != 16):
    num = raw_input("Ошибка! Введите номер карты:\n")
result = num[:4] + " " + "*" * 4 + " " + "*" * 4 + " " + num[-4:]
print result