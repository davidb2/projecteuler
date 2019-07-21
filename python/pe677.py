#!/usr/bin/env python3.6
import argparse
import functools

from enum import Enum
from itertools import chain, combinations_with_replacement


MOD = 1000000007

'''
Rules:
  - The graph is connected and has no cycles or multiple edges.
  - Each node is either red, blue, or yellow.
  - A red node may have no more than 4 edges connected to it.
  - A blue or yellow node may have no more than 3 edges connected to it.
  - An edge may not directly connect a yellow node to a yellow node.
'''

class Color(Enum):
  RED = 0
  YELLOW = 1
  BLUE = 2


def partitions(n, k):
  if k == 0 and n == 0:
    yield ()
    return
  elif k <= 0:
    yield from ()
    return

  for i in range(n+1):
    for tail in partitions(n-i, k-1):
      yield (i,) + tail


@functools.lru_cache(maxsize=None)
def ways(n, color):
  assert n >= 0
  if n <= 1: return n

  ans = 0
  for r, y, b in partitions(n-1, 3):
    c2n = { Color.RED: r, Color.YELLOW: y, Color.BLUE: b }
    m = min(3 + int(color == Color.RED), n-1)
    for k in range(m+1):
      for c in chain.from_iterable(combinations_with_replacement(Color, k)):
        if color == Color.YELLOW == c: continue
        ans += ways(c2n[c], c)

  return ans


def g(n):
  return sum(ways(n, color) for color in Color)


def main(args):
  n = args.n
  print(g(n))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', type=int, default=10000)
  args = parser.parse_args()
  main(args)
