# The Key Schedule Algorithm for DES

# n is the number of bits
# P is a list of integers of length m
# The integers in P are between 1 and n
# The input x is a n-bit integer
# The output y is a m-bit integer
def pbox(x, P, n):
	y = 0
	for i in P:
		y <<= 1
		y ^= (x >> (n - i)) & 1
	return y


# B64 to B56
PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 
       58, 50, 42, 34, 26, 18, 10, 2, 
       59, 51, 43, 35, 27, 19, 11, 3, 
       60, 52, 44, 36, 63, 55, 47, 39, 
       31, 23, 15, 7, 62, 54, 46, 38, 
       30, 22, 14, 6, 61, 53, 45, 37, 
       29, 21, 13, 5, 28, 20, 12, 4]


# B56 to B48
PC2 = [14, 17, 11, 24, 1, 5, 3, 28,
       15, 6, 21, 10, 23, 19, 12, 4,
       26, 8, 16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55, 30, 40,
       51, 45, 33, 48, 44, 49, 39, 56,
       34, 53, 46, 42, 50, 36, 29, 32]


# Rotate Halves Left by 1
RHL1 = list(range(2, 29)) + [1] + list(range(30, 57)) + [29]


# Rotate Halves Left by 2
RHL2 = list(range(3, 29)) + [1, 2] + list(range(31, 57)) + [29, 30]


# k is a 64-bit key
# The output is a list of sixteen 48-bit integers
def key_schedule(k):
	x = pbox(k, PC1, 64)
	keys = [] 
	for round in range(1, 17):
		if round in [1, 2, 9, 16]:
			x = pbox(x, RHL1, 56)
		else:
			x = pbox(x, RHL2, 56)
		keys.append(pbox(x, PC2, 56))				
	return keys


# test
k = int('AABB09182736CCDD', 16)
keys = key_schedule(k)
for key in keys:
	print(hex(key))

