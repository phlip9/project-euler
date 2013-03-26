# find the 12-digit number formed by concatenating a series of 3 4-digit
# numbers who are permutations of each other and are all prime

from itertools import permutations, dropwhile
from pe_utils import prime_sieve

prime_set = set(prime_sieve(10000))

def perm(n, inc):
    perm_set = set(map(lambda x: int("".join(x)), permutations(str(n))))
    perms = (n, n + inc, n + inc*2)
    if any(map(lambda x: x not in prime_set or x not in perm_set, perms)):
        return None
    else:
        return perms


primes = dropwhile(lambda x: x < 1000, prime_sieve(3333))
primes = filter(lambda x: x != None, map(lambda x: perm(x, 3330), primes))
primes = list(map(lambda x: x[0] * 10**8 + x[1] * 10**4 + x[2], primes))
print(primes)
