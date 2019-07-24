#!/usr/bin/env python3.6
import argparse
import functools
import numpy as np
import sys

# SIZE = 1000
SIZE = 6

# T = np.array([
#   [15, 0, 0, 0, 0, 0],
#   [-14, -7, 0, 0, 0, 0],
#   [20, -13, -5, 0, 0, 0],
#   [-3, 8, 23, -26, 0, 0],
#   [1, -4, -5, -18, 5, 0],
#   [-16, 31, 2, 9, 28, 3],
# ])

T = np.full((SIZE, SIZE), 0, np.int64)

def mod(a, b):
  assert b > 0
  return a % b if a >= 0 else (a%b)-b

def fillT():
  r = 0
  t = 0
  k = 1
  for n in range(1, SIZE+1):
    for c in range(n):
      t = mod(615949*t + 797807, 1 << 20)
      T[r, c] = t - (1 << 19)
      k += 1
    r += 1


def outOfBounds(r, c):
  return not (0 <= r < SIZE and 0 <= c < SIZE)


@functools.lru_cache(maxsize=None)
def sumDown(r, c, s):
  if outOfBounds(r, c) or s <= 0: return 0
  return T[r, c] + sumDown(r+1, c, s-1)


@functools.lru_cache(maxsize=None)
def sumTriangle(r, c, s):
  if outOfBounds(r, c) or s <= 0: return 0
  return sumDown(r, c, s) + sumTriangle(r+1, c+1, s-1)


# for r in reversed(range(SIZE)):
#   for c in reversed(range(r+1)):
#     for s in range(1, SIZE+1):
#       sumDown[r, c, s] = T[r, c] + sumDown[r+1, c, s-1]
#       sumTriangle[r, c, s] = sumDown[r, c, s] + sumTriangle[r+1, c+1, s-1]


if __name__ == '__main__':
  sys.setrecursionlimit(1 << 20)
  fillT()
  sumDown = np.full((SIZE+1,)*3, 0, dtype=np.int64)
  sumTriangle = np.full((SIZE+1,)*3, 0, dtype=np.int64)
  ans = +np.inf
  for r in reversed(range(SIZE)):
    for c in reversed(range(r+1)):
      for s in range(1, SIZE+1):
        sumDown[r, c, s] = T[r, c] + sumDown[r+1, c, s-1]
        sumTriangle[r, c, s] = sumDown[r, c, s] + sumTriangle[r+1, c+1, s-1]
        ans = min(ans, sumTriangle[r, c, s])
    print(r)
  print('Ans', ans)
