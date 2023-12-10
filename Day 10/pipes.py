pipes = []
start = ()
dists = dict()

def choices(loc):
    height, width = len(pipes), len(pipes[0])
    symb = pipes[loc[0]][loc[1]]
    adj = []
    if symb == '|':
        if loc[0] > 0:
            adj.append((loc[0]-1, loc[1]))
        if loc[0] < height-1:
            adj.append((loc[0]+1, loc[1]))
    if symb == '-':
        if loc[1] > 0:
            adj.append((loc[0], loc[1]-1))
        if loc[1] < width-1:
            adj.append((loc[0], loc[1]+1))
    if symb == 'L':
        if loc[0] > 0:
            adj.append((loc[0]-1, loc[1]))
        if loc[1] < width-1:
            adj.append((loc[0], loc[1]+1))
    if symb == 'J':
        if loc[0] > 0:
            adj.append((loc[0]-1, loc[1]))
        if loc[1] > 0:
            adj.append((loc[0], loc[1]-1))
    if symb == '7':
        if loc[0] < height-1:
            adj.append((loc[0]+1, loc[1]))
        if loc[1] > 0:
            adj.append((loc[0], loc[1]-1))
    if symb == 'F':
        if loc[0] < height-1:
            adj.append((loc[0]+1, loc[1]))
        if loc[1] < width-1:
            adj.append((loc[0], loc[1]+1))
    if symb == 'S':
        if loc[0] > 0 and (pipes[loc[0]-1][loc[1]] in '|7F'):
            adj.append((loc[0]-1, loc[1]))
        if loc[0] < height-1 and (pipes[loc[0]+1][loc[1]] in '|LJ'):
            adj.append((loc[0]+1, loc[1]))
        if loc[1] > 0 and (pipes[loc[0]][loc[1]-1] in '-LF'):
            adj.append((loc[0], loc[1]-1))
        if loc[1] < width-1 and (pipes[loc[0]][loc[1]+1] in '-J7'):
            adj.append((loc[0], loc[1]+1))
    if symb == '.':
        return []
    return adj

for i, line in enumerate(open('input.txt', 'r').readlines()):
    pipes.append(line.rstrip('\n'))
    if 'S' in line:
        start = (i, line.index('S'))

bfsq = [start]
dists[start] = 0

while bfsq:
    curloc = bfsq.pop(0)
    for next in choices(curloc):
        if not (next in dists):
            dists[next] = dists[curloc]+1
            bfsq.append(next)

print(max(dists.values()))