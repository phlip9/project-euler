from pe_utils import *

i = 232000000
running = True

while running:
	j = 0
	for j in range(1, 21, 1):
		if not divisible(i, j):
			i += 1
			print(i, " : failed")
			break
		else:
			if j == 20:
				print(i, " : worked")
				running = False
				break
