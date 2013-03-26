# find the next number that is a triangle number
# a pentagonal number, and a hexagonal number

maximum = 32000

# all pentagonal numbers are also triangle numbers
pent_set = set((int((3*n*n - n)/2) for n in range(2, maximum)))
hex_set = set((int(2*n*n - n) for n in range(2, maximum)))

print(max(pent_set & hex_set))
