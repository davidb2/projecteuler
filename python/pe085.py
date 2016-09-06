def ans(m, n):
    count = 0
    for x in range(1, m+1):
        for y in range(1, n+1):
            count += (m-x+1)*(n-y+1)
    return count
########################################
WAYS = 2000000
min_i, min_j, min_delta = 0, 0, WAYS
i, j = 1, 1
flag = True
while True:
    j = i
    pos_ans = ans(i, j)
    # print(i, j)
    if pos_ans > WAYS:
        break
    else:
        while True:
            pos_ans = ans(i, j)
            delta = abs(pos_ans - WAYS)
            # print(i, j, pos_ans)
            if delta < min_delta:
                min_i, min_j, min_delta = i, j, delta
            elif pos_ans > WAYS:
                flag = False
                break
            j += 1
    i += 1
print(min_i, min_j, ans(min_i, min_j), min_i*min_j)