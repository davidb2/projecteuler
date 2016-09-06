def s(n):
   if n%2 == 0:
       return -1
   inc = list(map(lambda x: 2*x, list(range(1,int((n+1)/2)))))
   f = 1
   num = 1
   for i in inc:
       for j in range(4):
           num += i
           f += num 
   return f
ans = s(1001)
print(ans)