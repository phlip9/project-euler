# num of letters to write out all nums from 1 - 1000

from math import log10

def strip(s):
	return s.replace(" ", "")

def ones_digit(n):
	return abs(n) % 10

def tens_digit(n):
	return ones_digit(int(n / 10))

def hundreds_digit(n):
	return ones_digit(int(n / 100))

def thousands_digit(n):
	return ones_digit(int(n / 1000))

def num_letters(n):
	one = ones_digit(n)
	ten = tens_digit(n)
	hund = hundreds_digit(n)
	thou = thousands_digit(n)

	amnt = 0

	if (thou != 0 or hund != 0) and (ten != 0 or one != 0):
		amnt += 3 # and

	if thou != 0:
		amnt += len(ones_map[thou]) + 8 # thousand

	if hund != 0:
		amnt += len(ones_map[hund]) + 7 # hundred

	if ten == 1:
		amnt += len(teens_map[n % 100]) # get last two digits
	else:
		amnt += len(tens_map[ten] + ones_map[one])

	return amnt

ones_map = \
	{0:"", 1:"one", 2:"two", 3:"three", 4:"four", \
	5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}

teens_map = \
	{10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", \
	15:"fifteen", 16:"sixteen", 17: "seventeen", 18:"eighteen", 19:"nineteen"}

tens_map = \
	{0:"", 1:"ten", 2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", \
	6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}

print(ones_map[3], ones_map[5], ones_map[9])
print(teens_map[10], teens_map[17], teens_map[19])

print("ones_digit:", ones_digit(321))
print("tens_digit:", tens_digit(321))
print("hundreds_digit:", hundreds_digit(321))


#  num :     name       : length
#   43 : "forty three"  : 10
#   99 : "ninety nine"  : 10
#    3 :    "three"     : 5
#  155 : "one hundred and fifty five" : 22
# 1000 : "one thousand" : 11
#  707 : "seven hundred and seven" : 20
print(num_letters(43))
print(num_letters(99))
print(num_letters(3))
print(num_letters(155))
print(num_letters(1000))
print(num_letters(707))

total = 0

for i in range(1, 1000 + 1, 1):
	total += num_letters(i)


print("total length:", total)

# 21124