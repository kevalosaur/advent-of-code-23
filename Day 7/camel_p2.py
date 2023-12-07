import re
from collections import Counter

digits = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
base = len(digits)

def score(hand):
    score = sum(digits.index(c) * (base ** (len(hand)-i-1)) for (i, c) in enumerate(hand))
    mode = 'J'
    for entry in Counter(hand).most_common():
        if entry[0] != 'J':
            mode = entry[0]
            break
    nojokers = re.sub('J', mode, hand)

    type = 0
    match len(set(nojokers)):
        case 1:
            type = 6    # five of a kind
        case 2:
            if 2 <= len(re.findall(nojokers[0], nojokers)) <= 3:
                type = 4    # full house
            else:
                type = 5    # four of a kind
        case 3:
            for c in nojokers:
                count = len(re.findall(c, nojokers))
                if count == 2:
                    type = 2    # two pair
                    break
                elif count == 3:
                    type = 3    # three of a kind
                    break
        case 4:
            type = 1    # one pair
        case 5:
            type = 0    # high card

    score += type * (base ** len(hand))
    return score

bids = []
for line in open('input.txt', 'r').readlines():
    [hand, bid] = line.split()
    bids.append((hand, int(bid)))

tot = 0
for (i, (hand, bid)) in (lst := list(enumerate(sorted(bids, key=lambda b : score(b[0]))))):
    tot += (i+1) * bid

print(tot)