#ready
mas = list(map(int, input().split()))
res = [mas[-1]] + mas[:-1]
print(*res)