from math import sqrt, ceil
from itertools import compress, islice, count, cycle
from collections import defaultdict
from functools import reduce
from operator import mul
from random import randrange

def palindromic(x):
	return str(x) == str(x)[::-1]

# approximate fibonacci
def fib(n):
	return int(((((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n)/sqrt(5)))

def lucas(n):
	return int(((1 + sqrt(5)) / 2)**n) + (n % 2 == 0)

# Generate fibonacci numbers up to n, or if n is None, then to infinity
def fibonacci_generator(n=None):
	a, b, c = 0, 1, 0

	while n == None or c < n:
		yield a
		a, b, c = b, a + b, c + 1

def pythag_triple(a, b, c):
	return ((a*a + b*b) == (c*c))

def triangle_num(n):
	return n*(n+1)/2

# All prime numbers mod 30 result in a number in the set
# 1, 7, 11, 13, 17, 19, 23, 29
# except for 2, 3, and 5
def prime_sieve(n=None):
	IT_MASK= (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0)
	MODULOS= frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )
	D = {9:3, 25:5}
	
	#don't ask for anything below 5
	yield 2
	yield 3
	yield 5
	
	for i in compress(islice(count(7), 0, None, 2), cycle(IT_MASK)):
		if n == None or i < n:
			j = D.pop(i, None)
			if j is None:
				D[i*i] = i
				yield i
			else:
				k = i + 2*j
				while k in D or (k % 30) not in MODULOS:
					k += 2*j
				D[k] = j
		else:
			break

def composites(n, lower=4):
	return set(list(range(lower, n))).difference(set(list(primes_to_n(n, lower))))

def primes_to_n(n, lower=1):
	for p in prime_sieve():
		if p <= n:
			if p > lower:
				yield p
		else:
			break

# Miller-Rabin primality test
def primality_test(n):
	def test_pass(a, s, d, n):
		a_pow = pow(a, d, n)
		if a_pow == 1:
			return True
		for i in range(s - 1):
			if a_pow == n - 1:
				return True
			a_pow = a_pow * a_pow % n
		return a_pow == n - 1

	if n % 2 == 0 and n != 2:
		return False
	d = n - 1
	s = 0
	while d % 2 == 0:
		d >>= 1
		s += 1
	for repeat in range(20):
		a = 0
		while a == 0:
			a = randrange(n)
		if not test_pass(a, s, d, n):
			return False
	return True

def factors(x):
	i = 2
	limit = x**0.5
	while i <= limit:
		if x % i == 0:
			yield i
			x = x / i
		else:
			i += 1
	if x > 1:
		yield int(x)

def factor_map(x):
	for prime in prime_sieve():
		if prime > x:
			break
		exponent = 0
		while x % prime == 0:
			exponent, x = exponent + 1, x / prime
		if exponent != 0:
			yield prime, exponent

# total count of numbers coprime to n
def totient(n):
	return reduce(mul, ((p-1) * p ** (exp-1) for p, exp in factor_map(n)), 1)

def cartesian_product(set_1, set_2):
	return [x*y for x in set_1 for y in set_2]

def map_occurances(nums):
	intmap = defaultdict(int)
	for i in nums:
		intmap[i] += 1
	return intmap

# tau = number of divisors of n
def tau(x):
	facs = list(factors(x))
	intmap = map_occurances(facs)

	t = 1
	for i in intmap.values():
		t *= i + 1

	return t

def factor_dict(x):
	facs = factors(x)
	fac_dict = defaultdict(int)
	for fac in facs:
		fac_dict[fac] += 1
	return fac_dict

def divisors(x):
	facs_list = list(factors(x))
	facs_set = list(set(facs_list))
	len_facs = len(facs_set)

	def rec_gen(n = 0):
		if n == len_facs:
			yield 1
		else:
			pows = [1]
			cur = facs_set[n]
			pow_max = facs_list.count(cur)

			for i in range(pow_max):
				pows.append(pows[-1] * cur)

			for j in rec_gen(n + 1):
				for prime in pows:
					yield prime * j

	for k in rec_gen():
		yield k

def proper_divisors(x):
	return list(divisors(x))[:-1]

def amicable(x):
	sum_a = sum(proper_divisors(x))
	return x != sum_a and x == sum(proper_divisors(sum_a))

def cyclic_number(prime, base):
	return (base**(prime - 1) - 1) / prime

def coprime(a, b=10):
	return set(factors(a)).isdisjoint(set(factors(b)))

def gcd(a, b):
	while a != 0:
		a, b = b % a, a
	return b

def lcm(a, b):
	return a * b / gcd(a, b)

def discriminant(a, b, c):
	return b*b - 4*a*c

def discriminant_bc(b, c):
	return b*b - 4*c

def complex_quad_polys(a_range, b_range):
	for a in a_range:
		for b in b_range:
			if discriminant(1, a, b) < 0:
				yield a, b

def bits_to_mask(bits):
	return (2**bits) - 1

def pack_xy(x, y, bits):
	return x | (y << bits)

def unpack_x(xy, mask):
	return xy & mask

def unpack_y(xy, bits):
	return xy >> bits

def unpack_xy(xy, mask, bits):
	return [unpack_x(xy, mask), unpack_y(xy, bits)]