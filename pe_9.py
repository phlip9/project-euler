from pe_utils import pythag_triple
from sys import exit

#Find product of pythagorean triplet where a + b + c == 1000

a = 0
b = 0
c = 0

for a in range(1, 1000):
	for b in range(1, 1000):
		for c in range(1, 1000):
			if (a + b + c == 1000) and pythag_triple(a, b, c):
				print("Product of a*b*c: ", (a*b*c), " - a, b, c:", a, " ,", b, " ,", c)
				exit()