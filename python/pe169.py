#!/usr/bin/env python3.6
# Example usage:
# $ ./pe169.py -N 10
# 5
import argparse
import numpy as np
import sys

from functools import lru_cache


BASE = 2
REPEATS = 2

# Recursive version.
def w(N, A):
  @lru_cache(maxsize=None)
  def ways(i, carry=0):
    if i == len(A): return int(carry == 0)
    return sum(
      ways(i+1, (carry+k)//BASE)
      for k in range(REPEATS+1)
      if (carry+k)%BASE == A[i]
    )
  return ways(0)


# Iterative version (more efficient).
def f(N, A):
  K = len(A)
  W = np.zeros((K+1,BASE), dtype=int)
  W[K,0] = 1
  for i in reversed(range(K)):
    for c in range(BASE):
      W[i,c] = sum(
        W[i+1, (c+k)//BASE]
        for k in range(REPEATS+1)
        if (c+k)%BASE == A[i]
      )

  return W[0,0]


def main(args):
  N, A, fn = args.N, args.A, args.fn
  print(fn(N, A))


if __name__ == '__main__':
  sys.setrecursionlimit(1 << 30)
  MODES = { 'iterative': f, 'recursive': w }
  parser = argparse.ArgumentParser(
    '''
    The number of different ways a number can be expressed as a\
    sum of powers of 2.
    '''
  )
  parser.add_argument('-N', type=int, default=10**25)
  parser.add_argument(
    '--mode',
    choices=MODES.keys(),
    default='iterative',
  )

  args = parser.parse_args()
  args.A = [int(b) for b in reversed(bin(args.N)[2:])]
  args.fn = MODES[args.mode]
  main(args)
