# find the max sum in a 100 row triangle

nums = map(int, " ".join((line[:-1] for line in open("triangle.txt"))).split(" "))

size = 100

def get_num(row, col):
	return nums[get_index(row, col)]

def get_index(row, col):
    return int(((row + 1) * row) / 2) + col

def add_num(row, col, num):
	nums[get_index(row, col)] += num

assert(get_num(0, 0) == 59)
assert(get_num(size - 1, size - 1) == 35)

for row in range(size - 1, 0, -1):
    for col in range(row):
        add_num(row - 1, col, max(get_num(row, col), get_num(row, col + 1)))

print("Max sum:", nums[0])
