list = input().split()

maks = 0
maks_temp = 0 

for i in range(len(list)):
    el = list[i]
    for j in range(i, len(list)):
        if el == list[j]:
            maks_temp += 1
    if maks_temp > maks:
        maks = maks_temp
    maks_temp=0
print(maks)
