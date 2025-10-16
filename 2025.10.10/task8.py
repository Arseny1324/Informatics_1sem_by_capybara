n = int(input())
listik = list(map(int, input().split()))

count = 0

for i in range(len(listik)):
    for j in range(len(listik)):
        if listik[i] > listik[j]:
            count+=1
    if count == (len(listik)-1)//2:
        print(listik[i])
        break
    count = 0
  