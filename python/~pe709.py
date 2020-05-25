#!/usr/bin/env python3.6
import numpy as np

from functools import lru_cache

MOD = 1020202009

@lru_cache(maxsize=None)
def choose(n, k, m):
  if n < 0 or k < 0 or n < k: return 0
  if n == 0 or k == 0: return 1
  return ((choose(n-1, k, m) % m) + (choose(n-1, k-1, m) % m)) % m

def F(N):
  @lru_cache(maxsize=None)
  def f(bags, n):
    if n == N: return 1
    ans = 0
    for group in range(bags//2+1):
      ways = 1  # choose(bags, 2*group, MOD)
      ans = (ans + ways*f(bags-2*group+1, n+1)) % MOD
    return ans
  return f(0, 0)
