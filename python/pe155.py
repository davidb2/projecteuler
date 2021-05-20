#!/usr/bin/env python3
import argparse

from collections import defaultdict
from fractions import Fraction


distinct = defaultdict(set)
distinct[0] = {Fraction(0)}
distinct[1] = {Fraction(60)}

def nums(n):
  '''n capacitors'''
  assert n >= 0
  if n in distinct: return distinct[n]
  for k in range(1, n):
    xs = nums(k)
    ys = nums(n-k)
    for x in xs:
      for y in ys:
        # parallel.
        distinct[n].add(x+y)
        # series.
        distinct[n].add(1/(1/x+1/y))
  return distinct[n]

def D(n):
  d = set()
  for i in range(1, n+1):
    d.update(distinct[i])
  return len(d), d

if __name__ == '__main__':
  n = 18
  d = nums(n)
  x, y = D(n)
  print(y)
  print(x)
