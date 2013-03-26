# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.

from itertools import count

max_multiples = 6

for e in count(1):
    for i in range(10**(e - 1), 10**e // 6 + 1):
        base = sorted(str(i))
        mults = [i * mult for mult in range(2, max_multiples + 1)]
        mults = map(lambda x: sorted(str(x)) == base, mults)
        if all(mults):
            print(i)
            exit()

# 142857
