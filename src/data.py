import pandas as pd
import numpy as np
import random
import math


class Data():

    def __init__(self,):
        self.data = self.read_data()

    def read_data(self):
        data = pd.read_csv('resources/sudoku.csv')
        data = data.to_numpy()

        return data

    def load_sudoku(self, difficulty):

        found = False

        while not found:
            num = random.randint(1, 29999)
            if difficulty == math.floor(self.data[num][4]):
                sudoku = self.data[num][1]
                found = True

        sudoku = self.str_to_int(sudoku)

        return sudoku

    def str_to_int(self, data):
        data = list(data)
        for i in range(len(data)):
            if data[i] == '.':
                data[i] = '0'

        data = list(map(int, data))
        
        return data
