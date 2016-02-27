# -*- coding: utf-8 -*-
N = int(raw_input("Введите количество слогаемых: "))
sign = 1;
res = 0
for i in range(1, N * 2 + 1, 2):
    res += sign * 1.0 / i
    sign = -sign
pi = res * 4
print pi