# In the first one-thousand expansions of sqrt(2),
# how many fractions contain a numerator with more
# digits than denominator?

from fractions import Fraction
from functools import lru_cache

@lru_cache(maxsize=None)
def sqrt_exp(n):
    if n == 0:
        return Fraction(1)
    return 1 + 1 / (1 + sqrt_exp(n - 1))

expans = filter(lambda x: len(str(x.numerator)) > len(str(x.denominator)), map(sqrt_exp, range(1, 1000 + 1)))
print(len(list(expans)))
