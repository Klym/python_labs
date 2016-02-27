# -*- coding: utf-8 -*-
import math

def sum_cubes(N):
    digits = []
    predel = int(math.pow(N, 1.0 / 3)) + 1
    for x in range(1, predel):
        for y in range(x, predel):
            for z in range(y, predel):
                if (x*x*x + y*y*y + z*z*z == N):
                    digits.append([x,y,z])
    return digits

cubes = {N: sum_cubes(N) for N in range(1, 100001) if len(sum_cubes(N)) >= 3}
for cub in cubes:
    res = "{0} : ".format(cub)
    for cmb in cubes[cub]:
        res += "({0},{1},{2}); ".format(cmb[0], cmb[1], cmb[2])
    print res