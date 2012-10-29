# find the last 10 digits of the sum of x**x from 1 to 1000

print(str(sum((x**x for x in range(1, 1001))))[-10:])
