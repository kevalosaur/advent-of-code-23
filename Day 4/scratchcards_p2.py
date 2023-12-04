import re

tot = 0
lines = open('input.txt', 'r').readlines()
instances = [1]*len(lines)

for i, l in enumerate(lines):
    [win, have] = [set(re.findall(r'\d+', x)) for x in l[l.index(':')+2:].split(' | ')]
    wins = len(win.intersection(have))
    for j in range(min(i+1, len(lines)), min(i+wins+1, len(lines))):
        instances[j] += instances[i]
print(sum(instances))