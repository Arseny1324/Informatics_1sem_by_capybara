#ready
s = input().strip()
x = {'A':'A','H':'H','I':'I','M':'M','O':'O','T':'T','U':'U','V':'V','W':'W','X':'X','Y':'Y','1':'1','8':'8','E':'3','3':'E','J':'L','L':'J','S':'2','2':'S','Z':'5','5':'Z'}
m = s == s[::-1]
n = all(c in x and x[c] == s[-i-1] for i, c in enumerate(s))
if m and n:
    print(f"{s} is a mirrored palindrome.")
elif m:
    print(f"{s} is a regular palindrome.")
elif n:
    print(f"{s} is a mirrored string.")
else:
    print(f"{s} is not a palindrome.")