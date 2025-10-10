def delen(n, d=2):
    if n < 2:
        return []
    if n == 1:
        return []
    if n % d == 0:
        return [d] + delen(n // d, d)
    else:
        return delen(n, d + 1)

num = int(input("Введите натуральное число: "))
result = delen(num)
print(f"Простые множители числа {num}: {result}")