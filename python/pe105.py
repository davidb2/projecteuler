# python 2.7
from itertools import combinations
def findsubsets(S):
    return reduce(lambda x,y:x+y, [list(combinations(S, z)) for z in xrange(1, len(S)+1)])

ans = 0
for line in open('../pe105.txt', 'r').readlines():
    arr = map(int, line.split(','))
    print arr
    Pn = findsubsets(arr)
    flag = True
    for i in xrange(len(Pn)):
        for j in xrange(i+1, len(Pn)):
            B, C = sorted((Pn[i], Pn[j]), key=len, reverse=True)
            Bs = sum(B)
            Cs = sum(C)
            if not (Bs != Cs and (len(B) == len(C) or (len(B) > len(C) and Bs > Cs))):
                flag = False
                break
        if not flag:
            break
    if flag:
        ans += sum(arr)
print ans