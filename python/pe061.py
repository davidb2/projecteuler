from functools import reduce
from math import sqrt, ceil
from sys import exit
cache = {3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}}
def P(s, n):
    return ((s-2)*n**2-(s-4)*n)//2
def invP(s, n):
    return ((s-4) + sqrt((s-4)**2 + 8*n*(s-2)))/(2*(s-2))
def jump(possible, acc, i, n): # DFS
    if i == n and acc[-1]%100 == acc[0]//100:
        print(acc)
        print(sum(acc))
        exit()
    else:
        for s in possible:
            if acc[-1]%100 in cache[s]:
                for _key in cache[s][acc[-1]%100]: 
                    new_pos = [x for x in possible if x != s]
                    jump(new_pos, acc+[_key], i+1, n)
sets = []
for s in range(3, 8+1):
    min_n, max_n = int(ceil(invP(s, 1000))), int(invP(s, 10000))
    sets.append(list(map(lambda n: P(s, n), list(range(min_n, max_n+1)))))
for i in range(6):
    for num in sets[i]:
        if num%100 > 9:
            if num//100 not in cache[i+3]:
                cache[i+3][num//100] = [num]
            else:
                cache[i+3][num//100] = cache[i+3][num//100]+[num]
pos = [3, 4, 5, 6, 7]
for num in sets[8-3]:
    jump(pos, [num], 0, 6-1)