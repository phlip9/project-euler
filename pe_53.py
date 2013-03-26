# How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are
# greater than one-million?

#from itertools import product
#from functools import reduce
from pe_utils import factorial

def comb(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

#inc_range = map(lambda x: ([x], list(range(1, x + 1))), range(23, 100 + 1))
#inc_range = reduce(lambda x,y: x + list(product(y[0], y[1])), inc_range, [])
#selections = filter(lambda x: x > 1000000, map(lambda x: combinatoric_selection(*x), inc_range))

ans = sum([1 if comb(n, r) > 1000000 else 0 for n in range(23, 100 + 1) for r in range(1, n + 1)])
print("Values over 1.000.000: ", ans)
