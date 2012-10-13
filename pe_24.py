import itertools

# counter = 0
# for p in itertools.permutations('0123456789'):
# 	counter += 1
# 	if counter == 1000000:
# 		print(p)

print(next(itertools.islice(itertools.permutations('0123456789'), 999999, 1000000)))

# 2783915460