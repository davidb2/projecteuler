from math import sqrt
# the product of these primes is just smallest 
# under 10^9
ps = [2, 3, 5, 7, 11, 13, 17, 19]

LIMIT = 10**9

def sieve():
    pprimes = [True for _ in xrange(int(sqrt(LIMIT)) + 1)]
    pprimes[0] = pprimes[1] = False
    for step in xrange(3, len(pprimes), 2):
        if pprimes[step]:
            for p in xrange(step * step, len(pprimes), 2 * step):
                pprimes[p] = False
    return [2] + [i for i in xrange(3, len(pprimes)) if pprimes[i]]

primes = sieve()

def is_prime(n):
    if n < 2: return False
    for d in primes:
        if n % d == 0 and n != d:
            return False
    return True

def admissable(i=0, curr_prod=2, xs=[]):
    if curr_prod < LIMIT:
        xs.append(curr_prod)
        admissable(i, curr_prod*ps[i], xs)
        if i != len(ps) - 1:
            admissable(i+1, curr_prod*ps[i+1], xs)

ns = []
admissable(xs=ns)
p_fortunate = set()

for n in ns:
    m = 3
    while not is_prime(n + m):
        m += 2
    p_fortunate.add(m)
print sum(p_fortunate)