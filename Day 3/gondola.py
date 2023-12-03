import re
mat = open('input.txt', 'r').readlines()
tot = 0
is_symbol = lambda c : not (c.isdigit() or c=='.' or c=='\n')
for nrow, line in enumerate(mat):
    matches = re.finditer(r'\d+', line)
    for match in matches:
        for i in range(max(0, match.span()[0]-1), min(len(line), match.span()[1]+1)):
            above, on, below = mat[max(0, nrow-1)][i], line[i], mat[min(len(mat)-1, nrow+1)][i]
            if is_symbol(above) or is_symbol(on) or is_symbol(below):
                tot += int(match.group())
                break
print(tot)