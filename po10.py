#!/usr/bin/python
import math


def is_prime(m):
    # even number but not 2 is prime
    if m != 2 and m % 2 == 0:
        return False
    # number can be divided by odd number is prime
    i = 3
    while i <= math.sqrt(m):
        if m % i == 0:
            return False
        else:
            i += 2
    return True

sum = 0
for i in range(2, 2000000):
    if(is_prime(i)):
        sum = sum + i
print sum
