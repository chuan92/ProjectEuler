#!/usr/bin/python

# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindromic(n):
    nstr = str(n)
    for i in range(0, len(nstr)/2):
        if(nstr[i] != nstr[-i - 1]):
            return False
    return True

max_palindromic = 0
i = 999
while i >= 100:
    # i or j must be divisible by 11
    # if i is not divisible by 11, then j must be
    if(i % 11 == 0):
        j = 999
        jstep = 1
    else:
        j = 990
        jstep = 11
    while j >= i:
        if(i * j <= max_palindromic):
            break
        if(is_palindromic(i * j)):
            max_palindromic = i * j
        j = j - jstep
    i = i - 1
print max_palindromic
