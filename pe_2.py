# find the sum of all even numbered fibonacci numbers under 4 000 000

from pe_utils import fibonacci_generator as fib_gen 

print(sum([i for i in fib_gen(4000000) if i % 2 == 0]))

# 4613732