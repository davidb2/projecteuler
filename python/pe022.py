def name_score(n):
   return sum(list(map(lambda x: ord(x)-ord('A')+1, n)))
names = open('../pe022.txt').read().split('","')
names[0] = ''.join(list(filter(lambda n: n != '"', names[0])))
names[len(names)-1] = ''.join(list(filter(lambda n: n != '"', names[len(names)-1])))
names.sort()
ans = 0
i = 1
for name in names:
   ans += name_score(name) * i
   i += 1
print(ans)