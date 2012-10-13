# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
from pe_utils import prime_sieve

def cycle_length(n):
	for i in range(1, 1000):
		if 10**i % n == 1:
			return i

longest_cycle = 0
d = 0

for i in range(1, 1000):
	current_cycle = cycle_length(i)
	if current_cycle != None and current_cycle > longest_cycle:
		longest_cycle = current_cycle
		d = i

print("1/" + str(d), "has cycle length of", longest_cycle)

#983