# The P-Boxes of DES

# This is general code to implement any P-Box
# n is the number of input bits
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


# IP is used at the beginning of the encryption process
# IPinv is used at the end of the encryption process
# E is used at the start and Q at the end in the Feistel function f
# PC1, PC2, RHL1, RHL2 are used in the key schedule


# Initial Permutation
# B64 to B64
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17,  9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]


# Final Permutation 
# Inverse of the Initial Permutation
# B64 to B64
IPinv = [40, 8, 48, 16, 56, 24, 64, 32,
         39, 7, 47, 15, 55, 23, 63, 31,
         38, 6, 46, 14, 54, 22, 62, 30,
         37, 5, 45, 13, 53, 21, 61, 29,
         36, 4, 44, 12, 52, 20, 60, 28,
         35, 3, 43, 11, 51, 19, 59, 27,
         34, 2, 42, 10, 50, 18, 58, 26,
         33, 1, 41,  9, 49, 17, 57, 25]


# Expansion Permutation 
# B32 to B48
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]


# Permutation
# B32 to B32
Q = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]



# Permuted Choice One
# B64 to B56
PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 
       58, 50, 42, 34, 26, 18, 10, 2, 
       59, 51, 43, 35, 27, 19, 11, 3, 
       60, 52, 44, 36, 63, 55, 47, 39, 
       31, 23, 15, 7, 62, 54, 46, 38, 
       30, 22, 14, 6, 61, 53, 45, 37, 
       29, 21, 13, 5, 28, 20, 12, 4]


# Permuted Choice Two
# B56 to B48
PC2 = [14, 17, 11, 24, 1, 5, 3, 28,
       15, 6, 21, 10, 23, 19, 12, 4,
       26, 8, 16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55, 30, 40,
       51, 45, 33, 48, 44, 49, 39, 56,
       34, 53, 46, 42, 50, 36, 29, 32]


# Rotate Halves Left by 1
# B56 to B56
RHL1 = list(range(2, 29)) + [1] + list(range(30, 57)) + [29]


# Rotate Halves Left by 2
# B56 to B56
RHL2 = list(range(3, 29)) + [1, 2] + list(range(31, 57)) + [29, 30]

