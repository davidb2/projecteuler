#!/usr/bin/env python3.6
import numpy as np

from functools import lru_cache


@lru_cache(maxsize=None)
def solve(t, k):
  if all(x == k for x in t): return 1
  if any(x > k for x in t): return 0
  if any(x == y and x != 0 and x != k for x, y in zip(t, t[1:])): return 0

  j = np.argmin(t)
  return (
    solve(tuple([x, x+2][i==j] for i, x in enumerate(t)), k)
    +
    solve(tuple([x, x+3][i==j] for i, x in enumerate(t)), k)
  )

if __name__ == '__main__':
  ans = solve((0,)*10, 32)
  print(ans)
