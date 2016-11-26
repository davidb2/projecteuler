cache = {}
def ways(n, m):
    if n < m:
        return 1
    elif (n, m) not in cache:
        # don't place a block OR place a block
        cache[(n, m)] = ways(n-1, m) + ways(n-m, m)
    return cache[(n, m)]

# exclude case where no blocks placed
def ans(n, m):
    return ways(n, m) - 1

ans = sum(map(lambda m: ans(50, m), [2, 3, 4]))
print(ans)