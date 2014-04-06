#!/usr/bin/python


def gcd(a, b):
    while b != 0:
        tmp = a
        a = b
        b = tmp % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


def smallestMultiple(n):
    if n == 2:
        return 2
    else:
        return lcm(smallestMultiple(n-1), n)

input_number = input()
print smallestMultiple(input_number)
