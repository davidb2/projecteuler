#!/usr/bin/env python3.6
import argparse
import numpy as np

from collections import Counter
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


LIMIT = 120000
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

@lru_cache(maxsize=None)
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
  return sorted(prods)


def products(n, last=2):
  if n == 1:
    yield ()
    return
  for d in (d for d in divisors(n) if d >= last):
    for ps in products(n//d, last=d):
      yield (d,) + ps
  yield from ()

def main(args):
  KLIM = 12000
  buckets = [np.inf]*(LIMIT+1)
  for n in range(2, LIMIT+1):
    for ps in products(n):
      p = n
      s = sum(ps)
      if s > p: continue
      ones = p-s
      k = len(ps) + ones
      buckets[k] = min(buckets[k], n)
  bs = buckets[2:KLIM+1]
  sbs = sum(set(bs))
  print(bs, sbs)


if __name__ == '__main__':
  main(None)
