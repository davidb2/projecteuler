#!/usr/bin/env python3.6
import argparse
import sys
import threading

from functools import lru_cache

B = 10
MOD = 10**9 + 7

def K(d):
  ans = 0
  for n in range(10**d):
    s = str(n)
    xs = [int(s[i:j]) for i in range(len(s)) for j in range(i+1, len(s)+1)]
    # print(n, xs)
    r = sum(int(x%3==0) for x in xs)
    if r % 3 == 0:
      ans += 1
  return ans

def F(d):
  return K(d)-K(d-1)

def shift(S, d):
  assert d >= 0, d
  if d == 0: return S
  return shift((S[-1],)+S[:-1], d-1)

@lru_cache(maxsize=None)
def phi(d, S):
  assert d in {0, 1, 2}
  Sp = list(shift(S, d))
  Sp[d] = (Sp[d]+1)%3
  return tuple(Sp)

def add(A, B):
  assert len(A) == len(B), (len(A), len(B))
  return tuple((a+b)%3 for a, b in zip(A, B))

def G(N):
  @lru_cache(maxsize=None)
  def g(n=0, S=(0, 0, 0), T=(0, 0, 0)):
    if n >= N: return int(T[0] == 0)

    ans = 0
    for d in range(int(n == N-1), B):
      Sp = phi(d%3, S)
      ans = (ans + g(n+1, S=Sp, T=add(Sp, T))) % MOD
    return ans
  return g()

def main(args):
  print(G(args.N))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-N', type=int, default=10**5)
  args = parser.parse_args()

  # ulimit -s 1048576
  sys.settrace(lambda *_: None)
  sys.setrecursionlimit(1<<30)
  thread = threading.Thread(target=main, args=(args,))
  thread.start()
  thread.join()

  # I needed more stack memory than my default 8192 KB.
  # I used a little more than 1 GB stack space to run this.
