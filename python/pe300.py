from collections import defaultdict
from itertools import product
from typing import DefaultDict, Dict, Set, Tuple

Point = Tuple[int, int]

def to_contact_map(fold: Dict[Point, int], n: int):
  idx_to_point = {v:k for k,v in fold.items()}
  contact_map: DefaultDict[int, Set[int]] = defaultdict(set)
  for i in range(n):
    r, c = idx_to_point[i]
    for pos in neighbors(r, c):
      if (dest := fold.get(pos, -1)) > i:
        contact_map[i].add(dest)

def neighbors(r, c):
  return (
    (r+dr, c+dc)
    for dr, dc in product((-1,0,+1), repeat=2)
    if dr ** 2 + dc ** 2 == 1
  )


def contact_maps(n):
  for fold in folds({}, (0, 0), 0, n):
    contact_map = to_contact_map(fold, n)
    expected_contact_points(contact_map)

def folds(seen: Dict[Point, int], curr: Point, i: int, n: int):
  if i == n:
    yield seen
    return

  assert i < n

  r, c = curr
  possible_positions = (
    pos
    for rp, cp in neighbors(r, c)
    if (pos := (rp, cp)) not in seen
  )
  for pos in possible_positions:
    seen[pos] = i
    yield from folds(seen, pos, i+1, n)
    seen.pop(pos)
