cache = {}          #dynamic programming
def collatz(n):     #not using recursing because it is expensive
    original_n = int(eval(str(n)))
    c = []
    c.append(n)
    while n != 1:
        if n % 2 == 0:
            n = int(n/2)
            try:
                return len(c + cache[n])
            except:
                c.append(n)
        else:
            n = 3 * n + 1
            try:
                return len(c + cache[n])
            except:
                c.append(n)
    cache[original_n] = c
    return len(c)  
a = list(map(collatz, list(range(500000,1000000))))    #starting at 500,000 was a guess
maxi = 0
maximum = 0
for i in range(500000-1):
    if a[i] > maximum:
        maximum = a[i]
        maxi = i+500000
ans = maxi
print(ans)