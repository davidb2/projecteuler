from functools import reduce

numerator = []
denominator = []

for a in range(10,100):
   for b in range (a+1, 100):
       al = list(map(int, str(a)))
       bl = list(map(int, str(b)))
       if al[0] == bl[0] and al[0]+bl[0] > 0 and al[1]!=0 and bl[1]!=0:
           if a/b == al[1]/bl[1]:
               numerator.append(al[1])
               denominator.append(bl[1])
               print (a, b, al[1], bl[1])
       elif al[0] == bl[1] and al[0]+bl[1] > 0 and al[1]!=0 and bl[0]!=0:
           if a/b == al[1]/bl[0]:
               numerator.append(al[1])
               denominator.append(bl[0])
               print (a, b, al[1], bl[0])
       elif al[1] == bl[0] and al[1]+bl[0] > 0 and al[0]!=0 and bl[1]!=0:
           if a/b == al[0]/bl[1]:
               numerator.append(al[0])
               denominator.append(bl[1])
               print (a, b, al[0], bl[1])
       elif al[1] == bl[1] and al[1]+bl[1] > 0 and al[0]!=0 and bl[0]!=0:
           if a/b == al[0]/bl[0]:
               numerator.append(al[0])
               denominator.append(bl[0])
               print (a, b, al[0], bl[0])
n = reduce(lambda x,y: x*y, numerator)
d = reduce(lambda x,y: x*y, denominator)

for i in range(2,int(d/2)+1):
   while n%i==0 and d%i==0:
       n = int(n/i)
       d = int(d/i)
print(d)