#!/usr/bin/env pythhon3.6
import argparse
import numpy as np


DIV = 250
LIMIT = 250250
MOD = 10 ** 16


# The recurrence.
def ways(r, i):
  if i > LIMIT: return int(r == 0)
  return (ways((r + pow(i, i, DIV)) % DIV, i+1) + ways(r, i+1)) % MOD


if __name__ == '__main__':
  W = np.full((DIV, LIMIT+2), 0, dtype=np.int64)
  W[0, LIMIT+1] = 1

  for i in reversed(range(1, LIMIT+1)):
    for r in range(DIV):
      rp = (r + pow(i, i, DIV)) % DIV
      W[r, i] = (W[rp, i+1] + W[r, i+1]) % MOD
    print(i)

  print('Ans:', W[0, 1]-1)
