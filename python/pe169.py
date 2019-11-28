import sys

from functools import lru_cache

y = int(sys.argv[1])
N = y # 2 ** y

@lru_cache(maxsize=None)
def W(n, i, t):
  if t > 2 or n > N: return 0
  if n == N: return 1
  if 2 ** i > N: return 0
  return W(n+2**i, i, t+1) + W(n, i+1, 0)


'''
def Q(n):
  def _Q(bs, i):
    if 

  bs = list(map(int, bin(n)[2:]))
  return _Q(bs, 0)
'''


if __name__ == '__main__':
  ans = W(0, 0, 0)
  print(ans)
