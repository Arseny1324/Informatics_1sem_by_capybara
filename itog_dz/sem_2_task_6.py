#ready
y = list(map(int, input().split()))
res = []
for x in y:
    if y.count(x) == 1:
        res.append(x)
print(*res)