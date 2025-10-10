a = int(input())
b = int(input())

NOD = b*a

while ((b % NOD != 0) or (a % NOD != 0)):
    NOD-=1
print(NOD)