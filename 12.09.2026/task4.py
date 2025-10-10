with open('input.txt', 'r') as file:
    nums_read = file.readline().strip()
    math = file.readline().strip()

nums = list(map(int, nums_read.split()))

if math == '+':
    ans = 0
    for i in range(0, len(nums)):
        ans = ans + nums[i]
elif math == '/':
    ans = nums[0]
    for i in range(0, len(nums)):
        ans = ans / nums[i]
elif math == '*':
    ans = 1
    for i in range(0, len(nums)):
        ans = ans * nums[i]   

with open('output.txt', 'w') as file:
    file.write(str(ans))