#ready
n = int(input("Введите N: "))
a, b = 0, 1

for i in range(n):
    a, b = b, a + b

print(f"{n}-ое число Фибоначчи: {a}")