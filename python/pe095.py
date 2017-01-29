from __future__ import division
from math import sqrt
from operator import itemgetter

LIMIT = 10**6

# collect sums of divisors
bucket = [1 for i in xrange(LIMIT+1)]
for step in xrange(2, (LIMIT+1)//2+1):
    for x in xrange(2*step, LIMIT+1, step):
        bucket[x] += step

def find_longest_amicable_chain(x, init, seen):
    if x in seen or x > LIMIT:
        return 0 if x == init else -LIMIT, x if x == init else LIMIT+1
    else:
        seen.add(x)
        chain_len, min_elem = find_longest_amicable_chain(bucket[x], init, seen)
        seen.remove(x)
        return 1 + chain_len, min(x, min_elem)

lis = map(lambda x: find_longest_amicable_chain(x, x, set()), xrange(LIMIT+1))
max_index, (chain_len, min_elem) = max(enumerate(lis), key=itemgetter(1))

print ('Chain starting at: {}\nChain length: {}\nMin element: {}'.format(
        max_index, chain_len, min_elem))