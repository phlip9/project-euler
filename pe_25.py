# find the first term in the Fibonacci sequence to contain 1000 digits

# paper problem
# 1000 = n log10(Phi) - 1/2 log10(5) + 1
# n = ceil((999 + 1/2 log10(5)) / log10(Phi))
# n = 4782

from pe_utils import fibonacci_generator

list(fibonacci_generator(100000))
