#!/usr/bin/env python3.6
import math

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import islice


def gen(n):
  a = Decimal(int(n))
  yield int(a)
  yield from gen(1 / (n - a))


def cf(n):
  '''
  [a0; a1, a2, ..., a_{r+1}]
  '''
  g = gen(n)

  a0 = next(g)
  ar = math.inf
  ans = [a0]
  while ar != 2*a0:
    ar = next(g)
    ans.append(ar)
  return ans


def extend(n):
  a = cf(Decimal(n))
  assert len(a) > 1

  i = 0
  while True:
    yield a[i]
    i = (i + 1) % len(a)
    if i == 0:
      i += 1


def cg(n):
  g = extend(n)
  a = []
  for _ in range(2):
    a.append(next(g))

  ps = [a[0], a[0] * a[1] + 1]
  qs = [1, a[1]]

  yield ps[0], qs[0]
  yield ps[1], qs[1]

  n = 2
  while True:
    an = next(g)
    pn = an * ps[n-1] + ps[n-2]
    qn = an * qs[n-1] + qs[n-2]
    yield pn, qn
    ps.append(pn)
    qs.append(qn)
    a.append(an)
    n += 1


def sols(n):
  yield from cg(Decimal(n).sqrt())


def best(D):
  print(D)
  return list(islice((x for (x, y) in sols(D) if x**2 - D*y**2 == 1), 1))[0]

if __name__ == '__main__':
  getcontext().prec = 1000
  print('Ans:', max([x for x in range(2, 1000+1) if int(x**0.5)**2 != x], key=best))
