# find d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
# in the number 123456789101112131415...

from operator import mul

n = "".join(map(str, range(1, 185185 + 1)))
print(reduce(mul, map(int, [n[10**i - 1] for i in range(7)])))

# 210
