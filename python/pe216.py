from functools import lru_cache

LIMIT = 100000 # 50000000

def sieve(n):
  p = [True] * (n+1)
  p[0] = p[1] = False

  for d in range(2, n+1):
    if p[d]: yield d
    for dp in range(d**2, n+1, d):
      p[dp] = False

def t(n):
  return 2*n**2-1

PRIMES = set(sieve(10+int((2*LIMIT**2-1)**0.5)))
@lru_cache(maxsize=None)
def isPrime(n):
  return all(n % p != 0 or n == p for p in PRIMES)

if __name__ == '__main__':
  ans = sum(1 for n in range(2, LIMIT+1) if isPrime(t(n)))
  print(ans)
