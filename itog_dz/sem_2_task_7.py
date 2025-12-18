#ready
x = list(map(int, input().split()))
max_ = 0
y = None
for el in set(x): 
    temp = x.count(el)
    if temp > max_:
        max_ = temp
        y = el
print(y)