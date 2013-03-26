# find the first four consecutive integers
# with unique prime factors

from pe_utils import prime_sieve, factor_map
from itertools import count, repeat, takewhile

distinct_factors = 4

prime_gen = prime_sieve()
primes = [next(prime_gen)]

factor_dict = {}

def n_distinct_factors(n):
    global factor_dict, primes, prime_gen
    if n in factor_dict:
        return factor_dict[n]
    else:
        if n in primes:
            return 1
        while primes[-1] < n:
            primes.append(next(prime_gen))
        distincts = len(list(factor_map(n, takewhile(lambda x: x < n, primes), True)))
        factor_dict[n] = distincts
        return distincts


for i in count(1):
    consec_nums = map(lambda x: x[0] + x[1], enumerate(repeat(i, distinct_factors)))
    consec_facs = map(lambda x: n_distinct_factors(x) == distinct_factors, consec_nums)
    if all(consec_facs):
        print(i)
        break
