n_str, b_str, c_str = input().split()
N = n_str
b = int(b_str)
c = int(c_str)

sum_proizv = 0
stepen = 0

for i in range(len(N) - 1, -1, -1):
    digit = int(N[i])
    sum_proizv += digit * (b ** stepen)
    stepen += 1

if sum_proizv == 0:
    result = '0'
else:
    result = ''
    while sum_proizv > 0:
        ost = sum_proizv % c
        result = str(ost) + result
        sum_proizv //= c

print(result)