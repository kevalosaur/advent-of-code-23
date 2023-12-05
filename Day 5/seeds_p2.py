import re

seeds = []

def edit_range(range_dict, dest, src, rng):
    range_dict.append((dest, src, rng))

def lookup(range_dict, source):
    for item in range_dict:
        (dest, src, rng) = item
        if src <= source < src + rng:
            return dest + (source - src)
    else: return source

def lookup_back(range_dict, destination):
    for item in range_dict:
        (dest, src, rng) = item
        if dest <= destination < dest + rng:
            return src + (destination - dest)
    else: return destination

def lookup_through(seed):
    num = seed
    for i in range(7):
        num = lookup(dicts[i], num)
    return num

dicts = [[], [], [], [], [], [], []]
breakpoints = [set(), set(), set(), set(), set(), set(), set()]
curdict = -1

for line in open('input.txt', 'r').readlines():
    if re.match('seeds: ', line):
        nums = [int(s) for s in re.findall(r'\d+', line)]
        for i in range(0, len(nums), 2):
            seeds.append((nums[i], nums[i+1]))
        continue
    if ':' in line:
        curdict += 1
        continue
    if row := re.findall(r'\d+', line):
        [dest, src, rng] = [int(s) for s in row]
        edit_range(dicts[curdict], dest, src, rng)

for d in range(6, -1, -1):
    breakpoints[d].add(0)
    for item in dicts[d]:
        (dest, src, rng) = item
        breakpoints[d].add(src)
    if d < 6:
        for bp in breakpoints[d+1]:
            breakpoints[d].add(lookup_back(dicts[d], bp))

seed_closeness = dict()
for ps in breakpoints[0]:
    seed_closeness[ps] = float('inf')
    for (start, rng) in seeds:
        if start <= ps < start + rng:
            seed_closeness[ps] = 0
        elif start > ps:
            seed_closeness[ps] = min(seed_closeness[ps], start - ps)

print(min([lookup_through(s + seed_closeness[s]) for s in breakpoints[0]]))