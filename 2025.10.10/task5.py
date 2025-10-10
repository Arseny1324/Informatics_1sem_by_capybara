list = input().split()

list_=[]
for i in range(0, len(list)-1, 1):
    list_.append(list[i+1])
list_.append(list[0])
print(*list_)