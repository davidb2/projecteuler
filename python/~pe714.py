#!/usr/bin/env python3.6
import argparse
import numpy as np

from functools import lru_cache

def primes(n):
  ps = np.full(shape=(n+1,), fill_value=True)
  ps[0] = ps[1] = False
  ps[4::2] = False

  lim = int(np.sqrt(n))+2
  for i in range(3, lim, 2):
    if not ps[i]: continue
    ps[3*i:n+1:2*i] = False

  return np.where(ps)[0]


LIMIT = 10**7
PRIMES = primes(int(np.sqrt(LIMIT))+3)
SPRIMES = set(PRIMES)

@lru_cache(maxsize=None)
def factor(n, i=0):
  if n <= 0: return []
  if n in SPRIMES: return [n]
  lim = int(np.sqrt(n)) + 2
  for ii, p in enumerate(PRIMES[i:]):
    if p > lim: break
    if n % p == 0: return [p] + factor(n//p, ii+i)
  return []

def divisors(n):
  c = Counter(factor(n))
  xs = list(c.keys())[::-1]
  prods = []
  def pp(i=0, prod=1):
    if i == len(c):
      prods.append(prod)
      return
    [pp(i+1, prod=xs[i]**m*prod) for m in range(c[xs[i]]+1)]
  pp()
  return prods

def duo(n, D):
  buckets = [np.inf]*(n+1)
  for d1 in range(10):
    for d2 in range(10):
      for r in range(1, D):
        for xs in product((d1, d2), repeat=r):
          dd = int(''.join([str(c) for c in xs]))
          if dd == 0: continue
          for x in sorted(divisors(dd)):
            if x > n: break
            buckets[x] = min(buckets[x], dd)
  return buckets
