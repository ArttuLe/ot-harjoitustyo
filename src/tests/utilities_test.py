import unittest

from sudoku import Sudoku


class TestUtilities(unittest.TestCase):

    def setUp(self):
        """
        Init a completed sudoku for testing
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

    def test_check_row_gui(self):

        row = 0

        self.assertTrue(self.sudoku.utils.check_row_gui(row, self.grid))

    def test_check_row_gui_false(self):

        row = 0
        self.grid[0][3] = 20
        self.assertFalse(self.sudoku.utils.check_row_gui(row, self.grid))

    def test_check_column_gui(self):

        column = 0

        self.assertTrue(self.sudoku.utils.check_column_gui(column, self.grid))

    def test_check_column_gui_false(self):
        column = 0
        self.grid[2][0] = 13

        self.assertFalse(self.sudoku.utils.check_column_gui(column, self.grid))

    def test_check_3x3_grid_gui(self):

        locations = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3),
                     (3, 6), (6, 0), (6, 3), (6, 6)]

        for loc in locations:
            self.assertTrue(
                self.sudoku.utils.check_3x3_grid_gui(self.grid, loc))

    def test_valid_num(self):

        self.grid[5][3] = 0

        loc = self.sudoku.utils.find_empty_cell(self.grid)

        self.assertTrue(self.sudoku.utils.valid_num(self.grid, 7, loc))

    def test_find_empty_cell(self):

        self.grid[3][8] = 0

        empty = self.sudoku.utils.find_empty_cell(self.grid)

        self.assertEqual(empty, (3, 8))

    def test_find_empty_cell_none(self):

        empty = self.sudoku.utils.find_empty_cell(self.grid)

        self.assertIsNone(empty)
