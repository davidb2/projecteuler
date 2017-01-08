def pattern():
    i = 1
    inc = True
    while True:
        if i == 0:
            inc = True
            i = 2
        elif i == 5:
            inc = False
            i = 3
        yield i
        i += 1 if inc else -1

MOD = 123454321
x = 1
e = pattern()
ans = 0
while x <= 10000:
    ts = 0
    a = ''
    while ts != x:
        s = e.__next__()
        ts += s
        a += str(s)
    ans = (ans + int(a)) % MOD
    # print(x, a, ans)
    
    #input()
    x += 1
print(ans)