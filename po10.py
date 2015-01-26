#!/usr/bin/python
import math


def isPrime(m):
    if(m == 2):
        return True
    i = 2
    while i <= math.sqrt(m):
        if(m % i == 0):
            return False
        else:
            if(i == 2):
                i = i + 1
            else:
                i = i + 2
    return m

sum = 0
for i in range(2, 2000000):
    if(isPrime(i)):
        sum = sum + i
print sum
