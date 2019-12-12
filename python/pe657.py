import gmpy
from functools import reduce

'''
# Complete words = sum_{k=0}^n of [x^k/k!](e^x-1)^a   (exp. gen. series).
# Words = 1+a+a^2+a^3+...+a^n = (a^(n+1)-1)/(a-1).
# Incomplete words = # Words - # Complete words
'''

def mulp(a,b,p): return (a*b)%p

def gp(j,n,p):
  return (n+1 if j == 1 else mulp(pow(j,n+1,p)-1, gmpy.invert(j-1,p), p))%p

def calc(a,n,p):
  binom = [1]*(a+1)
  for k in range(a):
    binom[k+1] = mulp(mulp(binom[k], (a-k), p), gmpy.invert(k+1,p), p)

  return (gp(a,n,p)-reduce(lambda x,y: (x+y)%p, (
    mulp(mulp(binom[j], gp(j,n,p), p), pow(-1,a-j,p), p)
    for j in range(a+1)), 0
  ))%p
