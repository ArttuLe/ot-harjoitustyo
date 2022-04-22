import numpy as np
from data import Data

from utilities import Utilities


class Sudoku():

    def __init__(self):
        self.utils = Utilities()
        self.data = Data()

    def check_sudoku(self, sudoku):
        not_solved = False
        sudoku = np.reshape(np.array(sudoku), (9, 9))
        locations = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3),
                     (3, 6), (6, 0), (6, 3), (6, 6)]
        for loc in locations:
            if self.utils.check_3x3_grid_gui(sudoku, loc) is False:
                return not_solved

        for k in range(9):
            if self.utils.check_column_gui(k, sudoku) is False:
                return not_solved
            if self.utils.check_row_gui(k, sudoku) is False:
                return not_solved
        return True

    def open_sudoku(self, difficulty):
        sudoku = self.data.load_sudoku(difficulty)

        return sudoku

    def solve(self, sudoku):

        sudoku = np.reshape(np.array(sudoku), (9, 9))
        print(sudoku)
        sudoku = self.utils.solver(sudoku)
        print(sudoku)
        if sudoku is not None:
            sudoku = sudoku.flatten()

        return sudoku
