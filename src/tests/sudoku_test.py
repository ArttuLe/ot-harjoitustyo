import unittest
from sudoku import Sudoku


class TestSudoku(unittest.TestCase):

    def setUp(self):
        """
        Init a completed sudoku for testing purposes
        """
        self.grid = [[1, 3, 9, 5, 7, 6, 8, 4, 2],
                     [2, 5, 8, 4, 9, 3, 1, 6, 7],
                     [7, 4, 6, 2, 8, 1, 9, 5, 3],
                     [9, 6, 3, 1, 4, 5, 2, 7, 8],
                     [4, 2, 7, 8, 6, 9, 3, 1, 5],
                     [8, 1, 5, 7, 3, 2, 6, 9, 4],
                     [6, 7, 4, 3, 1, 8, 5, 2, 9],
                     [5, 8, 1, 9, 2, 4, 7, 3, 6],
                     [3, 9, 2, 6, 5, 7, 4, 8, 1]]

        self.sudoku = Sudoku()

    def test_check_row(self):

        row = 0

        self.assertTrue(self.sudoku.check_row(row, self.grid))

        self.grid[0][3] = 1

        self.assertFalse(self.sudoku.check_row(row, self.grid))

    def test_check_column(self):

        column = 0

        self.assertTrue(self.sudoku.check_column(column, self.grid))

        self.grid[2][0] = 1

        self.assertFalse(self.sudoku.check_column(column, self.grid))
