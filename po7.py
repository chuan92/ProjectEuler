#!/usr/bin/python
import math


def is_prime(n):
    # even number but not 2 is prime
    if n != 2 and n % 2 == 0:
        return False
    # number can be divided by odd number is prime
    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        else:
            i += 2
    return True


def find_nth_prime(n):
    if n == 1:
        return 2
    j = 1
    prime = test = 3
    # j < 1 is not right
    while(j < n):
        if(is_prime(test)):
            j = j + 1
            prime = test
        test = test + 2
    return prime


if __name__ == '__main__':
        print find_nth_prime(10001)
