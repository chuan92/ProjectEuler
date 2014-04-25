def fib(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for i in range(n - 2):
        a, b = a+b, a
    return a

i = 1
x = 10**999
while True:
    result = fib(i)
    if result >= x:
        print i
        break
    i = i + 1
