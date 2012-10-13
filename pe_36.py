# find the sum of all numbers 1 - 1000000 that are palindromic in both base 10 and base 2

print(sum([n for n in range(1000000) if str(n) == str(n)[::-1] and bin(n)[2:] == bin(n)[:1:-1]]))