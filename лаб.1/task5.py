# -*- coding: utf-8 -*-

for dvznch in range(10, 100):
    if ((dvznch / 10 + dvznch % 10) % 7 == 0):
        print dvznch

sevens = [d for d in range(10, 100) if ((d / 10 + d % 10) % 7 == 0)]
print sevens