def func(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = func(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

a, b = map(int, input().split())

d, x, y = func(a, b)

print(x, y, d)