import re
tot = 0

def all_zero(lst):
    if lst:
        for x in lst:
            if x != 0:
                return False
        return True
    return False

def thingy(lst):
    if lst:
        return lst[0] - thingy(lst[1:])
    else:
        return 0

for line in open('input.txt', 'r').readlines():
    sequ = [int(d) for d in re.findall(r'-?\d+', line)]
    diffs = sequ
    firsts = []
    while not all_zero(diffs):
        firsts.append(diffs[0])
        diffs = [diffs[i+1]-diffs[i] for i in range(len(diffs)-1)]
    
    tot += thingy(firsts)

print(tot)