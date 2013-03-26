# Find the sum of all numbers equal to the factorial of their digits
# curious_nums = []

from functools import lru_cache
from itertools import count

@lru_cache()
def factorial(n):
    if n == 0:
        return 1
    if n <= 2:
        return n
    return n * factorial(n - 1)

curious_nums = filter(lambda x: x == sum(map(lambda y: factorial(int(y)), str(x))), count(3))

s = 0

while(True):
    num = next(curious_nums)
    s += num
    print(num, "sum:", s)
