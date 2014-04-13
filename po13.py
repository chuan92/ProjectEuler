#!/usr/bin/python


def sum3(x, y, z):
    a = x + y + z
    return [a/10, a % 10]


def sumLargeXY(x, y):
    z = []
    xlength = len(x)
    ylength = len(y)
    a = c = 0
    for i in range(xlength):
        if i >= ylength:
            a = 0
        else:
            a = y[i]
        # c is carryout bit
        [c, a] = sum3(x[i], a, c)
        z.append(a)
    if c != 0:
        z.append(c)
    return z

if __name__ == '__main__':
    a = [0 for x in range(50)]
    for i in range(100):
        b = raw_input()
        b = map(int, list(b))
        b.reverse()
        a = sumLargeXY(a, b)
    a.reverse()
    print a[0:10]
