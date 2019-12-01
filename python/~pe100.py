from __future__ import division
from math import sqrt, floor
from fractions import Fraction

'''
Pattern found: https://oeis.org/search?q=4%2C21%2C120%2C697&language=english&go=Search
a(n) = 6*a(n-1) - a(n-2) - 2, n >= 2, a(0) = 1, a(1) = 4.
'''

def is_triangular_num_times_two(n):
    ans = (1 + sqrt(1 + 4*n)) / 2
    if ans == floor(ans):
        return True, int(ans)
    else:
        return False, None

def nth_triangular_number(n):
    return (n * (n - 1)) // 2

def search():
  for a in xrange(2,10**12):
      itntt, x = is_triangular_num_times_two(nth_triangular_number(a))
      if itntt and Fraction(x, a) * Fraction(x-1, (a-1)) == Fraction(1/2):
          print '{}/{} * {}/{} = 1/2'.format(x, a, x-1, a-1)
          print Fraction(x, a) * Fraction(x-1, (a-1))

n = 2
n1, n2 = 4, 1
while True:
  n1, n2 = 6*n1-n2-2, n1
  if n1 > 10**12:
    a = n1
    print(a)
    itntt, x = is_triangular_num_times_two(nth_triangular_number(a))
    if itntt and Fraction(x, a) * Fraction(x-1, (a-1)) == Fraction(1/2):
        print '{}/{} * {}/{} = 1/2'.format(x, a, x-1, a-1)
        print Fraction(x, a) * Fraction(x-1, (a-1))
    break
  n += 1