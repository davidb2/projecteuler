def psieve(limit):
   bprimes = {key: True for key in list(range(1,limit+2))}
   bprimes[1] = False
   primes = []
   p = [2]
   for i in p:
       for step in list(map(lambda x: x * i, list(range(2, int(limit/i)+1)))):
           bprimes[step] = False
       if i+1 < int(limit/2):
           for pr in range(i+1, len(bprimes)+1):
               if bprimes[pr]:
                   p.append(pr)
                   break
       else:
           break
   for k in range(1, len(bprimes)):
       if bprimes[k]:
           primes.append(k)
   return primes
ps = {key: False for key in range(20000+1)}
pss = psieve(20000)
for i in pss:
   ps[i] = True
def nop (a,b,n):
   flag = True
   while flag:
       eq = n**2 + a*n + b
       if eq < 2:
           flag = False
       elif not ps[n**2 + a*n + b]:
           flag = False
       else:
           n += 1
   return n
anums = list(map(lambda x: -1*x, list(reversed(range(1,1000))))) + list(range(1000))
bnums = psieve(1000)
cp = []
for a in anums:
   for b in bnums:
       n = nop(a,b,0)
       cp.append((a,b,n,a*b))
quad = max(cp, key = lambda x: x[2])
ans = quad[3]
print(ans)