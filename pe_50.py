# find the greatest prime under 1000000 that is the sum of consecutive primes

from pe_utils import prime_sieve
from itertools import takewhile

max_sum = 1000000
primes = list(prime_sieve(max_sum))
num_primes = len(primes)

sums = list(takewhile(lambda x: x < max_sum, (sum(primes[:x]) for x in range(num_primes))))
num_sums = len(sums)

max_len = 0
def sum_and_bump(i, j):
    global max_len
    max_len = j - i
    return sums[j] - sums[i]

print(max([sum_and_bump(i, j) for i in range(num_sums) for j in range(i + 1 + max_len, num_sums) if j - i > max_len]))

# 997661
# 0.37 ms
# 2.40 GHz CPU
