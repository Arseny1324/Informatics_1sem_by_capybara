def fanc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fanc(n - 1) + fanc(n - 2)

N = int(input("номер"))
print(f"{N}-е число фибоначчи: {fanc(N)}")