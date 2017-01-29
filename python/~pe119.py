from Queue import PriorityQueue

A = []

next_a = 3
next_a_s = next_a * next_a
pq = PriorityQueue()
pq.put_nowait((2, (2, 1)))
while pq.not_empty:
    ans, (a, n) = pq.get_nowait()
    # print 'checking: {}^{} = {}'.format(a, n, ans)
    if ans > next_a:
        pq.put_nowait((ans, (a, n)))
        pq.put_nowait((next_a_s, (next_a, 2)))
        next_a += 1
        next_a_s = next_a * next_a
    else:
        if len(str(ans)) > 1 and a == sum(map(int, str(ans))):
            A.append(ans)
            print '{}^{} = {}'.format(a, n, ans)
        pq.put_nowait((ans * a, (a, n+1)))
