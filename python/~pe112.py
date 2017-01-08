cache = {}
def min_way(n):
    if n == 1:
        return 0
    elif n not in cache:
        min_ans = 999999999
        a, b = 0, 0
        for x in range(1, n):
            temp_ans = 1 + max(min_way(x), min_way(n-x))
            if temp_ans < min_ans:
                min_ans = temp_ans
                a, b = x, n-x
        if n == 4:
            print(a, b, min_ans)
        cache[n] = min_ans
    return cache[n]

print(list(map(lambda x: min_way(x), range(1, 20+1))))