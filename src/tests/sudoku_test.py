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

    def test_open_sudoku(self):

        ret_value = self.sudoku.open_sudoku(difficulty=0)

        self.assertFalse(self.sudoku.check_sudoku(ret_value))

    def test_check_sudoku(self):

        self.assertTrue(self.sudoku.check_sudoku(self.grid))

    def test_check_sudoku_false(self):

        self.grid[3][8] = 17

        self.assertFalse(self.sudoku.check_sudoku(self.grid))

    def test_solve(self):

        sudoku = self.sudoku.open_sudoku(0)

        sudoku = self.sudoku.solve(sudoku)

        self.assertTrue(self.sudoku.check_sudoku(sudoku))
