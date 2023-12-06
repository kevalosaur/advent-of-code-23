import re

race = []

def distance(press, limit):
    return press * (limit - press)

for line in open('input.txt', 'r').readlines():
    race.append(int(''.join(re.findall(r'\d+', line))))
    
ways = 0
[limit, record] = race
for i in range(limit+1):
    if distance(i, limit) > record:
        ways += 1

print(ways)