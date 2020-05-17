#!/usr/bin/env python3.6
import argparse
import math

from decimal import Decimal
from fractions import Fraction

from functools import lru_cache



@lru_cache(maxsize=None)
def binom(n, k):
  if n < 0 or k < 0: return 0
  if k == n or k == 0 or n == 0: return 1
  return binom(n-1, k) + binom(n-1, k-1)

def min2(a, b, c):
  return tuple(sorted((a,b,c)))[:2]

@lru_cache(maxsize=None)
def E(n, m):
  print(n, m)
  if n < 3 or m < 2: return (+math.inf, +math.inf)
  if m == 2:
    aa, bb = 0, 0
    for q in range(1, n-1):
      d = Fraction(1, n-2)
      x = n-q-1
      a, b = sorted((q, x))
      print((n,m), d, (a, b))
      input()
      aa += d*a
      bb += d*b

    print(n, m)
    print((aa, bb))
    input()
    return (aa, bb)

  aa, bb = 0, 0
  for k in range(1, n-2):
    d = Fraction(binom(n-k-3,m-2),binom(n-3,m-1))
    a, b = min2(Fraction(k,1), *E(n-k,m-1))
    print((n,m), d, (a, b))
    input()
    aa += d*a
    bb += d*b

  print(n, m)
  print((aa, bb))
  input()
  return (aa, bb)


def main(args):
  n, m = args.n, args.m
  ans = E(n, m)
  print(ans)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', type=int, default=10**7)
  parser.add_argument('-m', type=int, default=10**2)
  args = parser.parse_args()
  main(args)
