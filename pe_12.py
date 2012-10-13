from pe_utils import tau, triangle_num
# Find first triangle number with over 500 divisors

done = False
i = 1

while True:
	if tau(triangle_num(i)) >= 500:
		print("Highest triangle number with 500 divisors:", triangle_num(i))
		break
	else:
		i += 1

#76576500