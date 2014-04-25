def isLeap(n):
    if n % 400 == 0 or (n % 100 != 0 and n % 4 == 0):
        return True
    return False


def dayOfYear(n):
    if isLeap(n):
        return 366
    return 365

noLeap = [0, 31, 59, 90, 120, 151, 180, 212, 243, 273, 304, 334]
leap = [0, 31, 60, 91, 121, 152, 181, 213, 244, 274, 305, 335]

# sunday is zero!
# how many sundays in the first of month


def monthFirstSundays(n, isLeap):
    count = 0
    noLeap[0] = n
    leap[0] = n
    if isLeap:
        month = map(lambda x: (x + n) % 7, leap)
        for i in month:
            if i == 0:
                count = count + 1
        return count
    else:
        month = map(lambda x: (x + n) % 7, noLeap)
        for i in month:
            if i == 0:
                count = count + 1
        return count


def countSundays(n):
    sumSundays = 0
    firstDay = 1
    for i in range(1900, n):
        firstDay = (firstDay + dayOfYear(i)) % 7
        sumSundays = sumSundays + monthFirstSundays(firstDay, isLeap(i))
    return sumSundays

print countSundays(2000)
