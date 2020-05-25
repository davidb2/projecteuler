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


PI = [
  0,
  4,
  25,
  168,
  1229,
  9592,
  78498,
  664579,
  5761455,
  50847534,
  455052511,
  4118054813,
  37607912018,
  346065536839,
  3204941750802,
  29844570422669,
  279238341033925,
  2623557157654233,
  24739954287740860,
  234057667276344607,
  2220819602560918840,
  21127269486018731928,
  201467286689315906290,
  1925320391606803968923,
  18435599767349200867866,
  176846309399143769411680,
  1699246750872437141327603,
  16352460426841680446427399,
]

def G(N):
  PRIMES = primes(int(np.sqrt(10**N)))

  @lru_cache(maxsize=None)
  def g(lim, i=0):
    if lim <= 0: return 0
    if i == len(PRIMES): return int(lim >= 1)
    return 2*g(lim // PRIMES[i], i) + g(lim, i+1)
  return g(10**N)-2*len(PRIMES) + 2*PI[N]
