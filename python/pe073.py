import math
cache = {0.5: True, 1/3: True}
MAX_D = 12000
num = 0
for d in range(4, MAX_D+1):
    for n in range(math.ceil(d/3), d//2+1):
        frac = n/d
        if frac not in cache:
            cache[frac] = True
            num += 1
print(num)        