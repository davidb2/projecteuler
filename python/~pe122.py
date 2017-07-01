# from Queue import Queue

# min_lens = [0 for i in xrange(200+1)]

# bfs = Queue()

# # (curr_sum, used, len)
# bfs.put_nowait((1, set([1]), 0))

# while not bfs.empty():
#     (curr_sum, used, length) = bfs.get_nowait()
#     if curr_sum < len(min_lens):
#         if min_lens[curr_sum] == 0:
#             min_lens[curr_sum] = length
#         for e in used:
#             new_sum = curr_sum + e
#             bfs.put_nowait((new_sum, used.union(set([new_sum])), length+1))
# print sum(min_lens)

cache = {}
LIMIT = 10
def min_cost(target, curr_sum=1, used=set([1]), length=0):
    if curr_sum == target:
        return length
    t = (target-curr_sum), tuple(sorted(used))
    if t not in cache:
        ans = None
        for e in t[1]:
            new_sum = curr_sum + e
            if new_sum > target:
                break
            old_len = len(used)
            used.add(new_sum)
            new_len = len(used)
            temp_ans = min_cost(target, new_sum, used, length+1)
            if ans is None or temp_ans < ans:
                ans = temp_ans
            if old_len != new_len:
                used.remove(new_sum)
        cache[t] = ans
    else:
        print 'got'
    return cache[t]

print min_cost(155), len(cache)