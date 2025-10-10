nums = list(map(int, input().split()))

len_nums = len(nums)
z_nums = 1

for i in range(len_nums):
    z_nums = z_nums * nums[i]

ans = z_nums**(1/len_nums)
print(ans)