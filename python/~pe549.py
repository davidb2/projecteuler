from queue import Queue
from math import sqrt
LIMIT = 100
ps = []
def prime_sieve(lim):
    blist = [True for _ in range(lim+1)]
    blist[0] = blist[1] = False
    for i in range(3, lim//2+1, 2):
        if blist[i]:
            for p in range(i*i, lim+1, i):
                blist[p] = False
    ps.append(2)
    for i in range(3, lim+1, 2):
        if blist[i]:
            ps.append(i)
prime_sieve(LIMIT)


ans = [0 for x in range(LIMIT+1)]
ans[1] = 1
bfs = Queue()

# initialize Queue
for i in range(len(ps)):
    bfs.put_nowait((ps[i], ps[i], i)) # (curr_prod, fact, index)

while not bfs.empty():
    cp, f, i = bfs.get_nowait()
    if cp <= LIMIT:
        ans[cp] = f
        for x in range(i, len(ps)):
            np = cp*ps[x]
            bfs.put_nowait((np, f + (ps[x] - cp%ps[x])%np, x))
print(ans, sum(ans))