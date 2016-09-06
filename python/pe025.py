fib = {}
def f(n):
   try: 
       fib[n] = fib[n-1] + fib[n-2]
   except:
       for k in range(1, n+1):
           if k < 3: 
               f = 1
           else:
               f = fib[k-1] + fib[k-2]
           fib[k] = f
   return fib[n]
def nodof(n):
   return len(str(f(n)))
i = 1
n = nodof(i)
while n < 1000:
   i += 1
   n = nodof(i)
ans = i
print(ans)