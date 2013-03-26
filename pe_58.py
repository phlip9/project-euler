# what is the side length of the square spiral for which the ratio of primes
# along both diagonals first falls below 10%?

from pe_utils import primality_test
from itertools import count

side_length = lambda x: 2 * x + 1               # 2n + 1
bottom_right = lambda x: 4 * x * x + 4 * x + 1  # 4n^2 + 4n + 1
n_diagonal = lambda x: 4 * x + 1                # 4n + 1

diagonal = (bottom_right(n) + (side_length(n + 1) - 1) * i for n in count(0) for i in range(1, 4 + 1))

for i in range(4):
    next(diagonal)

primes = 3
n = 1
while primes / n_diagonal(n) > 0.10:
    n += 1
    for i in range(3):
        if primality_test(next(diagonal)):
            primes += 1
    next(diagonal)

print("side length:", side_length(n))
