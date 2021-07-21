#!/usr/bin/env python3
import argparse
import itertools
import numpy as np
import sys

from functools import lru_cache
from math import sqrt, factorial, floor, isclose

MOD = 10**9+7
MAX = 2*10**7+1
FACT = list(range(MAX))
IFACT = list(range(MAX))
FACT[0] = IFACT[0] = 1

def scanlr(fn, arr):
  '''In-place scan, left-to-right.'''
  for i in range(1, len(arr)):
    arr[i] = fn(arr[i-1], arr[i])

scanlr(lambda x, y: (x*y)%MOD, FACT)
scanlr(lambda x, y: (x*pow(y,-1, MOD))%MOD, IFACT)

def pyth_triples(limit):
  xs = set()
  for x in range(1, 1+int(sqrt(limit))):
    for y in range(1, 1+int(sqrt(limit))):
      z2 = x**2 + y**2
      z = sqrt(z2)
      if isclose(z, floor(z)):
        xs.add((x, y, int(z)))

  ys = sorted([(a**2, b**2) for a,b,_ in xs])
  return ys

def choose(n, k):
  return (FACT[n] * IFACT[k] * IFACT[n-k]) % MOD

def dominates(*ps):
  return all(x1 >= x2 for x1, x2 in zip(*ps))

def paths(p1, p2):
  if not dominates(p2, p1): return 0
  (x1, y1), (x2, y2) = p1, p2
  return choose(x2-x1+y2-y1, x2-x1)

def ways(A, n):
  ORIGIN = (0, 0)

  @lru_cache(maxsize=None)
  def _ways(k):
    if k < 0: return 0
    X = (n, n) if k == len(A) else A[k]
    # print(k, X)
    return ((paths(ORIGIN, X)%MOD) - (sum(
      (_ways(j)%MOD)*(paths(A[j], X)%MOD)
      for j in range(k)
    )%MOD))%MOD

  return _ways(len(A))


if __name__ == '__main__':
  sys.setrecursionlimit(1<<20)
  LIMIT = 10**7
  mines = pyth_triples(LIMIT)
  ways(mines, LIMIT)
