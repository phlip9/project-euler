sum_squares = 0
square_sum = 0

i = 0

for i in range(1, 101, 1):
	sum_squares = sum_squares + i * i
	square_sum += i
	print(sum_squares, " : ", square_sum)


square_sum = square_sum*square_sum

print("difference: ", square_sum - sum_squares)
