
class Utilities():

    def find_empty_cell(self, sudoku):

        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    return (i, j)
        return None

    def valid_num_solver(self, sudoku, num, loc):

        for i in range(9):
            if sudoku[loc[0]][i] == num:
                return False
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
        print(loc)
        if loc is None:
            return sudoku

        for num in range(1, 10):
            if self.valid_num_solver(sudoku, num, loc) is True:
                sudoku[loc[0]][loc[1]] = num
                self.solver(sudoku)
            else:
                sudoku[loc[0]][loc[1]] = 0
        return None
