# Find the sum of all products whose multiplicand/multiplier/product identity can be written as 1 - 9 pandigital

from math import log10

# def pandigital(n, digits=9):
# 	return len(n) == digits and "1234567890"[:digits].strip(n) == ""

# assert(pandigital(str(123), 3))
# assert(pandigital(str(15234), 5))
# assert(pandigital(str(391867254)))

products = []

for i in range(2, 100):
	for j in range(2000):
		product = i*j
		combined = str(i) + str(j) + str(product)
		if len(combined) == 9:
			if product not in products:
				if "123456789".strip(combined) == "":
					products.append(product)
					print(str(i) + " x " + str(j) + " = " + str(product) + " : " + combined)
					print("sum:", sum(products))

print(products)
# 45228