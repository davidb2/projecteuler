### THIS CODE IS A WORK IN PROGRESS ###
# import math
# from math import floor
# from decimal import *
# getcontext().prec = 10
# def next_period_int(n, acc, first):
#     m = floor(n)
#     x = 1 / (n - m)
#     #print(m, x, cache)
#     #input()
#     if m == first and len(acc) > 0:
#         return acc + [m]
#     else:
#         print(m, '!=', first)
#         return next_period_int(x, acc + [m], first)
# def period(n):
#     # print('\n', n)
#     try:
#         np = next_period_int(Decimal(n).sqrt(), [], floor(Decimal(n).sqrt()))
#         print(n, np)
#         input()
#         return np
#     except:
#         print(n, 'failed')
#         input()
# def plen(n):
#     return len(period(n))-2
# def is_not_perfect_square(n):
#     return n != floor(math.sqrt(n)) ** 2

# from sys import argv
# # print(*filter(is_not_perfect_square, range(2, int(argv[1]))))
# a = list(map(plen, filter(is_not_perfect_square, range(2, 1+int(argv[1])))))
# print(len(list(filter(lambda x: x % 2 == 1, a))))
# print(a)
# # print(period(76))


class Irrational:
    def __init__(self, rational, irrational):
        self.rational = rational
        self.irrational = irrational
        self.value = self.rational + self.irrational
    def __mul__(self, other):
        # FOIL, futhermore, we know we are dealing with the multiplicative conjugate
        rat = round(self.irrational * other.irrational) + self.rational * other.rational
        irr = self.irrational * other.rational + self.rational * other.irrational
        return Irrational(rat, irr) 
    def __add__(self, other):
        rat = self.rational + other.rational
        irr = self.irrational + other.irrational
        return Irrational(rat, irr)
    def __lt__(self, other):
        return self.value < other.value
    def __gt__(self, other):
        return self.value > other.value
    def __str__(self):
        return str(self.rational) + " + √" + str(round(self.irrational**2))

class Fraction:
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom
    def __add__(self, other):
        # we know these fractions will never have the same denom
        a = (self, other)[self.denominator < other.denominator]
        b = (self, other)[self.denominator > other.denominator]
        b.numerator *= a.denominator
        num = a.numerator +  b.numerator
        denom = a.denominator
        return Fraction(num, denom)
    def __str__(self):
        return "(" + str(self.numerator) + ") / (" + str(self.denominator) + ")"

from math import sqrt

a = Fraction(Irrational(3, sqrt(14)), Irrational(5, 0))
b = Fraction(Irrational(-1, 0), Irrational(1, 0))
print(a + b)
print(Irrational(3, sqrt(14)) + Irrational(-5, 0))
c = Irrational(5, 0)
d = Irrational(2, sqrt(14))
print (c * d)