from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from gui.components.mainwindow import Ui_Sudoku

from sudoku import Sudoku


class MainWindow(QMainWindow, Ui_Sudoku):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.sudoku = Sudoku()
        self.difficulty = 0

        # Init sudoku grid
        self.grid = self.findChild(QGridLayout, "gridLayout")
        self.init_grid(self.grid)
        self.grid.setSpacing(0)

        # Initialize buttons
        self.open_sudoku = self.findChild(QPushButton, "open_sudoku")
        self.set_difficulty = self.findChild(QPushButton, "set_difficulty")
        self.check_sudoku = self.findChild(QPushButton, "check_sudoku")
        self.help_button = self.findChild(QPushButton, "help_button")
        self.status_label = self.findChild(QLabel, "status_label")
        self.diff_label = self.findChild(QLabel, "diff_label")
        self.solver = self.findChild(QPushButton, "solve_button")

        # Connect buttons to functions
        self.open_sudoku.clicked.connect(self.open_a_sudoku)
        self.set_difficulty.clicked.connect(self.ask_difficulty)
        self.check_sudoku.clicked.connect(self.check)
        self.help_button.clicked.connect(self.help)
        self.solver.clicked.connect(self.solve)

    def solve(self):
        self.status("Status: Solving...")
        solved = self.sudoku.solve(self.sudoku_grid)

        for i in range(self.grid.count()):
            item = self.grid.itemAt(i)
            if isinstance(item, QWidgetItem):
                item.widget().setText(str(solved[i]))

    def ask_difficulty(self):
        """
        Ask user to input the difficulty of the sudoku
        """

        text, ok_ = QInputDialog.getText(
            self, 'Difficulty', 'Input difficulty of the sudoku 1-8?')
        if ok_:
            self.difficulty = text
            self.diff_label.setText("Difficulty: {}".format(self.difficulty))

    def open_a_sudoku(self,):
        """
        Opens a sudoku with the difficulty chosen
        """
        self.status("Status: Solving a sudoku")
        self.sudoku_grid = self.sudoku.open_sudoku(int(self.difficulty))

        for i in range(self.grid.count()):
            item = self.grid.itemAt(i)
            if isinstance(item, QWidgetItem):
                item.widget().setText(str(self.sudoku_grid[i]))

    def check(self):
        """
        Checks if the solved sudoku is correct
        """
        sudoku_to_check = []

        for i in range(self.grid.count()):
            item = self.grid.itemAt(i)
            if isinstance(item, QWidgetItem):
                sudoku_to_check.append(int(item.widget().text()))

        solved = self.sudoku.check_sudoku(sudoku_to_check)

        if solved:
            self.status("Status: Sudoku solved!")
            msg = QMessageBox()
            msg.setWindowTitle("Sudoku solved")
            msg.setText("Well done! You have correctly solved the sudoku")
            msg.setIcon(QMessageBox.Information)
            temp = msg.exec()
        else:
            self.status("Status: Incorrect!")
            msg2 = QMessageBox()
            msg2.setWindowTitle("Sudoku Incorrect")
            msg2.setText("The sudoku is not correct :( please try again...")
            msg2.setIcon(QMessageBox.Critical)
            temp = msg2.exec()

    def help(self):
        """
        Help button
        """
        msg = QMessageBox()
        msg.setWindowTitle("Help")
        msg.setText(
            "Start by choosing a difficulty and then pressing the open sudoku button. You can solve the sudoku by yourself or use the solver")
        msg.setIcon(QMessageBox.Information)
        temp = msg.exec()

    def status(self, status):
        """
        Set status on the UI
        """
        self.status_label.setText(status)

    def init_grid(self, grid_layout):
        """
        Initialize the sudoku grid on the UI
        """
        for i in range(1, 10):
            for j in range(1, 10):
                i_j = QLineEdit(str(0))
                i_j.setFixedWidth(40)
                font = i_j.font()
                font.setPointSize(24)
                i_j.setFont(font)
                if i % 3 == 0 and j == 1:
                    i_j.setStyleSheet("border : solid black;"
                                      "border-width : 1px 1px 4px 4px;")
                elif i % 3 == 0 and j % 3 == 0:
                    i_j.setStyleSheet("border : solid black;"
                                      "border-width : 1px 4px 4px 1px;")
                elif i % 3 == 0:
                    i_j.setStyleSheet("border : solid black;"
                                      "border-width : 1px 1px 4px 1px;")
                elif j == 1 and i == 1:
                    i_j.setStyleSheet("border : solid black;"
                                      "border-width : 4px 1px 1px 4px;")
                elif i == 1 and j % 3 == 0:
                    i_j.setStyleSheet("border : solid black;"
                                      "border-width : 4px 4px 1px 1px;")
                elif j % 3 == 0:
                    i_j.setStyleSheet("border : solid black;"
                                      "border-width : 1px 4px 1px 1px;")
                elif j == 1:
                    i_j.setStyleSheet("border : solid black;"
                                      "border-width : 1px 1px 1px 4px;")
                elif i == 1:
                    i_j.setStyleSheet("border : solid black;"
                                      "border-width : 4px 1px 1px 1px;")
                else:
                    i_j.setStyleSheet("border: 1px solid black;")

                grid_layout.addWidget(i_j, i, j)

        return grid_layout
