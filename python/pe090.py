import itertools

class Number:
  def __init__(self, value):
    self.values = {str(value)} if value not in (6, 9) else {'6', '9'}

  def __iter__(self):
    return iter(self.values)

  def __repr__(self):
    return repr(self.values)

  def __eq__(self, other):
    return self.values == other.values

  def __hash__(self):
    return hash(tuple(self.values))


NUMBERS = [Number(x) for x in range(9+1)]
SQUARES = set([str(x ** 2).rjust(2, '0') for x in range(1, 9+1)])


def get(cube1, cube2):
  s = set()
  for d1 in cube1:
    for d2 in cube2:
      for dr1 in d1:
        for dr2 in d2:
          s.add(dr1+dr2)
          s.add(dr2+dr1)
  return s

if __name__ == '__main__':
  total = 0
  for cube1 in itertools.combinations(NUMBERS, 6):
    for cube2 in itertools.combinations(NUMBERS, 6):
      s = get(cube1, cube2)
      if SQUARES <= s:
        total += 1

  print(int(total / 2))
