from pe_utils import palindromic

i = 0
j = 0

high_palind = 0

# first three digit number 100-999
for i in range(1000, 100, -1):
	# second three digit number 100-999
	for j in range(1000, 100, -1):
		mult = i * j
		if palindromic(mult) and mult > high_palind:
			print("palindrome: ", mult, " = ", i, " x ", j)
			high_palind = mult

print("highest palindrome: ", high_palind)