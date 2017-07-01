# from Queue import Queue
# LIMIT = 100
# min_n_for_k = [-1 for _ in range(LIMIT+1)]
# f = LIMIT
#
# # void method
# def mins(n):
#     print(n)
#     global f
#     bfs = Queue()
#     # initialize Queue
#     for i in range(1, n+1):
#         bfs.put_nowait((i, i, i, 1)) # (sum, prod, lastnum, len)
#
#     while not bfs.empty():
#         s, p, ln, l = bfs.get_nowait()
#         # print(s, p, ln, l)
#         if l <= LIMIT and n == s == p and min_n_for_k[l] == -1:
#             min_n_for_k[l] = n
#             f -= 1
#             #print(f)
#         elif s <= n and p <= n and l < LIMIT:
#             for i in range(ln, n+1):
#                 bfs.put_nowait((s+i, p*i, i, l+1))
#
# x = 1
# while f > 0:
#     mins(x)
#     x += 1
#
# print(min_n_for_k)

cache = {}
MAX = 120
def min_cost(start, prod, addi, n):
    print (start, prod, addi, n)
    if prod == addi:
        return n, prod
    elif n > MAX or (prod > addi and prod != 1 and addi != 0):
        return None
    elif (start, prod, addi) not in cache:
        ans = None
        for pos_start in xrange(start, MAX):
            temp_ans = min_cost(pos_start, prod*pos_start, addi+pos_start, n+1)
            if (ans is None) or (temp_ans is not None and temp_ans[0] < ans[0]):
                ans = temp_ans
        for pos_start in xrange(start, MAX):
            cache[(pos_start, prod, addi)] = ans
    return cache[(start, prod, addi)]




