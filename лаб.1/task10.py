# -*- coding: utf-8 -*-

arr = [1, 77, 153, 229, 305, 381, 457, 533, 609, 685, 761, 837, 913, 989]
step = arr[1] - arr[0]
if arr == range(arr[0], arr[-1] + step, step):
    print True
else:
    print False