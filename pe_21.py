# find sum of amicable numbers under 10000
from pe_utils import amicable

amicables = []

for i in range(10000):
	if amicable(i):
		amicables.append(i)

print("amicable numbers:", amicables)
print("sum of amicables:", sum(amicables))

#31626