import numpy as np
import sys

from collections import defaultdict
from functools import lru_cache
from itertools import chain, combinations, permutations

RANGE = tuple(range(1, 9+1))

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

def num(pp):
  return sum(10**i*x for i, x in enumerate(pp[::-1]))

def primes():
  for choose in RANGE:
    for pp in chain.from_iterable([permutations(xs) for xs in combinations(RANGE, choose)]):
      if isPrime(num(pp)):
        yield pp

d = defaultdict(set)
A = []
for pp in primes():
  d[len(pp)].add(pp)
  A.append(pp)

A.sort(key=lambda x: num(x))

# @lru_cache(maxsize=None)
used = [0]*9
W = [0]*(len(A)+1)
W[-1] = 1

for i in reversed(range(len(A))):
def ways(i):
  print(used)
  if i == len(A): return int(all(used))

  ai = set(A[i])
  skip = ways(i+1)
  take = 0
  if all(not used[x-1] for x in A[i]):
    for x in A[i]:
      used[x-1] = True
    take = ways(i+1)
    for x in A[i]:
      used[x-1] = False

  return skip + take


if __name__ == '__main__':
  ans = ways(0)
  print(ans)
