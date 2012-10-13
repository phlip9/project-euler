# Find the 10001 prime
from pe_utils import prime_sieve_n_primes

foo = list(prime_sieve_n_primes(10001))
print(foo[-1])
# 104743