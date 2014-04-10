#!/usr/bin/python
import math


def isPrime(n):
    if n == 2:
        return True
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        else:
            if i == 2:
                i = i + 1
            else:
                i = i + 2
    return True


def findNthPrime(n):
    if n == 1:
        return 2
    j = 1
    prime = test = 3
    # j < 1 is not right
    while(j < n):
        if(isPrime(test)):
            j = j + 1
            prime = test
        test = test + 2
    return prime


if __name__ == '__main__':
        print findNthPrime(10001)
