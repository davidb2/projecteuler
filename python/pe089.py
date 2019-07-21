#!/usr/bin/env python3.6
import functools
import math

'''
Rules

(i)   Numerals must be arranged in descending order of size.
(ii)  M, C, and X cannot be equalled or exceeded by smaller denominations.
(iii) D, L, and V can each only appear once.
(iv)  Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
(v)   I can only be placed before V and X.
(vi)  X can only be placed before L and C.
(vii) C can only be placed before D and M.
'''

ROM_TO_NUM = {
  'I' : 1,
  'IV': 4,
  'V' : 5,
  'IX': 9,
  'X' : 10,
  'XL': 40,
  'L' : 50,
  'XC': 90,
  'C' : 100,
  'CD': 400,
  'D' : 500,
  'CM': 900,
  'M' : 1000,
}
NUM_TO_ROM = {v: k for k, v in ROM_TO_NUM.items()}
ROMS = [t[0] for t in sorted(ROM_TO_NUM.items(), key=lambda t: t[1])]
SUBS = [x for x in ROMS if len(x) == 2]


@functools.lru_cache(maxsize=None)
def minimal(n, d, D=False, L=False, V=False):
  if n < 0 or d < 0: return +math.inf
  if n == 0: return 0
  zs = [y for x, y in [(D, 'D'), (L, 'L'), (V, 'V')] if x]
  keep = (
    minimal(
      n-ROM_TO_NUM[ROMS[d]],
      d,
      D=D or 'D' in ROMS[d],
      L=L or 'L' in ROMS[d],
      V=V or 'V' in ROMS[d],
    ) + len(ROMS[d]) if all(z not in ROMS[d] for z in zs) else +math.inf
  )
  move = minimal(n, d-1, D, L, V) if ROM_TO_NUM[ROMS[d]] > n else +math.inf
  return min(keep, move)


def best(n):
  return minimal(n, len(ROMS)-1)


@functools.lru_cache(maxsize=None)
def parse(r):
  if len(r) == 0: return 0
  if r[:2] in SUBS: return ROM_TO_NUM[r[:2]] + parse(r[2:])
  return ROM_TO_NUM[r[0]] + parse(r[1:])


if __name__ == '__main__':
  total = 0
  with open('../pe089.txt', 'r') as f:
    for line in f:
      r = line.strip()
      n = parse(r)
      m = best(n)
      assert m <= len(r), (m, n, r)
      total += (len(r)-m)
  print(total)
