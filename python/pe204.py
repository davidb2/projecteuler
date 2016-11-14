# using a queue
from queue import Queue
LIM = 10**9
TYPE = 100
bfs = Queue()
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
prime_sieve(TYPE)
for i in range(len(ps)):
    bfs.put_nowait((ps[i], i))
ans = 1
while not bfs.empty():
    top_num, i = bfs.get_nowait()
    if top_num <= LIM:
        for x in range(i, len(ps)):
            # print('{} x {}'.format(ps[x], top_num))
            bfs.put_nowait((ps[x]*top_num, x))
        ans += 1
print(ans)