# -*- coding: utf-8 -*-
import math
N = int(raw_input("Введите натуральное число N: "))
predel = int(math.pow(N, 1.0 / 3)) + 1
found = False
for x in range(1, predel):
    for y in range(x, predel):
        for z in range(y, predel):
            if (x*x*x + y*y*y + z*z*z == N):
                found = True
                print "(%s,%s,%s)"%(x, y, z)
if (found == False):
    print "No such combinations!"