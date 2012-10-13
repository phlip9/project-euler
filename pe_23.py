# find the sum of all positive integers that cannot be written as the sum of two abundant numbers
from pe_utils import proper_divisors

# def abundant_nums(limit):
# 	for i in range(limit):
# 		if i < sum(proper_divisors(i)):
# 			yield i

limit = 20161

total = 0

abundants = set()

for i in range(limit + 1):
	if sum(proper_divisors(i)) > i:
		abundants.add(i)
	if not any (i - x in abundants for x in abundants):
		total += i

print("total:", total)

# 4179871