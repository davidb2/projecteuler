from math import sqrt
LIMIT = 100 ** 6
table = {}
for x in xrange(1, int(sqrt(LIMIT))+1):
    # print x
    for y in xrange(1, x):
        z = y - (x - y)
        interm = x*x-y*y-z*z
        if interm == 27:
            pass#print '{}^2 - {}^2 - {}^2 = {}'.format(x, y, z, interm)
        if interm > 0 and x > y > z > 0:
            if interm not in table:
                table[interm] = 0
            table[interm] += 1
print table[1155]