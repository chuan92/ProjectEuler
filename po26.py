def reciprocal(n):
    while n % 2 == 0:
        n = n / 2
    while n % 5 == 0:
        n = n / 5
    if n == 1:
        return 0
    k = 1
    while (10**k - 1) % n != 0:
        k = k + 1
    return k


maxnum = 0
index = 1
for i in range(1, 1000):
    rec = reciprocal(i)
    if rec > maxnum:
        maxnum = rec
        index = i
print index, maxnum
