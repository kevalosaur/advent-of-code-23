import re

pat1 = r'^\D*(\d).*(\d)\D*$'
pat2 = r'^\D*(\d)\D*$'

sumn = 0
for line in open('input.txt', 'r').readlines():
    m1 = re.match(pat1, line)
    m2 = re.match(pat2, line)
    if m1:
        sumn += 10 * int(m1.group(1)) + int(m1.group(2))
    elif m2:
        sumn += 10 * int(m2.group(1)) + int(m2.group(1))

print(sumn)