#ready
g = int(input())
s = input()
g_len = len(s) // g
res = ''
for i in range(g):
    x = s[i * g_len:(i + 1) * g_len]
    res += x[::-1]
print(res)