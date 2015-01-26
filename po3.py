#!/usr/bin/python
import math

# The prime factors of 13195 are 5, 7, 13 and 29.conjugate
# What is the largest prime factor of the number 600851475143 ?


def max_prime_factor(m):
    i = 2
    while i <= math.sqrt(m):
        if(m % i == 0 and m != i):
            m = m / i
        else:
            if(i == 2):
                i = i + 1
            else:
                i = i + 2
    return m

input_number = input()
print max_prime_factor(input_number)
