def sotd(n):
   if n == 1:
       return False
   return n == sum(list(map(lambda x: int(x)**5, str(n))))
ans = sum(list(filter(sotd,list(range(777777)))))
print(ans)