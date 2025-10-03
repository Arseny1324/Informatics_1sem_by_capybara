n = int(input())

sum_ideal = (2+(n-1))*n/2
sum = 0
while n > 1:
    n -= 1
    sum += int(input())
print(int(sum_ideal-sum))
