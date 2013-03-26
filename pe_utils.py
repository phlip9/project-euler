from math import sqrt
from itertools import compress, islice, count, cycle
from collections import defaultdict
from functools import reduce, lru_cache
from operator import mul
from random import randrange

#
# Utility Methods
#
def perfect_square(n):
    h = n & 0xF
    if h != 0 and h != 1 and h != 4 and h != 9:
        return False
    else:
        s = int(sqrt(n))
        return n == s*s

def palindromic(x):
	return str(x) == str(x)[::-1]

def lucas(n):
	return int(((1 + sqrt(5)) / 2)**n) + (n % 2 == 0)

def multiples(n, minimum, maximum):
    return (n*i for i in range(int(minimum / n) + 1, int(maximum / n) + 1))

def list_to_num(list_num):
    num = 0
    list_num = list_num[::-1]
    for i in enumerate(list_num):
        num += i[1] * 10**i[0]
    return num

def num_to_list(num):
    return map(int, str(num))
def fibonacci_generator(n=None):
	a, b = 0, 1

	while n == None or a < n:
		yield a
		a, b = b, a + b

def fib_matrix(n):
    if n == 0 or n == 1:
        return n
    else:
        return reduce(mult2d, [(0, 1, 1, 1)]*(n - 1))[3]

@lru_cache(maxsize=None)
def fib_recurse(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_recurse(n - 1) + fib_recurse(n - 2)

@lru_cache(maxsize=None)
def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1
def mult2d(a, b):
    return (a[0]*b[0] + a[1]*b[2], a[0]*b[1] + a[1]*b[3], a[2]*b[0] + a[3]*b[2], a[2]*b[1] + a[3]*b[3])
def pythag_triple(a, b, c):
	return ((a*a + b*b) == (c*c))

def triangle_num(n):
	return n*(n+1)/2

def prime_sieve(n=None):
	IT_MASK = (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0)
	MODULOS = frozenset((1, 7, 11, 13, 17, 19, 23, 29))
	D = {9:3, 25:5}

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

def primality_test(n):
    """Returns True if n is prime"""
    def  test_pass(a, s, d, n):
        a_pow = pow(a, d, n)
        if a_pow == 1:
            return True
        for i in range(s - 1):
            if a_pow == n - 1:
                return True
            a_pow = (a_pow * a_pow) % n
        return a_pow == n - 1
    if n % 2 == 0:
        if n == 2:
            return True
        else:
            return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for i in range(20):
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
			x = x // i
		else:
			i += 1
	if x > 1:
		yield int(x)

def factor_map(x, primes=None, distinct=False):
    if primes == None:
        primes = prime_sieve()
    for prime in primes:
        if prime > x:
            break
        exponent = 0
        while x % prime == 0:
            exponent, x = exponent + 1, x // prime
        if exponent != 0:
            if distinct:
                yield prime
            else:
                yield prime, exponent

def totient(n):
	return reduce(mul, ((p-1) * p ** (exp-1) for p, exp in factor_map(n)), 1)

def cartesian_product(set_1, set_2):
	return [x*y for x in set_1 for y in set_2]

def map_occurances(nums):
	intmap = defaultdict(int)
	for i in nums:
		intmap[i] += 1
	return intmap

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


#
# Test Methods
#

if __name__ == '__main__':
    pass
