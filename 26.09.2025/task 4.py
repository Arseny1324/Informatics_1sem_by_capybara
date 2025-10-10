count, el = input().split()

count = int(count)

for i in range(0, (count+1)//2+1):
    j = 0
    while j < i:
        print(el, end="")
        j+=1
    print()
for i in range((count+1)//2-1, 0, -1):
    j = 0
    while j < i:
        print(el, end="")
        j+=1
    print()
