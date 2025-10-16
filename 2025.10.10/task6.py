list = input().split()

for i in range(len(list)):
    if list.count(list[i])==1:
        print(list[i], end=" ")
