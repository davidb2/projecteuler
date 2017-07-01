LIMIT = 190
primes = []
def psieve():
    ps = [True for _ in xrange(LIMIT+1)]
    ps[0] = ps[1] = False
    for step in xrange(3, (LIMIT // 2) + 1, 2):
        if ps[step]:
            for p in xrange(step * step, LIMIT+2, 2 * step):
                ps[p] = False
    primes.append(2)
    for i in xrange(3, LIMIT+1, 2):
        if ps[i]:
            primes.append(i)

def get_divisors(ps, i=0):
    if i == len(ps): return [1]
    xs = get_divisors(ps, i=i+1)
    xxs = [ps[i] * x for x in xs]
    return xs + xxs 

def psr(num):
    last = None
    for i in xrange(1, num+1):
        if num % i == 0:
            if last is not None and i > (num ** 0.5):
                return last
            last = i
    return last
print map(lambda x: (x, psr(x)), range(1, 100))