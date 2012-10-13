# Find the sum of the numbers in a 1001 x 1001 spiral

value = 1
sum_value = 1

for i in range(1 + 1, 501 + 1):
	for a in range(4):
		value += 2*i - 2
		sum_value += value

print("value:", value, "sum:", sum_value)

# 669171001