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

def isqrt(n):
  lo = 1
  hi = n
  while True:
    mid = (lo + hi)//2
    mmid = mid * mid
    if mmid == n: return mid
    if hi == mid or lo == mid: return mid
    elif mmid > n:
      hi = mid
    elif mmid < n:
      lo = mid
  return None

EPS = 1e-6
def iss(x):
  # return x.as_integer_ratio()[1] == 1
  return x % 1 == 0
  # return abs(round(x) - x) < EPS
  # return isqrt(n)**2 == n

from decimal import Decimal, getcontext
getcontext().prec = 20

def sat(a, b, c):
  s = (a+b+c)/Decimal(2)
  area = s.sqrt()*(s-a).sqrt()*(s-b).sqrt()*(s-c).sqrt()
  # return area
  return iss(area)

def main(args):
  # aa = LIMIT//3+1
  # LIM = heron(aa, aa, aa+1)
  s = 0
  for a in range(1, LIMIT//3+2, 2):
    # if a % int(1e8) == 0:
    #  print(a)
    if 2*a > a+1 and 3*a+1 <= LIMIT and sat(a, a, a+1):
      print(a, a, a+1)
      s += 3*a+1
    if 2*a > a and 3*a <= LIMIT and sat(a, a, a):
      print(a, a, a)
      s += 3*a
    if a-1 > 0 and 3*a-1 <= LIMIT and sat(a, a, a-1):
      print(a, a, a-1)
      s += 3*a-1
  print('ans: {}'.format(s))
  #   print(a, (4*a)**2)
  #   # area = heron(a, a, a+1)
  #   # if isNat(area):
  #     # print(a, a, a+1, area)



if __name__ == '__main__':
  main(None)
  # ans = 0
  # for x in squares():
  #   ss = sol(x)
  #   if ss:
  #     ans += sum(map(sum, ss))
  #     print(ss, x)
  #     print(ans)
