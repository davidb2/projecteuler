###########################################################################
### Very slow program exploiting hashing with prime factorization laws; ###
########################## runs in 32.732 seconds #########################
# f = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# magic_num = 6469693230
# cache = {}
# def ways(d, n, acc):
#     if n == 0:
#         return int(bool(acc == 0))
#     elif (d, n, acc) not in cache:
#         smaller = ways(d-1, n-1, (acc * f[d-1]) % magic_num) if d-1 != -1 else 0
#         bigger = ways(d+1, n-1, (acc * f[d+1]) % magic_num) if d+1 != 10 else 0
#         cache[(d, n, acc)] = smaller + bigger
#     return cache[(d, n, acc)]
# ans = 0
# for n in range(2, 40+1):
#     for d in range(1, 9+1):
#         ans += ways(d, n-1, f[d])
# print(ans)


############################################################
### Much fater than above program; runs in 0.183 seconds ###
############################################################
cache = {}
def ways(d, n, acc):
    # if no more digits, check to see that all digits were used at least once
    if n == 0:
        return int(bool(acc == tuple([True for i in range(10)])))
    # else, if not already computed, compute it!
    elif (d, n, acc) not in cache:
        # copies of the array determining the distinct digits used
        accp1 = list(acc)
        accp2 = list(acc)
        # if 0 <= d-1 <= 9, recur, marking d-1 as a used digit
        if d-1 >= 0:
            accp1[d-1] = True
            smaller = ways(d-1, n-1, tuple(accp1))
        # else, this is not valid digit
        else:
             smaller = 0
        # if 0 <= d+1 <= 9, recur, marking d+1 as a used digit
        if d+1 < 10:
            accp2[d+1] = True
            bigger = ways(d+1, n-1, tuple(accp2))
        # else, this is not valid digit
        else:
             bigger = 0
         # store the already calulated "left" and "right" side of the recurrence
         # relation in the cache
        cache[(d, n, acc)] = smaller + bigger
    # return the answer that is stored in cache
    return cache[(d, n, acc)]

# this is the entrypoint of the program
ans = 0
# `Java equivalent`
# for (int n = 2; n < 40+1; n++)
for n in range(2, 40+1):
    # `Java equivalent`
    # for (int d = 1; d < 9+1; d++)
    for d in range(1, 9+1):
        # `Java equivalent`
        # boolean acc[] = new boolean[10];
        # acc[d] = true;
        # ans += ways(d, n-1, acc);
        ans += ways(d, n-1, tuple([True if i == d else False for i in range(10)]))
print(ans)