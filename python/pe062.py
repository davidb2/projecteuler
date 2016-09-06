from functools import reduce
f_cache = {}
# prime generator
def f(n):
    if n not in f_cache:
        f_cache[n] = 2*n**2 + 29
    return f_cache[n]
cache = {}
max_len, min_num = 0, 0
def custom_hash(n):
    return reduce(lambda x, y: x*y, list(map(lambda z: f(ord(z)-48), str(n))))
n = 0
while max_len < 5:
    a = custom_hash(n**3)
    if a not in cache:
        cache[a] = []
    cache[a].append(n)
    if len(cache[a]) > max_len:
        max_len, min_num = len(cache[a]), cache[a][0]
    n += 1
print(max_len, min_num, min_num**3)