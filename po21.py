def d(n):
    sumn = 1
    for i in range(2, n):
        if n % i == 0:
            sumn = sumn + i
    return sumn

dicd = {}
for i in range(2, 10000):
    dicd[i] = d(i)

sumn = 0
for i in range(2, 10000):
    if dicd[i] != i and dicd.get(dicd[i]) == i:
        print i,dicd[i]
        sumn = sumn + dicd[i]

print sumn
