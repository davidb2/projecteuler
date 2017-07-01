LIMIT = 10**7
digits = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:4, 8:7, 9:6}
trans = {
    0 : set([0, 1, 2, 3, 4, 6]),
    1 : set([0, 3]),
    2 : set([0, 2, 4, 5, 6]), 
    3 : set([0, 3, 4, 5, 6]),
    4 : set([0, 1, 3, 5]),
    5 : set([1, 3, 4, 5, 6]),
    6 : set([1, 2, 3, 4, 5, 6]),
    7 : set([0, 1, 3, 4]),
    8 : set([0, 1, 2, 3, 4, 5, 6]),
    9 : set([0, 1, 3, 4, 5, 6])
}
sam_cache = {}
max_cache = {}
def S(n):
    return sum(map(int, str(n)))

def sam_transition_cost(n):
    return sum(map(lambda x: digits[x], map(int, str(n))))

def sam_transition(start):
    if start < 10:
        return 2 * digits[start]
    elif start not in sam_cache:
        sam_cache[start] = 2 * sam_transition_cost(start) + sam_transition(S(start))
    return sam_cache[start]

def max_transition_cost(start, end):
    ans = 0
    sstart = str(start)
    send   = str(end)
    for i in xrange(len(send)):
        ans += len(trans[int(sstart[i])] - trans[int(send[i])])
    for i in xrange(len(send), len(sstart)):
        ans += digits[int(sstart[i])]
    return ans

def similar(start, end):
    ans = 0
    sstart, send = str(start), str(end)
    for i in xrange(len(send)):
        ans += len(trans[int(send[i])]) - len(trans[int(send[i])] - trans[int(sstart[i])]) 
    return ans

def max_transition(start):
    if start < 10:
        return 2 * digits[start] 
    elif start not in max_cache:
        light_up = sam_transition_cost(start)
        next_number = S(start)
        light_down = max_transition_cost(start, next_number)
        residue = similar(start, next_number)
        max_cache[start] = light_up + light_down - residue + max_transition(next_number)
    return max_cache[start]

from math import sqrt
RANGE = 10**7, 2*10**7

def sieve():
    lim = int(sqrt(RANGE[~0]))+1
    ps = [True for _ in xrange(lim)]
    ps[0] = ps[1] = False
    for step in xrange(3, lim, 2):
        if ps[step]:
            for p in xrange(step * step, lim, step):
                ps[p] = False
    primes = [2]
    for i in xrange(3, len(ps), 2):
        if ps[i]:
            primes.append(i)
    return set(primes)

primes = sieve()

def is_prime(n):
    if n < 2:
        return False
    if n in primes:
        return True
    for p in primes:
        if n % p == 0:
            return False
    return True

def prange(start, end):
    for p in xrange(start, end+1):
        if is_prime(p):
            yield p

sam_ans = 0
max_ans = 0

for p in prange(RANGE[0], RANGE[~0]):
    sam_ans += sam_transition(p)
    max_ans += max_transition(p)

print sam_ans, max_ans, sam_ans - max_ans