from math import sqrt
cache = [
    [0],
    [0] + [0],
    [0] + [1, 1]
]
primes = {0: False, 1: False, 2: True, 3: True}
def is_prime(n):
    if n not in primes:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                primes[n] = False
                return False
        primes[n] = True
    return primes[n]

# swal = starts with at least
def calculate(n):
    if cache[n] == []:
        ip = int(is_prime(n))
        cache[n] = [0] + [ip for i in range(n)]
        acc = ip
        for swal in reversed(range(1, n//2+1)):
            remainder = n - swal 
            if cache[remainder] == []:
                calculate(remainder)
            cache[n][swal] = cache[remainder][swal] + acc if is_prime(swal) else acc
            acc += cache[remainder][swal] if is_prime(swal) else 0
def partitions(n):
    for i in range(len(cache), n+1):
        cache.append([])
    calculate(n)
    return cache[n][1] - int(is_prime(n))

pat = partitions(3)
n = 4
while pat < 5000:
    pat = partitions(n)
    n += 1
print(n-1)