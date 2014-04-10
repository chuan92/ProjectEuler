#!/usr/bin/python
import math


def findPrimeFactors(m):
    factor = {}
    i = 2
    while i <= math.sqrt(m):
        if(m % i == 0):
            m = m / i
            if i in factor:
                factor[i] = factor[i]+1
            else:
                factor[i] = 1
        else:
            if(i == 2):
                i = i + 1
            else:
                i = i + 2
    factor[m] = 1
    if 1 in factor:
        del factor[1]
    return factor


def findFactors(n):
    primeFactor = findPrimeFactors(n)
    return reduce(lambda x, y: x*y, map(lambda x: x+1, primeFactor.values()))

i = 7
while True:
    n = i*(i+1)/2
    if(i % 2 == 0):
        m = findFactors(i / 2) * findFactors(i + 1)
    else:
        m = findFactors(i) * findFactors((i + 1)/2)
    if m > 500:
        print n
        break
    i = i + 1
