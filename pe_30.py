# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

nums = []

limit = 6 * 9**5

for i in range(2, limit):
	num_sum = sum(int(a)**5 for a in str(i))
	if(i == num_sum):
		nums.append(i)

print(nums)
print(sum(nums))

# 443839