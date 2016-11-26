from queue import Queue
LIMIT = 10
min_n_for_k = [-1 for _ in range(LIMIT+1)]
f = LIMIT

# void method
def mins(n):   
    print(n)
    global f
    bfs = Queue()
    # initialize Queue
    for i in range(1, n+1):
        bfs.put_nowait((i, i, i, 1)) # (sum, prod, lastnum, len)
    
    while not bfs.empty():
        s, p, ln, l = bfs.get_nowait()
        # print(s, p, ln, l)
        if l <= LIMIT and n == s == p and min_n_for_k[l] == -1:
            min_n_for_k[l] = n
            f -= 1
            #print(f)
        elif s <= n and p <= n and l < LIMIT:
            for i in range(ln, n+1):
                bfs.put_nowait((s+i, p*i, i, l+1))

x = 1
while f > 0:
    mins(x)
    x += 1

print(min_n_for_k)