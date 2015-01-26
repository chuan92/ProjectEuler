#!/usr/bin/python


def largestProduct(a):
    max = 0
    for i in range(len(a) - 4):
        tmp = reduce(lambda x, y: x*y, a[i:i+5])
        if tmp > max:
            max = tmp
    return max

if __name__ == '__main__':
    a = raw_input()
    a = map(int, tuple(a))
    print largestProduct(a)
