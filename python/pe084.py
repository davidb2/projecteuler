#!/usr/bin/env python3.6
import math
import random

from collections import defaultdict, deque

TURNS = 10000000
BOARD = [
  'GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
  'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
  'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
  'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2',
]

BOARD_2_IDX = {x: i for i, x in enumerate(BOARD)}
assert len(BOARD) == len(BOARD_2_IDX)

LANDS = defaultdict(int)

def log(oldi, i):
  LANDS[BOARD[i]] += 1


def roll():
  return [random.randint(1, 4), random.randint(1, 4)]


def play():
  i = 0
  doubles = 0
  community = ['GO', 'JAIL'] + [None]*14
  chance = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'R', 'R', 'U', -3] + [None]*6
  random.shuffle(community)
  random.shuffle(chance)
  community = deque(community)
  chance = deque(chance)

  for _ in range(TURNS):
    oldi = i
    a, b = roll()

    doubles = doubles + 1 if a == b else 0
    if doubles == 3:
      i = BOARD_2_IDX['JAIL']
      doubles = 0
      log(oldi, i)
      continue

    i = (i + (a + b)) % len(BOARD)

    if BOARD[i] == 'G2J':
      i = BOARD_2_IDX['JAIL']
    elif BOARD[i].startswith('CH'):
      ch = chance.popleft()
      if ch is None:
        pass
      elif type(ch) is int:
        i = (i + ch) % len(BOARD)
      elif len(ch) == 1:
        for j in range(1, len(BOARD)):
          if BOARD[(i + j) % len(BOARD)].startswith(ch):
            i = (i + j) % len(BOARD)
            break
        else:
          assert False
      else:
        i = BOARD_2_IDX[ch]
      chance.append(ch)
    elif BOARD[i].startswith('CC'):
      cc = community.popleft()
      if cc is not None:
        i = BOARD_2_IDX[cc]
      community.append(cc)

    log(oldi, i)


if __name__ == '__main__':
  play()
  ds = sorted(LANDS.items(), reverse=True, key=lambda t: t[1])
  print(''.join([str(BOARD_2_IDX[d]).rjust(2, '0') for (d, _) in ds[:3]]))
