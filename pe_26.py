# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
from pe_utils import prime_sieve

def cycle_length(n):
	for i in range(1, 1000):
		if 10**i % n == 1:
			return i

longest_cycle = max(filter(lambda x: x[0] != None, zip(map(cycle_length, range(1, 1000)), range(1, 1000))))[1]

print(longest_cycle)

#983
