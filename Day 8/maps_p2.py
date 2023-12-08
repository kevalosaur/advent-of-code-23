from math import lcm
import re

lr = ('L', 'R')
directions = ''
nodes = dict()

for (i, line) in enumerate(open('input.txt', 'r').readlines()):
    if i == 0:
        directions = line.rstrip('\n')
    elif i == 1:
        continue
    else:
        match = re.match(r'(\w+) = \((\w+), (\w+)\)', line)
        nodes[match.group(1)] = (match.group(2), match.group(3))

locs = [l for l in nodes if re.match('..A', l)]
found = False
ret = 1

for loc in locs:
    steps = 0
    found = False
    while True:
        if found:
            ret = lcm(ret, steps)
            break
        for d in directions:
            if loc[2] == 'Z':
                found = True
                break
            loc = nodes[loc][lr.index(d)]
            steps += 1

print(ret)