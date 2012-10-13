from math import factorial

# from pe_utils import bits_to_mask, pack_xy, unpack_x, unpack_y

# # int supported stack
# class XYStack(object):
# 	def __init__(self, bits, mask):
# 		self.bits = bits
# 		self.mask = mask
# 		self.length = 0

# 	def push(self, xy):
# 		self.stack = (self.stack << self.bits) | xy
# 		length += 1

# 	def pop(self):
# 		tmp = self.stack & mask
# 		self.stack >>= mask
# 		length -= 1
# 		return tmp

# 	def peek(self):
# 		return self.stack & mask

# 	def get(self, index):
# 		return (self.stack >> ((index + 1) * bits)) & mask

# 	def set(self, index, xy):
# 		zero(index)
# 		self.stack |= (xy << (index * bits))

# 	def zero(self, index):
# 		# TODO: Replace with proper twos complement mask zero
# 		self.stack ^= get(index) << (index * bits)

# bits = 10
# mask = bits_to_mask(bits)
# print(bits, mask, bin(bits), bin(mask))

# x = 5
# y = 22

# print("x:", x, "y:", y, "pack_xy:", bin(pack_xy(x, y, bits)))


# better way, binomial coefficient

sides = 20
print(factorial(2*sides) / ((factorial(sides) * factorial(sides))))

#137846528820