# the "digits" function mimics long division
# when dividing by the same number, we have hit a cycle
# also, if the division yields a remainder of zero, we are also done
# the following is a translation of the F# code I wrote
# I also converted it to imperative style (no recursion; more mutation)

def digits(d):
    CYCLE_LENGTH_MAX = 1000000000000
    dic = {}
    i = 0
    n = 10
    while i < CYCLE_LENGTH_MAX: # 1000 is just a guess on the max length of a reciprocal cycle
        if n%d == 0:
            # if i == d:
            #     print(d)
            return i+1
        elif n in dic:
            # if i - dic[n] + 1 == d:
            #     print(d)
            return i - dic[n]
        else:
            dic[n] = i
            n = 10 * (n%d)
            i += 1
    print(d)
    return "ERROR: CYCLE LENGTH LONGER THAN " + str(CYCLE_LENGTH_MAX)
a = list(map(digits, list(range(2, 1000000))))
maxn, maxi = -1, 0
for i in range(len(a)):
    if a[i] > maxn:
        maxn = a[i]
        maxi = i
ans = maxi + 2
print("1/"+str(maxi+2)+" has the longest cycle of length " + str(maxn))