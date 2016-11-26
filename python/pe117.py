cache = {}
def ways(n):
    if n <= 0:
        return n == 0
    elif n not in cache:
        # don't place a block OR place blocks of size 2, 3, OR 4
        cache[n] = ways(n-1) + ways(n-2) + ways(n-3) + ways(n-4)
    return cache[n]

ans = ways(50)
print(ans)