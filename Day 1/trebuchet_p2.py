from re import match

digitcheck = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def concat_digits(n1, n2):
    return 10*digitcheck[n1] + digitcheck[n2]

anyd = r'|'.join([r'\d', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])

pat1 = (f'^.*?({anyd}).*({anyd})(?!{anyd}).*$')
pat2 = f'^.*?({anyd})(?!{anyd}).*$'

sumn = 0
for line in open('input.txt', 'r').readlines():
    m1 = match(pat1, line)
    m2 = match(pat2, line)
    if m1:
        sumn += concat_digits(m1.group(1), m1.group(2))
    elif m2:
        sumn += concat_digits(m2.group(1), m2.group(1))

print(sumn)