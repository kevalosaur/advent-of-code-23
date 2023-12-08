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

steps = 0
loc = 'AAA'
found = False

while True:
    if found:
        break
    for d in directions:
        if loc == 'ZZZ':
            found = True
            break
        loc = nodes[loc][lr.index(d)]
        steps += 1

print(steps)