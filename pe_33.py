# the denominator of the lowest common terms of the product of all
# unorthodox fractions with 2 digit numerators and denominators

from fractions import Fraction

# def is_unorthodox(ndx):
# 	return Fraction(ndx[0] * 10 + ndx[2], ndx[2] * 10 + ndx[1]) == Fraction(ndx[0], ndx[1])

# assert(is_unorthodox((4,8,9))) # 49/98

# print(reduce(lambda fraction1, fraction2: fraction1 * fraction2, map(lambda ndx: Fraction(ndx[0], ndx[1]), filter(is_unorthodox, [(n, d, x) for n in range(1,10) for d in range(1,10) for x in range(n + 1, 10)]))))

# one liner :P
print(reduce(lambda fraction1, fraction2: fraction1 * fraction2, map(lambda ndx: Fraction(ndx[0], ndx[1]), filter(lambda ndx: Fraction(ndx[0] * 10 + ndx[2], ndx[2] * 10 + ndx[1]) == Fraction(ndx[0], ndx[1]), [(n, d, x) for n in range(1,10) for d in range(1,10) for x in range(n + 1, 10)]))))

# 1/100