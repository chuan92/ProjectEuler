#!/usr/bin/python


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


def smallestMultiple(start, end):
    res = 1
    for elem in range(start, end + 1):
        res = lcm(res, elem)
    return res

if __name__ == '__main__':
    print smallestMultiple(1, 20)
