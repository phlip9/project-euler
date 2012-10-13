# Find the sum of all numbers equal to the factorial of their digits
# curious_nums = []

factorials = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}

# for i in range(10, 50000):
# 	if i == sum(map(lambda d: factorials[int(d)],list(str(i)))):
# 		curious_nums.append(i)

curious_nums = [i for i in range(10, 50000) if i == sum(factorials.get(int(n)) for n in str(i))]

print(curious_nums)
print(sum(curious_nums))