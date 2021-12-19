
from functools import lru_cache
from math import comb
d = 10

def sat(k, l, r, z):
  return 1 <= r <= min(k, d) and z in (0, 1)

@lru_cache(maxsize=None)
def w(k, r, z, dd, start):
  if k == 0:
    return r == 0 and (0 in dd if z else 0 not in dd)

  assert k > 0

  ans = 0
  for digit in range(start, d):
    if digit in dd:
      ans += w(k-1, r, z, dd, start=0)
    else:
      ans += w(k-1, r-1, z, dd | {digit}, start=0)
  return ans

def W(k, r, z):
  return w(k, r, z, frozenset(), start=1)



"""
def g(k, l, r, z):
  return comb(d-1, r-z) * (r-z)*r**(k-1) * (d-r-(1-z))*(d-r)**(l-1)
"""

def g(k, l, r, z):
  return W(k, r, z) * (d-r-(1-z))*(d-r)**(l-1)

def G(n):
  return sum(
    g(k, l, r, z)
    for k in range(1, n+1)
    for l in range(1, n+1)
    for r in range(1, d+1)
    for z in (0, 1)
    if sat(k, l, r, z)
  )

def f(n):
  return ((d**n-1)**2 - G(n) - (d**n-1)) // 2

def friends(p, q):
  px = set(str(p))
  qx = set(str(q))
  return len(px.intersection(qx)) > 0

def fp(n):
  return sum(
    friends(p, q)
    for p in range(1, d**n)
    for q in range(p+1, d**n)
  )


if __name__ == '__main__':
  print(f(18) % 1000267129)
