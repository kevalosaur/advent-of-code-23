import re
preformat = []

def distance(press, limit):
    return press * (limit - press)

for line in open('input.txt', 'r').readlines():
    preformat.append([int(n) for n in re.findall(r'\d+', line)])

races = list(zip(preformat[0], preformat[1]))

prod = 1
for race in races:
    ways = 0
    (limit, record) = race
    for i in range(limit+1):
        if distance(i, limit) > record:
            ways += 1
    prod *= ways

print(prod)