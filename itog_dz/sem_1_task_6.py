#ready
with open('input.txt', 'r') as file:
    nums = file.readline().strip()
    znak = file.readline().strip()
    ss = int(file.readline().strip())

nums_b = nums.split()

mas = []
for num_str in nums_b:
    decyt = 0
    sum = 0
    for i in range(len(num_str) - 1, -1, -1):
        digit = int(num_str[i])
        desyt += digit * (ss ** sum)
        sum += 1
    mas.append(desyt)

if znak == '+':
    desyt_res = 0
    for num in mas:
        desyt_res = desyt_res + num
elif znak == '*':
    desyt_res = 1
    for num in mas:
        desyt_res = desyt_res * num
elif znak == '-':
    desyt_res = mas[0]
    for i in range(1, len(mas)):
        desyt_res = desyt_res - mas[i]


if desyt_res == 0:
    res_ = '0'
elif desyt_res < 0:
    sign = '-'
    desyt_res = -desyt_res 
else:
    sign = ''


if desyt_res == 0:
    res_ = '0'
else:
    res_ = ''
    temp = desyt_res
    while temp > 0:
        y = temp % ss
        res_ = str(y) + res_
        temp //= ss

res_ = sign + res_

with open('output.txt', 'w') as f:
    f.write(res_)