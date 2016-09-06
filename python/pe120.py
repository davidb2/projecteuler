# brute force; take a couple of minutes; there are better ways!
def calc(a):
    # debugging purposes
    if a % 100 == 0: print(a)
    max_r  = 0
    # starting from a = 3:
    # double 
    # half
    # double 
    # same
    # -------
    # after some analysis, this is true
    iterations = 2*a if a % 2 == 1 else (a, a//2)[a % 4 == 0]
    # when n is even, r = 2, therefore, only check odd n's
    for n in range(1, 2*iterations+3, 2):
        ans = (a-1)**n + (a+1)**n
        r = ans % a**2
        max_r = r if r > max_r else max_r
    return max_r
print(sum(map(calc, range(3, 1000+1))))