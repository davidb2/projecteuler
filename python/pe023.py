def sod(n):
   divisors = []
   temp_divisors = []
   divisors.append(1)
   temp_divisors.append(1)
   for i in range(2,int(n**0.5)+1):
       if n % i == 0:
           divisors.append(i)
           temp_divisors.append(i)
   for i in reversed(temp_divisors[1:len(temp_divisors)]):
       divisors.append(int(n/i))
   return sum(list(set(divisors)))
def abundant(n):
   return sod(n) > n
ab = list(filter(abundant, list(range(12, 28124))))
sums_of_ab = []
for i in ab:
   for j in ab:
       if i+j > 28123:
           break
       else:
           sums_of_ab.append(i+j)
sums_of_ab = set(sums_of_ab)
sums = {key: True for key in range(28124)}
for i in sums_of_ab:
   sums[i] = False
ans = 0
for i in range(28124):
   if sums[i]:
       ans += i
print(ans)