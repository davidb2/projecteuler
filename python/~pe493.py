# def ans()

# div = 70!/50!

# P(0) = 0
# P(1) = 0
# P(2) = ((7 pick 2) * (10!)^2) / div
# P(3) = 

from random import randint
COLORS = 7
PICKS = 20
#def sim():
#    balls_selected = set()
#    balls = [x // COLORS for x in range(COLORS * 10)]
#   for _ in range(PICKS):
#        i = randint(0, len(balls)-1)
#        balls_selected.add(balls[i])
#        del balls[i]
#    return float(len(balls_selected))
#
#dis = 0.0  
#count = 0.0
#MOD = 100000
#while True:
#    dis += sim()
#    count += 1.0
#    if int(count) % MOD == 0:
#        print(dis/count)

from functools import reduce
from fractions import Fraction
from sys import setrecursionlimit
setrecursionlimit(1 << 30)

SUM = Fraction(0, 1)
N = 7

BUCKETS = 20

cache = {}

def fact(n):
    if n < 2:
        return 1
    elif n not in cache:
        cache[n] = n * fact(n-1)
    return cache[n]

DENOM = fact(10*N)//fact(10*N - BUCKETS)

# start at; go to (down)
def sagt(n, k):
    return reduce(lambda x, y: x*y, range(k, n+1))

def nCr(n, r):
    return fact(n) // (fact(r) * fact(n-r))

def all_sets(k, n):
    sets = set()
    def ways(np, acc=[]):
        if sum(acc) > n:
            return
        if np == 0:
            if sum(acc) == n:
                sets.add(tuple(acc))
        else:
            for i in range(1 if np==k else acc[~0], n//2+1):
                ways(np-1, acc+[i])
    ways(k)
    #print(sets)
    return sets

power_set = [set() for x in range(N+1)]
for i in range(1, N+1):
    power_set[i] = all_sets(i, BUCKETS)

bucket = [0 for x in range(N+1)]

for i in range(len(power_set)):
    for s in power_set[i]:
        ls = list(s)
        #print(ls)
        ps = reduce(lambda x, y: x*y, [sagt(10, 10-e+1) for e in ls]) 
        #print(ps)
        num = BUCKETS
        bs = []
        for j in range(len(ls)):
            bs.append(nCr(num, ls[j]))
            num -= ls[j]
        print(ls)
        print(bs)
        bbs = reduce(lambda x, y: x*y, bs)
        print(bbs)
        print(bbs * ps)
        print(DENOM)
        tot = (bbs * ps) 
        #print(bs, bbs, ps, DENOM)
        #print(tot)
        print()
        bucket[i] += tot
    x = Fraction(bucket[i], DENOM)
    bucket[i] = x
    SUM += x

# normalize
for i in range(len(bucket)):
    bucket[i] /= SUM

exp_val = 0
print(bucket)
for x in range(N+1):
    exp_val += x * bucket[x]

from decimal import Decimal, getcontext
getcontext().prec = 10
d = Decimal(exp_val.numerator) / Decimal(exp_val.denominator)

print(exp_val, float(exp_val), d)