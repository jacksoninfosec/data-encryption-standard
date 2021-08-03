# Implementation of the Key Schedule of DES

from des_pbox import *


# k is a 64-bit key
# The output is a list of sixteen 48-bit round keys
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

