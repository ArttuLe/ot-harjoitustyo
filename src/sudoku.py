import numpy as np
from data import Data

from utilities import Utilities


class Sudoku():
    """Class responsible for the sudoku game
    """    

    def __init__(self):
        """Constructor for the class
        """        
        self.utils = Utilities()
        self.data = Data()

    def check_sudoku(self, sudoku):
        """Checks if the sudoku is correct or not

        Args:
            sudoku (list): sudoku to be checked

        Returns:
            boolean: True or False depending on if the sudoku is correctly solved
        """        
        sudoku = np.reshape(np.array(sudoku), (9, 9))
        locations = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3),
                     (3, 6), (6, 0), (6, 3), (6, 6)]
        for loc in locations:
            if self.utils.check_3x3_grid_gui(sudoku, loc) is False:
                return False

        for k in range(9):
            if self.utils.check_column_gui(k, sudoku) is False:
                return False
            if self.utils.check_row_gui(k, sudoku) is False:
                return False
        return True

    def open_sudoku(self, difficulty):
        """Opens a new sudoku

        Args:
            difficulty (int): Difficulty of the sudoku on a scale 1-8

        Returns:
            list: a sudoku with the desired difficulty
        """                
        sudoku = self.data.load_sudoku(difficulty)

        return sudoku

    def solve(self, sudoku):
        """Solve a sudoku

        Args:
            sudoku (list): the sudoku to be solved in a list format

        Returns:
            list: solved sudoku
        """
        sudoku = np.reshape(np.array(sudoku), (9, 9))
        self.utils.solver(sudoku)

        if sudoku is not None:
            sudoku = sudoku.flatten()
        return sudoku
