import numpy as np
import unittest
from data import Data


class TestData(unittest.TestCase):

    def test_str_to_int(self):
        """
        Test the string to int conversion of the sudoku from the dataset
        """
        data = Data()
        sudoku_data = data.read_data()
        sudoku = sudoku_data[0][1]

        int_sudoku = data.str_to_int(sudoku)

        for num in int_sudoku:
            self.assertIsInstance(num, int)
