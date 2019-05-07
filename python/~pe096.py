class Tile:
  def __init__(self, number=None, hints=None):
    self.number = number
    self.hints = hints or set()

class Board:
  def __init__(self, board):
    self.board = [[Tile() for _ in range(9)] for _ in range(9)]
    for rowIdx, row in enumerate(board):
      for colIdx, element in enumerate(row):
        self.board[rowIdx][colIdx].number = element

  def __getitem__(self, key):
    return self.board[key]

  def __iter__(self):
    return self.board.__iter__()

  def getCode(self):
    return int(''.join([str(tile.number) for tile in self.board[0][0:3]]))

  def updateAllHints(self):
    for rowIdx, row in enumerate(self.board):
      for colIdx, element in enumerate(row):
        self.board[rowIdx][colIdx].hints = self.getHints(rowIdx, colIdx)

  def getHints(self, row, col):
    '''Set possible moves for (row, col).'''
    assert 0 <= row <= len(self.board) and 0 <= col <= len(self.board[0])
    if self.board[row][col].number is not None:
      return set()
    hints = set(range(1, 10))
    for rowIdx in range(9):
      if rowIdx != row:
        hints.discard(self.board[rowIdx][col].number)
    for colIdx in range(9):
      if colIdx != col:
        hints.discard(self.board[row][colIdx].number)
    blockRow, blockCol = row // 3, col // 3
    for rowIdx in range(3 * blockRow, 3 * (blockRow + 1)):
      for colIdx in range(3 * blockCol, 3 * (blockCol + 1)):
        if rowIdx != row or colIdx != col:
          hints.discard(self.board[rowIdx][colIdx].number)
    return hints

  def uniqueHints(self, row, col):
    assert 0 <= row < len(self.board) and 0 <= col < len(self.board[0])

    colHints = set()
    for rowIdx in range(9):
      if rowIdx != row:
        colHints.update(self.board[rowIdx][col].hints)

    rowHints = set()
    for colIdx in range(9):
      if colIdx != col:
        rowHints.update(self.board[row][colIdx].hints)

    blockRow, blockCol = row // 3, col // 3
    blockHints = set()
    for rowIdx in range(3 * blockRow, 3 * (blockRow + 1)):
      for colIdx in range(3 * blockCol, 3 * (blockCol + 1)):
        if rowIdx != row or colIdx != col:
          blockHints.update(self.board[rowIdx][colIdx].hints)

    myHints = self.board[row][col].hints
    return (myHints - rowHints), (myHints - colHints), (myHints - blockHints)

  def isSolved(self):
    for rowIdx, row in enumerate(self.board):
      for colIdx, element in enumerate(row):
        if self.board[rowIdx][colIdx].number is None:
          return False
    return True

  def __str__(self):
    return '\n'.join([''.join([str([tile.number, '-'][tile.number is None]) for tile in row]) for row in self.board])

def solve(board, guesses=0):
  print('##################')
  print(f'guesses: {guesses}')
  print('##################')
  print(board)
  if board.isSolved():
    return board.getCode()

  board.updateAllHints()
  for rowIdx, row in enumerate(board):
    for colIdx, element in enumerate(row):
      if board[rowIdx][colIdx].number is None:
        if len(board.getHints(rowIdx, colIdx)) == 0:
          return None
        uniqueHints = board.uniqueHints(rowIdx, colIdx)
        for i, uniqueHint in enumerate(uniqueHints):
          if len(uniqueHint) > 2:
            return None
          if len(uniqueHint) == 1:
            board[rowIdx][colIdx].number = list(uniqueHint)[0]
            answer = solve(board, guesses)
            if answer is not None:
              return answer
            board[rowIdx][colIdx].number = None
            board.updateAllHints()


  # no forced moves
  for rowIdx, row in enumerate(board):
    for colIdx, element in enumerate(row):
      if board[rowIdx][colIdx].number is None:
        hints = board.getHints(rowIdx, colIdx)
        for hint in hints:
          board[rowIdx][colIdx].number = hint
          answer = solve(board, guesses + 1)
          if answer is not None:
            return answer
          board[rowIdx][colIdx].number = None
          board.updateAllHints()
  return None

if __name__ == '__main__':
  total = 0
  count = 0
  with open('../pe096.txt', 'r') as f:
    grid = None
    for line in f.readlines():
      if line.startswith('Grid'):
        if grid is not None:
          board = Board(grid)
          total += solve(board)
          print(f'finished {count+1}')
          count += 1
        grid = []
      else:
        grid.append(list([int(x), None][x == '0'] for x in line.strip()))
  print(total)