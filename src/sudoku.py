
from numpy import diff
from data import Data

class Sudoku():

    def __init__(self):
        
        self.data = Data()


    def check_sudoku(self):
        solved = False



    def open_sudoku(self, difficulty):
        sudoku = self.data.load_sudoku(difficulty)

        return sudoku

    def is_solvable(self,sudoku):
        solvable = False


        return solvable