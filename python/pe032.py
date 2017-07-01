# not most effiecient (~10^8 operations)
LIM = 10 ** 3
ip = lambda a, b: sorted(''.join(map(str, (a, b, a*b)))) == list('123456789')
nums = set()
for a in xrange(LIM):
    for b in xrange(LIM):
        if ip(a, b):
            nums.add(a*b)

for a in xrange(LIM*10):
    for b in xrange(LIM//10):
        if ip(a, b):
            nums.add(a*b)

print sum(nums)