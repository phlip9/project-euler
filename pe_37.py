# Find the sum of all 11 primes that are truncatable from right to left and left to right

from pe_utils import prime_sieve
from math import log10
# from itertools import izip

truncatables = []

primes = set(list(prime_sieve(1000000)))

valid_least_sig = set([3, 7])
valid_most_sig = set([2, 3, 5, 7])
# valid_middle = set([1, 3, 7, 9])

def rtl_gen(n):
	for i in range(int(log10(n))):
		n /= 10
		yield n

def ltr_gen(n):
	for i in range(int(log10(n)), 0, -1):
		n %= 10**i
		yield n

for prime in primes:
	if prime > 7 and prime % 10 in valid_least_sig and prime / 10**(int(log10(prime))) in  valid_most_sig:
		truncatable = True
		for rtl in rtl_gen(prime):
			if rtl not in primes:
				truncatable = False
				break
		if truncatable:
			for ltr in ltr_gen(prime):
				if ltr not in primes:
					truncatable = False
					break
			if truncatable:
				truncatables.append(prime)

print(truncatables)
print(sum(truncatables))
print(len(truncatables))

# 748317