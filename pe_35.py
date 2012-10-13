# Find number of circular primes below 1 million

from pe_utils import primes_to_n, primality_test
from math import log10
from functools import reduce

primes = set(list(primes_to_n(1000000)))
num_primes = len(primes)
circular_primes = set()

def all_rotations(n):
	yield n
	digits_m1 = int(log10(n))
	ten_e_digits = 10**digits_m1
	for i in range(digits_m1):
		n = n / 10 + n % 10 * ten_e_digits
		yield n

def rotation_is_prime(rotations):
	for rotation in rotations:
		if rotation not in primes:
			return False
	return True

for prime in primes:
	if prime not in circular_primes:
		rotations = list(all_rotations(prime))
		if rotation_is_prime(rotations):
			for rotation in rotations:
				circular_primes.add(rotation)

print(len(circular_primes))