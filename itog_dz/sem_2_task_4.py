#ready
x = list(map(int, input().split()))

for i in range(0, len(x) - 1, 2):
    x[i], x[i + 1] = x[i + 1], x[i]

for i in range(len(x)):
    if i < len(x) - 1:
        print(x[i], end=' ')
    else:
        print(x[i])