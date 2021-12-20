from math import comb

def I(n, s, l):
  return sum(
    s <= l <= n-s and s <= c <= l-s
    for c in range(0, l+1)
  )


def G(n, s):
  return sum(I(n, s, l) for l in range(0, n+1))

def H(n):
  return sum(G(n, s) for s in range(1, n+1))
