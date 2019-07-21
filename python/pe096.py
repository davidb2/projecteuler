def findIdx(grid):
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] == 0:
        return r, c

  return None

def pprint(grid):
  for r in range(len(grid)):
    print(grid[r])

def valid(grid, r, c):
  v = [grid[x][c] for x in range(9) if grid[x][c] != 0]
  h = [grid[r][x] for x in range(9) if grid[r][x] != 0]
  s = [
    grid[rr][cc]
    for rr in range(3*(r // 3), 3*(r // 3) + 3)
    for cc in range(3*(c // 3), 3*(c // 3) + 3)
    if grid[rr][cc] != 0
  ]
  return all(len(set(y)) == len(y) for y in (v, h, s))


def solve(grid):
  x = findIdx(grid)
  if x is None: return True

  r, c = x
  for n in range(1, 9+1):
    grid[r][c] = n
    if valid(grid, r, c) and solve(grid): return True
    grid[r][c] = 0

  return False


if __name__ == '__main__':
  total = 0
  with open('../pe096.txt', 'r') as f:
    grid = None
    for line in f.readlines():
      if line.startswith('Grid'):
        if grid is not None:
          assert solve(grid)
          tl = int(''.join(map(str, grid[0][:3])))
          print(tl)
          total += tl
        grid = []
      else:
        grid.append(list(map(int, line.strip())))

    if len(grid) > 0:
      assert solve(grid)
      tl = int(''.join(map(str, grid[0][:3])))
      print(tl)
      total += tl

  print('Ans:', total)