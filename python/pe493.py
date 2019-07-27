import random

from decimal import Decimal, getcontext
from functools import lru_cache

@lru_cache(maxsize=None)
def f(n):
  if n <= 1: return 1
  return n * f(n-1)


@lru_cache(maxsize=None)
def C(n, k):
  if k > n or n < 0 or k < 0: return 0
  return f(n) / f(k) / f(n-k)


def E(colors):
  num = sum(c*C(Decimal(colors),c)*C(10*colors, 20)*C(Decimal(20)-1,c-1) for c in range(2,colors+1))
  denom = sum(C(Decimal(colors),c)*C(Decimal(20)-1,c-1) for c in range(2,colors+1))
  return num / denom

def sim(colors):
  turns = 100000
  ans = 0
  for _ in range(turns):
    cs = [c for c in range(colors)] * 10
    random.shuffle(cs)
    s = set()
    for _ in range(20):
      i = random.randint(0, len(cs)-1)
      s.add(cs[i])
      del cs[i]
    ans += len(s)
  return ans / turns



if __name__ == '__main__':
  print(E(7))
  print(sim(7))
