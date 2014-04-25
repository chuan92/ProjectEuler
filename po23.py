def isAbundant(n):
    result = 0
    for i in range(1, n):
        if n % i == 0:
            result = result + i
    if result > n:
        return True
    else:
        return False


def findSum(seq, sum):
    i = 0
    j = len(seq) - 1
    while i <= j:
        if seq[i] + seq[j] == sum:
            return True
        elif seq[i] + seq[j] > sum:
            j = j - 1
        else:
            i = i + 1
    return False


abundant = []
for i in range(1, 28124):
    if isAbundant(i):
        abundant.append(i)
abundant.sort()

result = 0
for i in range(1, 28124):
    if not findSum(abundant, i):
        result = result + i
print result
