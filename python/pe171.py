#!/usr/bin/env python3.6
import argparse

from functools import lru_cache

BASE = 10
MOD = 10 ** 9

SQUARES = set([x**2 for x in range(100)])


@lru_cache(maxsize=None)
def isPerfectSquare(n):
  return n in SQUARES


@lru_cache(maxsize=None)
def ways(s, l):
  if l == 0: return int(isPerfectSquare(s)), 0

  ans = 0
  tcount = 0
  for d in range(BASE):
    count, sm = ways(s + d**2, l-1)
    ans = (ans + d * pow(BASE, l-1, MOD) * count + sm) % MOD
    tcount = (tcount + count) % MOD
  return tcount, ans


if __name__ == '__main__':
  print(ways(0, 20)[1])
