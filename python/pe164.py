cache = {} 
def count(ds):
    if ds[2] == 0:
        return 1
    elif ds in cache:
        return cache[ds]
    else:
        num = 0
        for next_digit in range(10):
            if ds[0] + ds[1] + next_digit <= 9:
                num += count((ds[1], next_digit, ds[2]-1))
        cache[ds] = num
        return num
def ans(n):
    if n < 1:
        return 0
    elif n == 1:
        return 9
    elif n == 2:
        return 45
    else:
        num = 0
        for d1 in range(1, 10):
            for d2 in range(10):
                num += count((d1, d2, n-2))
        return num
for i in range(10):
    print ans(i)
