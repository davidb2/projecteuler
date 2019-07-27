#!/usr/bin/env python3.6
import argparse

from decimal import Decimal, getcontext

TARGET = -600000000000
EPS = 1e-12

def u(k, r):
  return (900-3*k)*r**(k-1)

def s(n, r):
  return sum(u(k, r) for k in range(1, n+1))

if __name__ == '__main__':
  getcontext().prec = 40
  lo = Decimal(0)
  hi = Decimal(2)
  while True:
    mid = (lo + hi) / 2
    ans = s(5000, mid)
    print(ans)
    if abs(ans - TARGET) < EPS:
      print(mid)
      break
    elif ans > TARGET:
      lo = mid
    else:
      hi = mid
