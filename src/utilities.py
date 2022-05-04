
class Utilities():
    """Class for all the utility functions for the sudoku game
    """

    def find_empty_cell(self, sudoku):
        """Checks the sudoku for an empty cell where a number can be placed

        Args:
            sudoku (2d array): The sudoku in a 9x9 grid form

        Returns:
            tuple: location of the empty cell in the grid if there is one, otherwise None
        """
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    return (i, j)
        return None

    def valid_num(self, sudoku, num, loc):
        """Checks if a number can be placed in the location given

        Args:
            sudoku (2d array): _description_
            num (int): The number to be tested for validity
            loc (tuple(int)): desired location for the number to be placed

        Returns:
            boolean: True if the number can be placed in the location
        """
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
        """Checks a 3x3 sub-grid of a sudoku for duplicate numbers

        Args:
            sudoku (2d array): sudoku grid
            location (tuple(int)): location from where the check begins, and which grid to check

        Returns:
            boolean: True if no duplicates ie. grid is valid
        """
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
        """Checks the row of the complete sudoku for duplicate numbers.

        Args:
            row (int): row index
            sudoku (2d array): sudoku grid

        Returns:
            boolean: True if no duplicates found on the row
        """
        nums = set()

        for i in range(9):
            if 1 <= sudoku[row][i] <= 9:
                nums.add(sudoku[row][i])

        if len(nums) != 9:
            return False
        return True

    def check_column_gui(self, column, sudoku):
        """Checks the column of the complete sudoku for duplicates

        Args:
            column (int): column index
            sudoku (2d array): sudoku grid

        Returns:
            boolean: True if no duplicates
        """
        nums = set()

        for i in range(9):
            if 1 <= sudoku[i][column] <= 9:
                nums.add(sudoku[i][column])

        if len(nums) != 9:
            return False
        return True

    def solver(self, sudoku):
        """Recursive solver function for the application to solve the sudoku automatically

        Args:
            sudoku (2d array): sudoku

        Returns:
            boolean: True if sudoku is solved,  None if not solvable
        """
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
