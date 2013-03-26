# Considering natural numbers of the form, a^b, where a, b < 100, what is the
# maximum digital sum?

from pe_utils import num_to_list

print(max((sum(num_to_list(a**b)) for a in range(1, 100) for b in range(1, 100))))
# 972
