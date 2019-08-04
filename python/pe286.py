from decimal import Decimal, getcontext
from functools import lru_cache

getcontext().prec = 15

TARGET = Decimal(0.02)
EPS = 1e-15

@lru_cache(maxsize=50*20+100)
def P(i, s, q):
  if i == 0: return Decimal(s == 0)
  if s < 0: return Decimal(0)
  return P(i-1, s-1, q) + (i/q)*(P(i-1, s, q) - P(i-1, s-1, q))


if __name__ == '__main__':
  Pr = lambda q: P(50, 20, q)

  lo = Decimal(50)
  hi = Decimal(55)

  while True:
    q = (lo + hi) / 2
    p = Pr(q)
    print(p, q)

    if abs(p - TARGET) < EPS:
      print(q, p)
      break
    elif p < TARGET:
      hi = q
    else:
      lo = q

