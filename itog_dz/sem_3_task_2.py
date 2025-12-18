#ready
num = int(input("Введите число: "))
x = []
y = 2
n = num

while y * y <= n:
    while n % y == 0:
        x.append(y)
        n //= y
    y += 1

if n > 1:
    x.append(n)

print(f"Простые множители числа {num}: {x}")