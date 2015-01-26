#!/usr/bin/python


if __name__ == '__main__':
    for c in range(1000, 0, -1):
        for b in range(c, 1, -1):
            if(b+c<1000 and b*b + (1000-c-b)*(1000-c-b) == c * c):
                print b*c*(1000-b-c)
                break
