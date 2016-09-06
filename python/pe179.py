LIMIT = 10000000

primes = [2 for i in range(LIMIT)] # not really primes
def psieve(limit):
    primes[0] = 0
    primes[1] = 1
    primes[2] = 2
    for step in range(2, limit//2+1):
        for i in range(2*step, limit, step):
            primes[i] += 1
psieve(LIMIT)

ans = 0
for i in range(1, len(primes)):
    if primes[i-1] == primes[i]:
        ans += 1
print(ans)