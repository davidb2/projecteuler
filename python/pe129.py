def sieve(limit):
  p = [True]*(limit+1)
  p[0] = p[1] = False

  for d in range(2, limit+1):
    if not p[d]: continue

    yield d
    for dd in range(d*d, limit+1, d):
      p[dd] = False

def f(r, k, m):
  if k == 0: return 1

  r2 = pow(r, 2, m)
  if k % 2 == 0:
    return (1 + (r + r2) * f(r2, (k-2)//2, m)) % m
  else:
    return ((1+r) * f(r2, (k-1)//2, m)) % m

def nextf(xn, n, k, m):
  # a^(b^c) = a^(b^c % phi(p)) (mod p) if p is prime.
  return (xn * f(pow(10, pow(10, n, m-1), m), k-1, m)) % m

def divides(d, x, n, seen):
  if d % 2 == 0: return False
  while True:
    if x == 0: return True
    if x in seen: return False
    seen.add(x)
    x = nextf(x, n, 10, d)
    n += 1

if __name__ == '__main__':
  LIMIT = 100000
  ans = [p for p in sieve(LIMIT) if not divides(p, 1, 0, set())]
  print(ans)
  print(sum(ans))

