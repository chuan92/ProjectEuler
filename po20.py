def factorial(n):
    mul = 1
    for i in range(1, n+1):
        mul = mul * i
    return mul

print sum(int(digit) for digit in str(factorial(100)))
