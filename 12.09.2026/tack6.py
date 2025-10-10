with open('input.txt', 'r') as file:
    nums_line = file.readline().strip()
    math = file.readline().strip()
    ss = int(file.readline().strip())

nums_b = nums_line.split()

decimal_numbers = []
for num_str in nums_b:
    decimal_num = 0
    power = 0
    for i in range(len(num_str) - 1, -1, -1):
        digit = int(num_str[i])
        decimal_num += digit * (ss ** power)
        power += 1
    decimal_numbers.append(decimal_num)

if math == '+':
    result_decimal = 0
    for num in decimal_numbers:
        result_decimal = result_decimal + num
elif math == '*':
    result_decimal = 1
    for num in decimal_numbers:
        result_decimal = result_decimal * num
elif math == '-':
    result_decimal = decimal_numbers[0]
    for i in range(1, len(decimal_numbers)):
        result_decimal = result_decimal - decimal_numbers[i]


if result_decimal == 0:
    result_b = '0'
elif result_decimal < 0:
    sign = '-'
    result_decimal = -result_decimal 
else:
    sign = ''


if result_decimal == 0:
    result_b = '0'
else:
    result_b = ''
    temp = result_decimal
    while temp > 0:
        remainder = temp % ss
        result_b = str(remainder) + result_b
        temp //= ss

result_b = sign + result_b

with open('output.txt', 'w') as f:
    f.write(result_b)