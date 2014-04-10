#!/usr/bin/python


def sumSquare(n):
    res = 0
    for i in range(1, n + 1):
        res = res + i * i
    return res


def squareSum(n):
    res = 0
    for i in range(1, n + 1):
        res = res + i
    return res * res


if __name__ == '__main__':
    print squareSum(100)-sumSquare(100)
