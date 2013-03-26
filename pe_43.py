# find the sum of all 0-9 pandigitals exhibiting the
# particular sub-string divising property

from itertools import permutations
from pe_utils import list_to_num

nums = (2,3,5,7,11,13,17)
def substring_pandigital(list_d):
    for i in range(6, 0 - 1, -1):
        if list_to_num(list_d[i + 1:i + 4]) % nums[i] != 0:
            return False
    return True

print(sum(map(list_to_num, filter(substring_pandigital, map(list, permutations((1,2,3,4,5,6,7,8,9,0)))))))
