from Queue import Queue
LIMIT = 10 ** 6

def ways(start, limit=LIMIT):
    ans = 0
    curr_sum = 0
    curr = start
    queue = Queue()
    while curr_sum <= limit:
        curr_sum += 4*(curr-1)
        if curr_sum > limit:
            while curr_sum > limit:
                if queue.empty():
                    break
                else:
                    ans += queue.qsize()
                    old = queue.get_nowait()
                    curr_sum -= 4*(old-1)
        queue.put_nowait(curr)
        curr += 2
    return ans
print ways(3) +  ways(4)