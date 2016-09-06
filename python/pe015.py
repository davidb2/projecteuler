cache = {}
def ways(r, c):
    if r == 0 or c == 0:
        return 1
    elif (r, c) not in cache:
        cache[(r, c)] = ways(r, c-1) + ways(r-1, c)
    return cache[(r, c)]
print(ways(20, 20))