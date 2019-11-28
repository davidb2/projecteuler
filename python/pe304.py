import numpy as np

MOD = 1234567891011

def mulm(A, B, m):
  return [
    [((A[0][0]*B[0][0])%MOD+(A[0][1]*B[1][0])%MOD)%MOD, ((A[0][0]*B[0][1])%MOD+(A[0][1]*B[1][1])%MOD)%MOD],
    [((A[1][0]*B[0][0])%MOD+(A[1][1]*B[1][0])%MOD)%MOD, ((A[1][0]*B[0][1])%MOD+(A[1][1]*B[1][1])%MOD)%MOD],
  ]

def mpown(A, n, m):
  if n == 0: return np.eye(A.shape[0], dtype=np.uint64)

  bs = []
  while n > 0:
    bs.append(n)
    n //= 2

  p = A
  for i in range(1, len(bs)):
    h = p
    q = mulm(h, h, MOD)
    if bs[len(bs)-i-1] % 2 == 1:
      q = mulm(q, A, MOD)
    p = q
  return p

def isPrime(n):
  '''Miller-Rabin'''
  if n < 2: return False
  if n % 2 == 0: return n == 2
  if n == 3: return True

  d = n-1
  r = 0
  while d % 2 == 0:
    d //= 2
    r += 1

  k = 10
  for _ in range(k):
    a = np.random.randint(2, n-1)
    x = pow(a, d, n)
    if x == 1 or x == n - 1: continue
    for _ in range(r-1):
      x = pow(x, 2, n)
      if x == n-1: break
    else:
      return False
  return True


def fib(n):
  F = [[1,1],[1,0]]
  return mpown(F, n, MOD)[0][1]


if __name__ == '__main__':
  b = 0
  ans = 0
  n = 10**14 + 1
  while b < 100000:
    if not isPrime(n):
      n += 2
      continue

    ans = (ans + fib(n)) % MOD
    # print(n)
    b += 1
    n += 2

  print(ans)
