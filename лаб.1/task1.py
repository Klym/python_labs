# -*- coding: utf-8 -*-

years = int(raw_input("Введите возраст: "))
while (years > 100 or years <= 0):
    years = int(raw_input("Ошибка! Возраст должен быть от 1 до 100. Введите возраст: "))
ostatok = years % 10
if (years in range(11, 20)):
    print "%s лет"% years
elif ostatok in range(2,5):
    print "%s года"% years
elif ostatok == 1:
    print "%s год"% years
else:
    print "%s лет"% years