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
a = list(primes_sieve2(LIMIT))
len_a = len(a)
ans = 0
xp = 0
rlim = int(sqrt(LIMIT))+1
def binary_search(x, val):
    i, j = 0, len_a
    while True:
        mid = (i + j)//2
        if j-i < 1:
            if a[i] <= val:
                return (mid-x)+1
            else:
                return (mid-x)
        elif a[mid] < val:
            i = mid + 1
        else:
            j = mid
while a[xp] < rlim:
    temp_ans = binary_search(xp, (LIMIT-1)//a[xp])
    if temp_ans == None:
        print('ERROR')
    else:
        ans += temp_ans
    xp += 1
print(ans)