from math import sqrt
from queue import Queue

def ps(x):
    return int(sqrt(x))**2 == x

def satifies(x, y, z):
    a = [x+y, x-y, x+z, x-z, y+z, y-z]
    if len(set(map(lambda x: x%2, (x, y, z)))) != 1:
        return False
    # print('{}, {}, {}'.format(x, y, z))
    # print('\tx + y = {}\n\tx - y = {}'.format(x+y, x-y))
    # print('\tx + z = {}\n\tx - z = {}'.format(x+z, x-z))
    # print('\ty + z = {}\n\ty - z = {}'.format(y+z, y-z))
    # print('\n')
    for n in a:
        if not ps(n):
            return False
    return True

seen = set()
bfs = Queue()
initial_conf = 3, 2, 1
bfs.put_nowait(initial_conf)
while not bfs.empty():
    x, y, z = bfs.get_nowait()
    if x > y > z > 0 and (x, y, z) not in seen:
        seen.add((x, y, z))
        if satifies(x, y, z):
            print(x, y, z)
            break
        else:
            bfs.put_nowait((x+1, y, z))
            bfs.put_nowait((x, y+1, z))
            bfs.put_nowait((x, y, z+1))
    # input()