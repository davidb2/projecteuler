# from numbers import Number
# from copy import deepcopy
# from operator import mul
# from fractions import Fraction

# product = lambda it: reduce(mul, it, 1)

# def pprint(matrix):
#     assert(isinstance(matrix, Matrix))
#     print str(matrix)

# class Matrix:
#     def __init__(self, grid):
#         assert(isinstance(grid, list))
#         assert(grid != [])
#         assert(isinstance(grid[0], list))
#         row_lengths = set()
#         for i in xrange(len(grid)):
#             item = grid[i]
#             assert(isinstance(grid[i], list))
#             row_lengths.add(len(grid[i]))
#             assert(len(row_lengths) == 1)
#             for j in xrange(len(grid[i])):
#                 assert(isinstance(j, Number))
        
#         # passed all prerequisites

#         self.matrix = deepcopy(grid)
#         self.rows = len(grid)
#         self.cols = len(grid[0])
    
#     @staticmethod
#     def transpose(src):
#         assert(isinstance(src, Matrix))
#         dest = Matrix([
#             [0 for c in xrange(src.rows)] 
#             for r in xrange(src.cols)
#         ])
#         for i in xrange(dest.rows):
#             for j in xrange(dest.cols):
#                 dest[i][j] = src[j][i]
#         return dest
    
#     def __add__(self, other):
#         assert(isinstance(other, Matrix))
#         assert(self.rows == other.rows and self.cols == other.cols)
#         dest = Matrix([
#             [0 for c in xrange(self.cols)] 
#             for r in xrange(self.rows)
#         ])
#         for i in xrange(self.rows):
#             for j in xrange(self.cols):
#                 dest[i][j] = self[i][j] + other[i][j]
#         return dest

#     def __sub__(self, other):
#         assert(isinstance(other, Matrix))
#         assert(self.rows == other.rows and self.cols == other.cols)
#         dest = Matrix([
#             [0 for c in xrange(self.cols)] 
#             for r in xrange(self.rows)
#         ])
#         for i in xrange(self.rows):
#             for j in xrange(self.cols):
#                 dest[i][j] = self[i][j] - other[i][j]
#         return dest
    
#     def __mul__(self, other):
#         assert(isinstance(other, Matrix))
#         assert(self.cols == other.rows)
#         dest = Matrix([
#             [0 for c in xrange(other.cols)] 
#             for r in xrange(self.rows)
#         ])
#         for i in xrange(self.rows):
#             for j in xrange(other.cols):
#                 for k in xrange(self.cols):
#                     dest[i][j] += self[i][k] * other[k][j]
#         return dest
    
#     # https://en.wikipedia.org/wiki/Gaussian_elimination#Pseudocode
#     def _row_reduce(self):
#         dest = deepcopy(self)
#         for k in xrange(min(dest.rows, dest.cols)):
#             # find the kth pivot
#             i_max = max(xrange(k, dest.rows), key=lambda i: abs(dest[i][k]))

#             # check if singular
#             if dest[i_max][k] == 0:
#                 raise Exception('Matrix is singular!')
            
#             # swap kth and i_maxth rows
#             for c in xrange(dest.cols):
#                 dest[k][c], dest[i_max][c] = dest[i_max][c], dest[k][c]
            
#             # do for all rows below pivot
#             for i in xrange(k+1, dest.rows):
#                 f = Fraction(dest[i][k]) / Fraction(dest[k][k])

#                 # do for all remaining elements in current row
#                 for j in xrange(k+1, dest.cols):
#                     dest[i][j] -= dest[k][j] * f
                
#                 # fill lower triangular matrix with zeros
#                 dest[i][k] = 0
        
#         pprint(dest)
#         # back-substitution
#         for i in reversed(xrange(1, dest.rows)):
#             pprint(dest)
#             # find first non-zero entry
#             j = -1
#             for c in xrange(dest.cols-1):
#                 if dest[i][c] != 0:
#                     j = c
#                     break

#             # if j == 0, overdetermined
#             if j == -1:
#                 continue
            
#             f1 = Fraction(1) / Fraction(dest[i][j])
#             for c in xrange(dest.cols):
#                 dest[i][c] *= f1

#             f2 = - Fraction(dest[i-1][j]) / Fraction(dest[i][j])
#             for c in xrange(dest.cols):
#                 dest[i-1][c] += dest[i][j] * f2  
        
#          # find first non-zero entry
#         j = -1
#         for c in xrange(dest.cols-1):
#             if dest[0][c] != 0:
#                 j = c
#                 break
#         if j != -1:
#             f1 = Fraction(1) / Fraction(dest[0][j])
#             for c in xrange(dest.cols):
#                 dest[0][c] *= f1

#         # retrieve solution vector
#         ans = [0 for i in xrange(dest.rows)]
#         for i in xrange(dest.rows):
#             j = -1
#             # find first, non-zero entry
#             for c in xrange(dest.cols-1):
#                 if dest[i][c] == 1:
#                     j = c
#                     break
            
#             if j == -1:
#                 continue
            
#             ans[j] = dest[i][~0]
        
#         return Matrix.transpose(Matrix([ans]))

#     def augment(self, other):
#         assert(isinstance(other, Matrix))
#         assert(self.rows == other.rows)

#         dest = Matrix([
#             [self[r][c] if c < self.cols else other[r][c-self.cols] for c in xrange(self.cols + other.cols)] 
#             for r in xrange(self.rows)
#         ])
#         return dest

#     @staticmethod
#     def solve(A, b):
#         assert(isinstance(A, Matrix))
#         assert(isinstance(b, Matrix))
#         assert(A.rows == b.rows)
#         assert(b.cols == 1)

#         augmented_matrix = A.augment(b)
#         reduced_matrix = augmented_matrix._row_reduce()
        
#         return (
#             Matrix.transpose(
#                 Matrix([[reduced_matrix[r][~0]
#                 for r in xrange(reduced_matrix.rows)]])
#             )
#         )

#     @property
#     def shape(self):
#         return (self.rows, self.cols)
    
#     def __getitem__(self, key):
#         return self.matrix[key]

#     def __str__(self):
#         padding = 1
#         for i in xrange(self.rows):
#             for j in xrange(self.cols):
#                 padding = max(padding, 1+len(str(self[i][j])))
#         rows = []
#         for i in xrange(self.rows):
#             acc = ''
#             for j in xrange(self.cols):
#                 acc += str(self[i][j]).ljust(padding, ' ')
#             rows.append('[{}]'.format(acc))
#         return '\n'.join(rows)

import numpy as np

def OP(f, degrees):
    b = np.matrix([[f(n) for n in xrange(1, degrees+1)]], dtype=np.int64).transpose()
    A = np.matrix([
        [x ** n for n in xrange(degrees)]
        for x in xrange(1, degrees+1)
    ], dtype=np.int64)
    x = np.linalg.solve(np.matmul(A.transpose(), A), np.matmul(A.transpose(), b))
    print x
    return lambda n: sum(x[e, 0]*n**e for e in xrange(degrees))

u = lambda n: sum(((-1)**x) * (n**x) for x in xrange(10+1))
f = lambda n: n**3
ans = 0
for degree in xrange(1, 10+1):
    op = OP(u, degree)
    n = 1
    while op(n) == u(n):
        n += 1
    ans += op(n)
print ans