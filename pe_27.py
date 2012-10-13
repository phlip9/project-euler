# Find the prime generating polynomial of form n^2 + an + b
# where |a| < 1000 & |b| < 1000 and generates the longest array of primes

from pe_utils import prime_sieve, discriminant_bc, complex_quad_polys, primes_to_n

primes = list(prime_sieve(10000))

# only quadratics with disriminant less than 0 can be prime generating
# |b| <= 63
# c cannot be negative, otherwise discriminant would be positive
# 1 <= c <= 1000
# |c| must be prime (1st iteration is always c, and since we're finding primes, c must always be prime)
poly_gen = complex_quad_polys(range(-63, 63 + 1), list(primes_to_n(1000)))

def polynomial(a, b, i):
	return i*i + a*i + b

highest_num_primes = 0
high_ab = None

for ab in poly_gen:
	iterations = 0
	while polynomial(ab[0], ab[1], iterations) in primes:
		iterations += 1

	if iterations > highest_num_primes:
		high_ab = ab
		highest_num_primes = iterations
		print(high_ab, highest_num_primes)

print(highest_num_primes, high_ab)
# print(num_primes(-61, 971))

# n^2 - 61 + 971