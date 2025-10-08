def delits(n):
    list_del = []
    delit = 2
    while n > 1:
        while n % delit == 0:
            list_del.append(delit)
            n //= delit
        delit += 1
    return list_del


num = int(input())
result = delits(num)
print(result)