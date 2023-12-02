from re import search

tot = 0
for l in open('input.txt', 'r').readlines():
    trimmed = l[l.index(':')+1:].replace(' ', '').split(';')
    minr, ming, minb = 0, 0, 0
    for t in trimmed:
        mr, mg, mb = search(r'(\d+)red', t), search(r'(\d+)green', t), search(r'(\d+)blue', t)
        r, g, b = (int(mr.group(1)) if mr else 0, int(mg.group(1)) if mg else 0, int(mb.group(1)) if mb else 0)
        minr, ming, minb = max(minr, r), max(ming, g), max(minb, b)
    tot += minr*ming*minb

print(tot)