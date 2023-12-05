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

def lookup_through(seed):
    num = seed
    for i in range(7):
        num = lookup(dicts[i], num)
    return num

dicts = [[], [], [], [], [], [], []]
curdict = -1

for line in open('input.txt', 'r').readlines():
    if re.match('seeds: ', line):
        seeds = [int(s) for s in re.findall(r'\d+', line)]
        continue
    if ':' in line:
        curdict += 1
        continue
    if row := re.findall(r'\d+', line):
        [dest, src, rng] = [int(s) for s in row]
        edit_range(dicts[curdict], dest, src, rng)

print(min([lookup_through(seed) for seed in seeds]))
