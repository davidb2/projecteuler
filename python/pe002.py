fib = {}  
def fib3(n):
    for k in range(1, n+1):
        if k < 3: 
            f = 1
        else:
            f = fib[k-1] + fib[k-2]
        fib[k] = f
ans = 0
fib3(33)
for i in list(map(lambda x: 3 * x, range(1,12))):
    ans += fib[i]
print(ans)