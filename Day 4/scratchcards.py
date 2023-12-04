import math
import re

tot = 0
for l in open('input.txt', 'r').readlines():
    [win, have] = [set(re.findall(r'\d+', x)) for x in l[l.index(':')+2:].split(' | ')]
    tot += math.floor(pow(2, len(win.intersection(have))-1))
print(tot)