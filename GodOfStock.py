def getR():
    n = int(input())
    k = n
    i = 0
    j = 2
    while(k > j):
        i += 2
        k -= j
        j += 1
    return n - i
print(getR())

