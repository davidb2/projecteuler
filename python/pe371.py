#!/usr/bin/env python3.6
import argparse
import sys

from decimal import Decimal, getcontext
from functools import lru_cache

M = None
N = None

# This is wrong! 000 and 500 need to be treated differently.
@lru_cache(maxsize=None)
def E(x):
  '''
  E_x = x/M*(.5*1 + .5(1+E_x)) + (1-x/M)(1+E_{x+1}) for x < M
  E_M = 1 + .5*E_{M}
  '''
  if x == M: return 2
  return N*(1+(1-x/M)*E(x+1))/(N-x)

# Markov chain and solved for expectations.
@lru_cache(maxsize=None)
def Ep(x,b):
  if x == M-1:
    if b == 1: return 2
    if b == 0: return 2 + 2/N*Ep(x,b+1)
  else:
    if b == 1: return (1+(1-2/N*(1+x))*Ep(x+1,b)) / (1-1/N*(1+x))
    if b == 0: return (1+(1-2/N*(1+x))*Ep(x+1,b)+1/N*Ep(x,b+1)) / (1-1/N*(1+x))


def main(args):
  global N, M
  N = args.N
  M = N // 2

  print(Ep(0, 0))


if __name__ == '__main__':
  sys.setrecursionlimit(1 << 30)
  getcontext().prec = 10
  parser = argparse.ArgumentParser()
  parser.add_argument('-N', type=Decimal, default=1000)

  args = parser.parse_args()
  assert 2*(args.N//2) == args.N, ('N must be even.', 2*(args.N//2), N,)
  main(args)
