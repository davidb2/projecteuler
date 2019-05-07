#!/usr/bin/env python3.6
import argparse
import functools
import itertools
import operator as op

from collections import defaultdict


def evaluatePostfix(xs):
  ss = []
  for x in xs:
    if type(x) is int:
      ss.append(x)
    elif len(ss) > 1:
      a = ss.pop()
      b = ss.pop()
      try:
        ss.append(x(a, b))
      except ZeroDivisionError as e:
        return None
    else:
      return None
  if len(ss) != 1:
    return None
  return ss[0]

@functools.lru_cache(maxsize=None)
def compute():
  strides = defaultdict(set)
  for i, (a, b, c, d) in enumerate(itertools.combinations(range(1, 10), 4)):
    sabcd = f'{a}{b}{c}{d}'
    for op1, op2, op3 in itertools.combinations_with_replacement((op.add, op.sub, op.mul, op.truediv), 3):
      for xs in itertools.permutations((a, b, c, d, op1, op2, op3)):
        ans = evaluatePostfix(xs)
        if ans is not None:
          strides[sabcd].add(ans)
  return strides

def main(args):
  strides = compute()
  ms, mi = None, 0
  for sabcd, anss in strides.items():
    i = 1
    while i in anss:
      i += 1
    if i > mi:
      mi = i
      ms = sabcd

  print(ms, mi)



if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', type=int, default=4)
  args = parser.parse_args()
  main(args)
