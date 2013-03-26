# Find the largest 1 - 9 pandigital number that can be formed as a
# concatination of products 1, 2, n where n > 1

from itertools import count
from pe_utils import pandigital

max_pand = 987654321

assert(pandigital(918273645))
assert(pandigital(123456789))
assert(not pandigital(223456789))
assert(not pandigital(1234567891))
assert(not pandigital(123, 9))

for i in range(1, 9999):
    prod = ""
    for j in count(1):
        prod += str(i * j)
        #print(i, j, prod)
        if pandigital(int(prod)):
            print(prod, i, j)
            break
        elif int(prod) > max_pand:
            break
