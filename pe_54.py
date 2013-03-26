# How many poker hands does Player 1 win?

from collections import Counter

value_conv = {'2':1, '3':2, '4':3, '5':4,
              '6':5, '7':6, '8':7, '9':8,
              'T':9, 'J':10, 'Q':11,
              'K':12, 'A':13}

suit_conv = {'H':1, 'D':2, 'C':3, 'S':4}

DEBUG=False

def first(l):
    return l[0]

def second(l):
    return l[1]

def values(h):
    return list(map(first, h))

def suits(h):
    return list(map(second, h))

def all_equal(l):
    l = list(l)
    first = l[0]
    return all(map(lambda x: first == x, l))

def parse_hand(h):
    return sorted(map(lambda x: (value_conv[x[0]], suit_conv[x[1]]), h.split(' ')))

def rank_hand(h):
    """hands are ranked from 1 to 10
    high card to royal flush"""
    vs = values(h)
    ss = suits(h)

    flush = all_equal(ss)
    straight = all_equal(map(lambda ic: (ic[1] - ic[0]) % 13, enumerate(vs)))

    if flush and straight:
            # Royal Flush
            if vs[0] == value_conv['T']:
                if DEBUG: print('royal flush')
                return 10
            # Straight Flush
            if DEBUG: print('straight flush')
            return 9, vs[-1]

    c = Counter(map(first, h))
    most_common = c.most_common()

    # 4 of a kind
    if most_common[0][1] == 4:
        if DEBUG: print('4 of a kind')
        return 8, most_common[0][0]

    # full house
    if most_common[0][1] == 3 and most_common[1][1] == 2:
        if DEBUG: print('full house')
        return 7, most_common[0][0]

    # flush
    if flush:
        if DEBUG: print('flush')
        return 6, vs[::-1]

    # straight
    if straight:
        if DEBUG: print('straight')
        return 5, vs[-1]

    # 3 of a kind
    if most_common[0][1] == 3:
        if DEBUG: print('3 of a kind')
        return 4, most_common[0][0]

    if most_common[0][1] == 2:
        # 2 pair
        if most_common[1][1] == 2:
            if DEBUG: print('2 pair')
            pairs = sorted([most_common[0][0], most_common[1][0]], reverse=True)
            del most_common[0]
            del most_common[1]
            return 3, pairs + sorted(map(first, most_common), reverse=True)
        # 1 pair
        if DEBUG: print('1 pair')
        pair = most_common[0][0]
        del most_common[0]
        return 2, [pair] + sorted(map(first, most_common), reverse=True)

    # High card
    if DEBUG: print('high card')
    return 1, sorted(vs, reverse=True)

def compare_hands(h1, h2):
    """Takes two hands
    Returns 1 for h1 win, 0 for h1 loss"""
    return int(rank_hand(h1) > rank_hand(h2))

f = open('poker.txt', 'r')
hands = map(lambda txt: (parse_hand(txt[:14]), parse_hand(txt[15:-1])), f)
print("p1 wins:", sum(map(lambda hs: compare_hands(*hs), hands)))
