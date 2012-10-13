# Find the largest prime factor of 600 851 475 143

from pe_utils import factors
from functools import reduce

print(reduce(lambda x,y: max(x, y), factors(600851475143)))

# 6857