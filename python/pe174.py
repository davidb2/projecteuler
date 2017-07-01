from sys import setrecursionlimit
setrecursionlimit((1<<31)-1)
cache = {}
def f(x, y, skip=False):
    print x, y
    raw_input()
    if x == 0:
        return 1
    elif x < 0 or x < 4*(y-1):
        return 0
    elif (x, y, skip) not in cache:
        ans = f(x-4*(y-1), y+2, skip=False) 
        if skip:
            ans += f(x, y+2, skip=skip)
        cache[(x, y, skip)] = ans
    return cache[(x, y, skip)]
def g(t):
    if t == 0:
        return 0
    else:
        return f(t, 3, skip=True) + f(t, 4, skip=True)