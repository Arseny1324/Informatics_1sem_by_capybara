#ready

import sys

def func(a, b):
    if a == 0:
        return 0, 1, b
    x1, y1, d = func(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return x, y, d

for line in sys.stdin:
    if line.strip():
        a, b = map(int, line.split())
        x, y, d = func(a, b)
        print(x, y, d)