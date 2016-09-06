# a couple of seconds
from math import sqrt
LIMIT = 100000000
def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
a = {i:True for i in primes_sieve2(LIMIT)}
def is_prime(n):
    return n in a
def check(n):
    if not is_prime(n+1): return False
    lim = int(sqrt(n))
    d = 2
    while d <= lim:
        if n%d == 0:
            a, b = n//d, d
            # print(d, n//d)
            if not is_prime(n//d+d): return False
        d += 1
    #print(n, n//(d-1), (d-1))
    return True
print(1+sum(list(filter(check, range(2, LIMIT, 4)))))