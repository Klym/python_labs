# -*- coding: utf-8 -*-
try:
    price = float(raw_input("Введите цену: "))
    if (price < 0):
        raise ValueError("Цена не может быть отрицательной.")
except ValueError as e:
    print e
    exit()

rubs = int(price)
cops = int(price * 100 % 100)

print "%s руб. %s коп."% (rubs, cops)