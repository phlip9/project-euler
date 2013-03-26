# Goldbach conjuecture
# find the first odd number that can be expressed as
# 2x a square + a prime
# ex: 19 = 17 + 2(1^2)

from pe_utils import prime_sieve
from itertools import count

prime_gen = prime_sieve()
primes = [next(prime_gen), next(prime_gen)]

square_gen = (2*i*i for i in count(1))
squares = [next(square_gen)]

composite_odds = filter(lambda odd: odd not in primes, count(3, 2))

def fail():
    for odd in composite_odds:
        while(primes[-1] < odd):
            primes.append(next(prime_gen))

        while(squares[-1] < odd):
            squares.append(next(square_gen))

        diffs = (odd - square for square in squares if square < odd)
        if not any(map(lambda diff: diff in primes, diffs)):
            yield odd

print(next(fail()))
