#!/usr/bin/env python3
import argparse
import numpy as np
from functools import lru_cache


S = [1,3,6,8,10,11]
S = [(i**2) for i in range(100)]


N = sum(S)
def solve(c):
  DP = np.full((N+1, len(S)+1, c+1), 0)

  DP[0,len(S),0] = 1
  for n in range(N+1):
    for i in reversed(range(len(S))):
      for l in range(c+1):
        a = DP[n-S[i],i+1,l-1] if 0<=n-S[i]<=N and 0 <= l-1 else 0
        b = DP[n,i+1,l]
        DP[n,i,l] = min(a+b, 2)
  print(DP)
  return sum(n for n in range(N+1) if DP[n,0,c]==1)
'''
  def f(n, i, l):
    if n < 0 or l < 0: return 0
    if i == len(S): return bool(n == 0 and l == 0)
    if DP[n,i,l] == -1:
      DP[n,i,l] = min(f(n-S[i], i+1, l-1) + f(n, i+1, l), 2)
    return DP[n,i,l]
  return f(n, 0, 50)
'''



if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  print(solve(3))
