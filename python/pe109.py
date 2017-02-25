cache = {}
pcache = {}
tcache = {}

def tways(n):
    if n not in tcache:
        tcache[n] = n*(n+1)//2
    return tcache[n]

def pways(n):
    if n not in pcache:
        if n < 0 or 60 < n:
            return 0
        if n == 0 or n == 25 or n == 50:
            return 1
        ans = 0
        if n % 2 == 0 and n // 2 <= 20:
            ans += 1
        if n % 3 == 0 and n // 3 <= 20:
            ans += 1 
        pcache[n] = ans + int(0 <= n <= 20)
    return pcache[n]


def split(n):
    if n == 0: return 1
    elif n not in cache:
        ans = 0
        for i in xrange(n//2+1):
            if i == n-i:
                ans += tways(pways(i))
            else:
                ans += pways(i)*pways(n-i)
        cache[n] = ans
    return cache[n]


def ways(n):
    return sum(map(split, filter(lambda t: t >= 0, map(lambda s: n-s, range(2, 40+2, 2)+[50]))))

N = 100
ans = sum(map(ways, range(1, N)))
print ans