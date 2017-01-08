pows = list(map(lambda x: 1 << x, range(84)))
cache = {}
def ways(n, i, prev):
    # print('ways({}, {}, {})'.format(n, i, prev))
    if n <= 0:
        return int(n == 0)
    elif (n, i, prev) not in cache:
        ans = 0
        for x in range(i if i != prev else i+1, len(pows)):
            new_n = n-pows[x]
            if new_n >= 0:
                ans += ways(new_n, x, i)
            else:
                break
        cache[(n, i, prev)] = ans
    return cache[(n, i, prev)]
def answer(n):
    ans = 0
    for x in range(2):
        ans += ways(n-pows[x], x, -2)
    return ans

n = 10 ** 10
print(answer(n))
        