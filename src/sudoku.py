import numpy as np
from data import Data


class Sudoku():

    def __init__(self):

        self.data = Data()

    def check_sudoku(self, sudoku):
        not_solved = False
        sudoku = np.reshape(np.array(sudoku), (9, 9))
        locations = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3),
                     (3, 6), (6, 0), (6, 3), (6, 6)]
        for loc in locations:
            if self.check_3x3_grid(sudoku, loc) is False:
                return not_solved

        for k in range(9):
            if self.check_column(k, sudoku) is False:
                return not_solved
            if self.check_row(k, sudoku) is False:
                return not_solved

        return True

    def open_sudoku(self, difficulty):
        sudoku = self.data.load_sudoku(difficulty)

        return sudoku

    def check_3x3_grid(self, sudoku, location):
        y_coord = location[0]
        x_coord = location[1]
        nums = set()
        print("location: ", location)

        for i in range(0, 3):
            for j in range(0, 3):
                nums.add(sudoku[y_coord+i][x_coord+j])

        if len(nums) != 9:
            return False
        return True

    def check_row(self, row, sudoku):
        nums = set()

        for i in range(9):
            nums.add(sudoku[row][i])

        if len(nums) != 9:
            return False
        return True

    def check_column(self, column, sudoku):

        nums = set()

        for i in range(9):
            nums.add(sudoku[i][column])

        if len(nums) != 9:
            return False
        return True
