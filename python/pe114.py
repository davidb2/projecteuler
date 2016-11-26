cache = {}
def ways(i, n, red=False):
    if n == i:
        return 1
    elif i > n:
        return 0
    elif (i, n, red) not in cache:
        ans = 0
        init = 3 if red else 1
        for l in range(init, n):
            ans += ways(i+l, n, not red)
        cache[(i, n, red)] = ans
    return cache[(i, n, red)]

def ans(n):
    return 2 + ways(0, n, red=True) + ways(0, n, red=False)

print(ans(50))