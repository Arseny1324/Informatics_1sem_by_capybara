list = input().split()

for i in range(0, len(list)-1, 2):
    list[i+1], list[i] = list[i], list[i+1]
print(*list)