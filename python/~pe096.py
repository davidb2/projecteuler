def irange(start, finish):
    return xrange(start, finish+1)

class SudokuSolver:
    from itertools import chain
    EMPTY = 0
    def __init__(self, grid, size=3):
        self.missing = 0
        self.size = size
        self.min_num = 1
        self.max_num = size * size
        self.solved_grid = None
        self.grid = (
            [list(map(int, line.strip()))
                for line in grid.strip().split('\n')]
        )
        self.original_grid = [row[:] for row in self.grid]
        for row in self.grid:
            for e in row:
                self.missing += int(e == SudokuSolver.EMPTY)

    def _is_valid_row(self, r):
        row = self.grid[r]
        filtered_row = filter(lambda x: x != 0, row)
        return len(set(filtered_row)) == len(filtered_row)

    def _is_valid_col(self, c):
        col = [self.grid[r][c] for r in xrange(len(self.grid))]
        filtered_col = filter(lambda x: x != 0, col)
        return len(set(filtered_col)) == len(filtered_col)

    def _is_valid_square(self, i, j):
        r, c = self.size * (i // self.size), self.size * (j // self.size)
        vals = list(SudokuSolver.chain(*[row[c:c+self.size]
                                    for row in self.grid[r:r+self.size]]))
        filtered_vals = filter(lambda x: x != 0, vals)
        return len(set(filtered_vals)) == len(filtered_vals)

    def _is_valid_guess(self, guess, i, j):
        saved = self.grid[i][j]
        self.grid[i][j] = guess
        ans = ( self._is_valid_square(i, j) and
                self._is_valid_row(i) and
                self._is_valid_col(j)
        )
        self.grid[i][j] = saved
        return ans

    # def _is_valid_forced_row(self, r):
    #     pass
    # def _is_valid_forced_col(self, c):
    #     pass
    # def _is_valid_forced_(self, c):
    #     pass


    def _is_forced(self, i, j):
        vals = []
        for g in irange(self.min_num, self.max_num):
            if self._is_valid_guess(g, i, j):
                if vals == []:
                    vals.append(g)
                else:
                    return (False, None)
        if len(vals) == 1:
            return (True, vals[0])
        else:
            return (False, None)

    def _is_solved(self):
        return self.missing == 0

    def solve(self):
        if self._is_solved():
            self.solved_grid = [row[:] for row in self.grid]
            return self.solved_grid


        # find forced answer
        forced_nums = []
        while True:
            num_forced_ans = 0
            for i in xrange(self.max_num):
                for j in xrange(self.max_num):
                    if self.grid[i][j] == SudokuSolver.EMPTY:
                        is_forced, forced_num = self._is_forced(i, j)
                        if is_forced:
                            forced_nums.append((forced_num, i, j))
                            self.grid[i][j] = forced_num
                            self.missing -= 1
                            num_forced_ans += 1
            if num_forced_ans == 0:
                break

        # print self.missing

        # if self.grid[0][2] == 5:
        # import numpy as np
        # print np.matrix(self.grid)
        # raw_input()

        valid_guesses = {}
        for r in xrange(self.max_num):
            for c in xrange(self.max_num):
                for guess in irange(self.min_num, self.max_num):
                    if self.grid[r][c] == SudokuSolver.EMPTY:
                        if self._is_valid_guess(guess, r, c):
                            if (r, c) not in valid_guesses:
                                valid_guesses[(r, c)] = []
                            valid_guesses[(r, c)].append(guess)
        valid_guesses = valid_guesses.items()
        valid_guesses.sort(key=lambda x: len(x[~0]))
        for ((r, c), arr) in valid_guesses:
            for g in arr:
                # print g, r, c
                saved = self.grid[r][c]
                self.grid[r][c] = g
                self.missing -= 1
                ans = self.solve()
                if ans is not None:
                    return ans
                else:
                    self.grid[r][c] = saved
                    self.missing += 1
        if self._is_solved():
            self.solved_grid = [row[:] for row in self.grid]
            return self.solved_grid
        else:
            for (forced_num, r, c) in forced_nums:
                self.grid[r][c] = SudokuSolver.EMPTY
                self.missing += 1








example_board = '''
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300
'''

example_board1 = '''
123020600
900305031
001806400
008102900
700000008
006708200
002609500
870203009
065010300
'''

example_board2 = '''
200080300
060070084
030500209
000105408
000000000
402706000
301007040
720040060
004010003
'''