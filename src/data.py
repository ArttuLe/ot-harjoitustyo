import random
import math
import pandas as pd


class Data():
    """Class for dealing with the sudoku data
    """    
    def __init__(self,):
        """Constructor which reads the sudokus from a csv file.
        """        
        self.data = self.read_data()

    def read_data(self):
        """Read the sudokus off of csv file

        Returns:
            numpy array: sudoku data
        """        
        data = pd.read_csv('resources/sudoku.csv')
        data = data.to_numpy()

        return data

    def load_sudoku(self, difficulty):
        """loads a sudoku off of the data with desired difficulty

        Args:
            difficulty (int): desired difficulty

        Returns:
            list: sudoku in a list format for the UI
        """
        found = False

        while not found:
            num = random.randint(1, 29999)
            if difficulty == math.floor(self.data[num][4]):
                sudoku = self.data[num][1]
                found = True

        sudoku = self.str_to_int(sudoku)

        return sudoku

    def str_to_int(self, data):
        """Converts the sudoku from a list of chars to ints.

        Returns:
            list(int): sudoku in a list format
        """        
        data = list(data)
        for i in range(len(data)):
            if data[i] == '.':
                data[i] = '0'

        data = list(map(int, data))

        return data
