# The Data Encryption Standard (DES)

from des_pbox import *
from des_sbox import S


# The Feistel function of DES
# x is 32 bits
# key is 48 bits
# The output is 32 bits
# Note that 0x3f in binary is six ones: 111111
def f(x, key):
	x = pbox(x, E, 32)
	x ^= key
	y = 0
	for i in range(1, 9):
		z = (x >> 6 * (8 - i)) & 0x3f
		y <<= 4
		y ^= S(i, z)
	return pbox(y, Q, 32)

