#!/usr/bin/env python3.6
import argparse

from collections import deque


def compute(k):
  q = deque()

  fs = {}

  # Base case.
  for i in range(1, k):
    q.append((i, i, i))

  while q:
    p, s, h = q.popleft()
    if p > k or s > k: continue
    if p == s:


def main(args):
  print(compute(k))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-k', type=int, default=10)
  args = parser.parse_args()
  main(args)
