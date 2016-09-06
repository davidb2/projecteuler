i_cache = {}
def inc(d, n):
    if n == 0: 
        return 1
    if n not in i_cache:
        i_cache[n] = {}
    if d not in i_cache[n]:
        ans = 0
        for x in range(d, 10):
            ans += inc(x, n-1)
        i_cache[n][d] = ans
    return i_cache[n][d]
d_cache = {}
def dec(d, n):
    if n == 0: 
        return 1
    if n not in d_cache:
        d_cache[n] = {}
    if d not in d_cache[n]:
        ans = 0
        for x in range(d+1):
            ans += dec(x, n-1)
        d_cache[n][d] = ans
    return d_cache[n][d]
MAX_DIGITS = 100
ans = 0
for d in range(MAX_DIGITS):
    for x in range(1, 10):
        ans += inc(x, d)
        ans += dec(x, d)
    ans -= 9 # remove duplicates (ie. 5555 or 99999)
print(ans)