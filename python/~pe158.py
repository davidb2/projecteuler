cache = {}
num_storage = {}
alphabet = list(map(chr, range(ord('a'), ord('z')+1)))


def sorted_ways(n, last, seen):
    if n == 0:
        return 1
    elif (n, last) not in num_storage:
        ans = 0
        for i in xrange(ord('a'), ord(last)+1):
            ans += sorted_ways(n-1, chr(i))
        num_storage[(n, last)] = ans
    return num_storage[(n, last)]

def ways(n, last, count, seen):
    #print(carry)
    #raw_input()
    if n == 0 and count == 1:
        print carry
        return 1
    elif count == 1:
        ans = sorted_ways(n, last)
        #print 'sw({}, {}): {}'.format(n, last, ans)
        return ans
    elif (n == 0 and count != 1) or count > 1:
        return 0
    elif (n, last) not in cache:
        ans = 0
        for c in alphabet:
            ans += ways(n-1, c, count + int(last < c))
        cache[(n, last)] = ans
    return cache[(n, last)]

ans = 0
n = 3
for c in alphabet:
    ans += ways(n-1, c, 0, set([c]))

print ans