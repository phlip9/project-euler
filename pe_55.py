# How many Lychrel numbers are there below ten-thousand?

from pe_utils import palindromic

max_iterations = 50

def lychrel_recursive(n, i=1):
    if i == 50:
        return True
    n = n + int(str(n)[::-1])
    if palindromic(n):
        return False
    else:
        return lychrel_recursive(n, i + 1)

print(sum(map(lychrel_recursive, range(1, 10000 + 1))))
