import numpy as np
from data import Data

class Sudoku():

    def __init__(self):
        
        self.data = Data()


    def check_sudoku(self, sudoku):
        not_solved = False
        sudoku = np.reshape(np.array(sudoku),(9,9))
        print("Sudoku to check: ", sudoku)

        for i in range(0,7,3):
            for j in range(0,7,3):
                if j % 3 == 0 or j == 0 and i == 0:
                    if self.check_3x3_grid(sudoku, (i,j)) == False:
                        return not_solved
                elif j % 3 == 0 or j == 0 and i == 0:
                    if self.check_3x3_grid(sudoku, (i,j)) == False:
                        return not_solved
                    
        for c in range(9):
            if self.check_column(c,sudoku) == False:
                return not_solved
            if self.check_row(c,sudoku) == False:
                return not_solved

        return True

    def open_sudoku(self, difficulty):
        sudoku = self.data.load_sudoku(difficulty)

        return sudoku

    def check_3x3_grid(self, sudoku, location):
        y = location[0]
        x = location[1]
        nums = set()
        print("location: ", location)
        
        for i in range(0,3):
            for j in range(0,3):
                nums.add(sudoku[y+i][x+j])
        
        print("Distinct numbers in a grid: ",len(nums), "Nums: ", nums)
        if len(nums) != 9:
            return False
        else:
            return True

    def check_row(self, row, sudoku):
        nums = set()

        for i in range(9):
            nums.add(sudoku[row][i])
            
        if len(nums) != 9:
            return False
        else:
            return True

    def check_column(self, column, sudoku):   
        
        nums = set()

        for i in range(9):
            nums.add(sudoku[i][column])

        if len(nums) != 9:
            return False
        else:
            return True
