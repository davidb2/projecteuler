from operator import add, sub, mul, div
from math import floor
from fractions import Fraction
OPERATORS = set([add, sub, mul, div])
cache = {}

def ways(num_set):
    if len(num_set) == 1:
        return num_set
    xs = tuple(sorted(tuple(num_set)))
    if xs not in cache:
        ans = set()
        for n in xs:
            for o in OPERATORS:
                num_set.remove(n)
                all_lower_sets = ways(num_set)
                for e in all_lower_sets:
                    try:
                        a = o(n, e)
                        ans.add(a)
                    except Exception as e:
                        pass # print e.message
                    try:
                        b = o(e, n)
                        ans.add(b)
                    except Exception as e:
                        pass # print e.message
                num_set.add(n)
        cache[xs] = ans
    return cache[xs]

def find_highest(s):
    # print s
    ss = filter(lambda x: x.denominator == 1 and x >= 1, sorted(list(s)))
    if len(ss) == 0 or ss[0] != 1:
        print ss, s
        return 0
    for i in xrange(1, len(ss)):
        if ss[i] != ss[i-1] + 1:
            return ss[i-1]
    return ss[~0]

max_run = -1
ans = ''
for a in xrange(10):
    for b in xrange(a+1, 10):
        for c in xrange(b+1, 10):
            for d in xrange(c+1, 10):
                temp = find_highest(ways(set(map(Fraction, [a, b, c, d]))))
                print '{} {} {} {}: {}'.format(a, b, c, d, temp)
                if temp > max_run:
                    max_run = temp
                    ans = ''.join(map(str, [a, b, c, d]))
                break
print 'max run: {}\nanswer: {}'.format(max_run, ans)
# print cache[(1, 2, 5, 6)]