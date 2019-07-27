import numpy as np

from scipy.special import binom

'''
def E(n):
  if n == 0xffffffff: return 0
  return 1 + E(np.random.randint(1 << 32) | n)

def sim(turns):
  return sum(E(0) for _ in range(turns)) / turns
'''

def P(i, j):
  if j < i: return 0
  return (2**i)*binom(32-i,j-i)/(2**32)


if __name__ == '__main__':
  M = np.full((33, 33), 0, np.float64)
  b = np.full((33,), -1, np.float64)

  # E[32] = 0.
  M[32, 32] = 1
  b[32] = 0

  # E[i] = sum_j P(i, j) * (1 + E[j]).
  for i in range(32):
    for j in range(32):
      M[i, j] = P(i, j) - int(i == j)

  X = np.linalg.solve(M, b)
  print('Ans:', X[0])
