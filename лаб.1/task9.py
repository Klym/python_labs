# -*- coding: utf-8 -*-
import random, math

N = random.randint(1, 1000)
arr = [random.randint(1, 50) for i in range(0, N)]
log = math.log(N, 2)
if log - int(log) != 0 or N < 2:
    count = int(math.pow(2, int(log) + 1)) - N
    arr += [0] * count
print N
print arr