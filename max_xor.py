
def maxXor(l,r):
	value = l ^ r
	value |= value >> 1
	value |= value >> 2
	value |= value >> 4
	return value

print(maxXor(10, 13))
print(3>>2)