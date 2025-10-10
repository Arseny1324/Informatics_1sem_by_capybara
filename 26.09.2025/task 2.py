n = int(input())

delit  = 2

if n > 1:
    while delit <= n:
        if n % delit == 0:
            n = n / delit
            print(delit)
            delit = 2
        else:
            delit += 1
