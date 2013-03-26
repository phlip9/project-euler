# find the largest ndigit pandigital prime
from pe_utils import primality_test, list_to_num
from itertools import permutations

print(max(filter(primality_test, map(list_to_num, permutations([1,2,3,4,5,6,7])))))
