#!/usr/bin/env python3.6
import numpy as np
import sys

from functools import lru_cache

BASE = 10
MOD = 10 ** 9

@lru_cache(maxsize=None)
def S(n, r=0, d=23):
  if d > 23: return 0
  if n == 0: return int(r == 0 and d == 0)

  ans = 0
  for x in range(BASE):
    ans += S(n-1, (r + x * BASE ** (n-1)) % 23, d-x)
  return ans


if __name__ == '__main__':
  N = 1000

  S = np.full((23+1, 23+1), 0, dtype=np.int32)
  L = np.full((23+1, 23+1), 0, dtype=np.int32)
  L[0, 0] = 1
  for n in range(1, N+1):
    for r in range(23+1):
      for d in range(23+1):
        for x in range(min(BASE, d+1)):
          S[r, d] = (S[r, d] + L[(r + x * pow(BASE, n-1, 23)) % 23, d-x]) % MOD
    L, S = S, np.full((23+1, 23+1), 0, dtype=int)

  print(L[0, 23])
