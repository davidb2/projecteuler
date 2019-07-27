#!/usr/bin/env python3.6
import argparse

from functools import lru_cache

BASE = 10

@lru_cache(maxsize=None)
def ways(t, l, first=True):
  if any(x > 3 for x in t): return 0
  if l == 0: return 1

  ans = 0
  z = list(t)
  for d in range(int(first), BASE):
    z[d] += 1
    ans += ways(tuple(z), l-1, first=False)
    z[d] -= 1

  return ans


if __name__ == '__main__':
  print(ways((0,)*10, 18))
