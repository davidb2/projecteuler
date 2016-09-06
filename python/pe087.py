from functools import reduce
MAX = 50000000
cache = {0: False, 1: False}
ps = []
def is_prime(n):
    if n not in cache:
        for i in ps:
            if n % i == 0:
                cache[n] = False
                return cache[n]
        cache[n] = True
        ps.append(n)
    return cache[n]

squares = list(map(lambda x: x**2, filter(is_prime, range(1+int(MAX**(1/2))))))
cubes = list(map(lambda x: x**3, filter(is_prime, range(1+int(MAX**(1/3))))))
fourths = list(map(lambda x: x**4, filter(is_prime, range(1+int(MAX**(1/4))))))

cache = {}
total = 0
for x in squares:
    for y in cubes:
        xy = x + y
        if xy > MAX: break
        for z in fourths:
            xyz = xy + z
            if xyz > MAX: break
            if xyz not in cache:
                #print(' + '.join(map(str, [x, y, z])), '=', xyz)
                cache[xyz] = True
                total += 1
print(total)