import re
tot = 0

def all_zero(lst):
    if lst:
        for x in lst:
            if x != 0:
                return False
        return True
    return False

for line in open('input.txt', 'r').readlines():
    sequ = [int(d) for d in re.findall(r'-?\d+', line)]
    diffs = sequ
    sumlast = 0
    while not all_zero(diffs):
        sumlast += diffs[-1]
        diffs = [diffs[i+1]-diffs[i] for i in range(len(diffs)-1)]
    tot += sumlast

print(tot)