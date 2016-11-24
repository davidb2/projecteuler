MOD = 250
LIMIT = 250250

cache = {}

def ways(arr, i, k):
    if i == len(arr)-1:
        return k if arr[i][0] == k else 0
    elif (i, k) not in cache:
        ans = 0
        for x in xrange(i+1, len(arr)):
            ans += ways(arr, x, (MOD - k) % MOD)
        cache[(i, k)] = ans
    return cache[(i, k)]

        




d = {}
arr = [pow(x, x, MOD) for x in xrange(1, LIMIT)]

for x in arr:
    if x not in d:
        d[x] = 0
    d[x] += 1

arr = sorted(d.items())
ans = 0
for x in xrange(len(arr)):
    ans += 

