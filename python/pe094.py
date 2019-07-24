import math

LIMIT = 10 ** 9

def squares():
  i = 1
  q = i ** 2
  while True:
    yield q
    q += 2*i+1
    i += 1

def isNat(x):
  return x >= 0 and math.floor(x) == math.ceil(x)

def roots(a, b, c):
  d = math.sqrt(b**2 - 4*a*c)
  return ((-b+d)/(2*a), (-b-d)/(2*a))

def isPerfectSquare(n):
  return int(math.sqrt(n)) ** 2 == n

def sol(x):
  '''
  x = (3s+1)(s-1) ?
  x = (3s-1)(s+1) ?
  '''
  s1, s2 = roots(3, -2, -1-x)
  ss1 = []
  for s in (s1, s2):
    y = (3*s+1)*(s-1)
    if isNat(s) and isPerfectSquare(y) and (y % 2 == 0 or s % 4 == 0):
      ss1.append((s, s, s+1))

  s3, s4 = roots(3, +2, -1-x)
  ss2 = []
  for s in (s3, s4):
    y = (3*s-1)*(s+1)
    if isNat(s) and isPerfectSquare(y) and (y % 2 == 0 or s % 4 == 0):
      ss2.append((s, s, s-1))

  return ss1 + ss2


def A(s, t):
  b = t / 2.
  h = (s**2 - b**2) ** 0.5
  return b*h/2.


def P(s, t):
  return 2*s + t


if __name__ == '__main__':
  ans = 0
  for x in squares():
    ss = sol(x)
    if ss:
      ans += sum(map(sum, ss))
      print(ss, x)
      print(ans)
