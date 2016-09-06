# U...g...l...y.........but it runs fine
cprobs = {key: 0 for key in list(range(6,37))}
for i in range(1,7):
   for j in range(1,7):
       for k in range(1,7):
           for l in range(1,7):
               for m in range(1,7):
                   for n in range(1,7):
                       cprobs[i+j+k+l+m+n]+=1
pprobs = {key: 0 for key in list(range(9,37))}
for i in range(1,5):
   for j in range(1,5):
       for k in range(1,5):
           for l in range(1,5):
               for m in range(1,5):
                   for n in range(1,5):
                       for o in range(1,5):
                           for p in range(1,5):
                               for q in range(1,5):
                                   pprobs[i+j+k+l+m+n+o+p+q]+=1
psum = 0
for i in range(9,37):
   psum += pprobs[i]
csum = 0
for i in range(6,37):
   csum += cprobs[i]
for i in range(9,37):
   pprobs[i]/=psum
for i in range(6,37):
   cprobs[i]/=csum
ans = 0
for i in range(9,37):
   for j in range(6,37):
       if i > j:
           ans+=pprobs[i]*cprobs[j]
print('{0:.7}'.format(ans))

### OR A MUCH NICER VERSION ###

ccprobs = {key: 0 for key in list(range(6,37))}
ppprobs = {key: 0 for key in list(range(9,37))}
def base_sum(n, b, l, i, acc):
    if n == 0:
        return acc + (l-i)
    else:
        return base_sum(n//b, b, l, i+1, acc+(n % b)+1)
for i in range(6**6):
    ccprobs[base_sum(i, 6, 6, 0, 0)] += 1
for i in range(4**9):
    ppprobs[base_sum(i, 4, 9, 0, 0)] += 1
ppsum = sum(ppprobs[i] for i in ppprobs)
ccsum = sum(ccprobs[i] for i in ccprobs)
for i in ppprobs:
   ppprobs[i] /= ppsum
for i in ccprobs:
   ccprobs[i] /= ccsum
aans = 0
for i in range(9,37):
   for j in range(6,37):
       if i > j:
           aans += ppprobs[i] * ccprobs[j]
print('{0:.7}'.format(aans))