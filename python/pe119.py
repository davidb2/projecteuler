from queue import PriorityQueue

# Brute force. Very ugly. There are better ways. Below code runs in ~2 mins for
# me.
if __name__ == '__main__':
  bfs = PriorityQueue()
  bfs.put((2**2, 2, 2))
  seen = set()
  i = 0
  while not bfs.empty() and i < 30:
    x, a, n = bfs.get()
    if (a, n) in seen: continue
    seen.add((a, n))

    if sum(map(int, str(x))) == a:
      print(i, a, n, x)
      i += 1

    if (a+1, n) not in seen:
      bfs.put(((a+1)**n, a+1, n))
    if (a, n+1) not in seen:
      bfs.put((x*a, a, n+1))
