import csv

# calc the score of string s
def score(s):
    s = list(s)
    s = map(lambda x:1 + ord(x) - ord('A'), s)
    return sum(s)

# read
namefile = file('names.txt', 'rb')
reader = csv.reader(namefile)
for row in reader:
    names = row
names.sort()


sumn = 0
for i in range(len(names)):
    sumn = sumn + (i + 1) * score(names[i])

print sumn
