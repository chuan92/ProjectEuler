#!/usr/bin/python


dic = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
       6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
       11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
       15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
       19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
       60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 0: ""}

lenDic = dict(map(lambda x_y: (x_y[0], len(x_y[1])), dic.items()))


def numberLen(n):
    if n >= 1 and n <= 20:
        return lenDic[n]
    elif n > 20 and n < 100:
        return lenDic[n - n % 10] + lenDic[n % 10]
    elif n == 1000:
        return 11
    elif n % 100 == 0:
        return lenDic[n / 100] + 7
    elif n > 100 and n < 1000:
        if (n / 10) % 10 == 1:
            return lenDic[n / 100] + 10 + lenDic[n - (n/100)*100]
        else:
            return lenDic[n / 100] + 10 + lenDic[((n/10) % 10)*10] + lenDic[n % 10]
total = 0
for i in range(1, 1001):
    total = total + numberLen(i)
print total
