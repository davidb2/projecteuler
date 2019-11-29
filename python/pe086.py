#!/usr/bin/env python3.6
import argparse
import numpy as np

from functools import lru_cache

last = (1, 1)
ps = set([1])

@lru_cache(maxsize=1<<8)
def isPerfectSquare(x):
  global last
  if x <= last[1]: return x in ps
  last = (last[0]+1, (last[0]+1)**2)
  ps.add(last[1])
  return isPerfectSquare(x)

def intPaths(m):
  ans = 0
  c = m
  for a in range(1,m+1):
    for b in range(a,m+1):
      aa = a*a
      bb = b*b
      cc = c*c
      xs = [(a+b)**2+cc, aa+(b+c)**2, (a+c)**2+bb]
      xs.sort()
      l = xs[0]

      if isPerfectSquare(l):
        ans += 1
  return ans

def upTo(M):
  return sum(intPaths(m) for m in range(1,M+1))


if __name__ == '__main__':
  print(upTo(10))
