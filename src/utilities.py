
class Utilities():

    def find_empty_cell(self, sudoku):

        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    return (i, j)
        return None

    def valid_num(self, sudoku, num, loc):

        for i in range(9):
            if sudoku[loc[0]][i] == num:
                return False

        for i in range(9):
            if sudoku[i][loc[1]] == num:
                return False

        row = loc[0]-loc[0] % 3
        col = loc[1]-loc[1] % 3

        for i in range(row, row+3):
            for j in range(col, col+3):
                if sudoku[i][j] == num:
                    return False
        return True

    def check_3x3_grid_gui(self, sudoku, location):
        y_coord = location[0]
        x_coord = location[1]
        nums = set()

        for i in range(0, 3):
            for j in range(0, 3):
                if 1 <= sudoku[y_coord+i][x_coord+j] <= 9:
                    nums.add(sudoku[y_coord+i][x_coord+j])

        if len(nums) != 9:
            return False
        return True

    def check_row_gui(self, row, sudoku):
        nums = set()

        for i in range(9):
            if 1 <= sudoku[row][i] <= 9:
                nums.add(sudoku[row][i])

        if len(nums) != 9:
            return False
        return True

    def check_column_gui(self, column, sudoku):

        nums = set()

        for i in range(9):
            if 1 <= sudoku[i][column] <= 9:
                nums.add(sudoku[i][column])

        if len(nums) != 9:
            return False
        return True

    def solver(self, sudoku):

        loc = self.find_empty_cell(sudoku)
        if loc is None:
            return True

        for num in range(1, 10):
            if self.valid_num(sudoku, num, loc):
                sudoku[loc[0]][loc[1]] = num
                if self.solver(sudoku):
                    return True
                sudoku[loc[0]][loc[1]] = 0
        return None
