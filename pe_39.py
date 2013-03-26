# find the perimeter of a right triangle <= 1000 that
# has the most solutions for sides a,b,c

print(max(map(lambda x: (len(x[0]) / 2, x[1]), [(filter(lambda x: int(x) == x, [p * (x - p / 2.0) / (x - p) for x in range(1, p / 2)]), p) for p in range(2, 1000 + 1, 2)])))
# (8, 840)
