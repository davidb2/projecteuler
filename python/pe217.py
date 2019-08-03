#!/usr/bin/env python3.6
import argparse

from functools import lru_cache

BASE = 10
MOD = 3 ** 15

'''
def S(n):
  ans = 0
  for x in range(BASE**n):
    s = str(x)
    e = len(s) % 2
    if sum(map(int, s[:len(s)//2+e])) == sum(map(int, s[len(s)//2:])):
      ans += x
  return ans

def Lr(n, d):
  ans = 0
  num = 0
  for x in range(BASE**d):
    s = str(x)
    if len(s) == d and s[0] != '0' and sum(map(int, s)) == n:
      print(x)
      num += 1
      ans += x
  return ans, num

def Rr(n, d):
  ans = 0
  num = 0
  for x in range(BASE**d):
    s = str(x)
    if sum(map(int, s)) == n:
      num += 1
      ans += x
  return ans, num


def C(k, d):
  ans = 0
  for x in range(BASE**d):
    s = str(x)
    e = len(s) % 2
    if len(s) == d and s[0] != '0' and k == sum(map(int, s[:len(s)//2+e])) == sum(map(int, s[len(s)//2:])):
      ans += x
  return ans
'''


@lru_cache(maxsize=None)
def L(n, d):
  if n == 0 and d == 0: return (0, 1)
  if n == 0 or d == 0: return (0, 0)

  ans, num = 0, 0
  for x in range(min(BASE, n+1)):
    if x == 0 and d == 1: continue
    anst, numt = L(n-x, d-1)
    if numt == 0: continue
    ans += x * numt + BASE * anst
    num += numt

  return (ans, num)


@lru_cache(maxsize=None)
def R(n, d):
  if n == 0 and d == 0: return (0, 1)
  if d == 0: return (0, 0)

  ans, num = 0, 0
  for x in range(min(BASE, n+1)):
    anst, numt = R(n-x, d-1)
    if numt == 0: continue
    ans += BASE ** (d-1) * (x * numt) + anst
    num += numt
  return (ans, num)


def T(n):
  if n == 0: return 0
  ans = 0

  if n % 2 == 0:
    for k in range(1+(BASE-1)*(n//2)):
      ansl, numl = L(k, n // 2)
      ansr, numr = R(k, n // 2)
      adding = BASE ** (n // 2) * numr * ansl + numl * ansr
      ans += adding
  elif n % 2 == 1:
    for k in range(1+(BASE-1)*(n//2)):
      for d in range(BASE):
        ansl, numl = L(k, n // 2)
        ansr, numr = R(k, n // 2)
        ansl = BASE * ansl + numl * d
        adding = BASE ** (n // 2) * numr * ansl + numl * ansr
        ans += adding
  return ans + T(n-1)


def main(args):
  n = args.n
  print(T(n) % MOD)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', type=int, required=True)
  args = parser.parse_args()
  main(args)

