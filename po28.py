result = 1
for i in range(3, 1003, 2):
    result = result + i * i * 4 - 6 * (i - 1)

print result
