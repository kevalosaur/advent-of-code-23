import re
mat = open('input.txt', 'r').readlines()
gears = {(i, j): [] for i in range(len(mat)) for j in range(len(mat[0]))}
tot = 0
is_gear = lambda c : c=='*'
for nrow, line in enumerate(mat):
    matches = re.finditer(r'\d+', line)
    for match in matches:
        for i in range(max(0, match.span()[0]-1), min(len(line), match.span()[1]+1)):
            above, below = max(0, nrow-1), min(len(mat)-1, nrow+1)
            if is_gear(mat[above][i]):
                gears[(above,i)] += [int(match.group())]
            if is_gear(mat[nrow][i]):
                gears[(nrow,i)] += [int(match.group())]
            if is_gear(mat[below][i]):
                gears[(below,i)] += [int(match.group())]

for g in gears.values():
    if len(g) == 2:
        tot += g[0]*g[1]

print(tot)