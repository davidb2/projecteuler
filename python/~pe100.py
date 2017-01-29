from __future__ import division
from math import sqrt, floor
from fractions import Fraction

def is_triangular_num_times_two(n):
    ans = (1 + sqrt(1 + 4*n)) / 2
    if ans == floor(ans):
        return True, int(ans)
    else:
        return False, None

def nth_triangular_number(n):
    return (n * (n - 1)) // 2



for a in xrange(10**12, 10**13):
    itntt, x = is_triangular_num_times_two(nth_triangular_number(a))
    if itntt and Fraction(x, a) * Fraction(x-1, (a-1)) == Fraction(1/2):
        print '{}/{} * {}/{} = 1/2'.format(x, a, x-1, a-1) 
        print Fraction(x, a) * Fraction(x-1, (a-1))
        break