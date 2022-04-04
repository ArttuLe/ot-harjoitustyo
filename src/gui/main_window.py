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

        # Init sudoku grid
        self.grid = self.findChild(QGridLayout, "gridLayout")
        self.init_grid(self.grid)
        self.grid.setSpacing(0)

        #Initialize buttons
        self.open_sudoku = self.findChild(QPushButton, "open_sudoku")
        self.set_difficulty = self.findChild(QPushButton, "set_difficulty")
        self.check_sudoku = self.findChild(QPushButton, "check_sudoku")
        self.help_button = self.findChild(QPushButton, "help_button")
        self.status_label = self.findChild(QLabel, "status_label")
        self.diff_label = self.findChild(QLabel, "diff_label")

        #Connect buttons to functions
        self.open_sudoku.clicked.connect(self.open_a_sudoku)
        self.set_difficulty.clicked.connect(self.ask_difficulty)
        self.check_sudoku.clicked.connect(self.check)
        self.help_button.clicked.connect(self.help)




    def ask_difficulty(self):

        text, ok = QInputDialog.getText(self, 'Difficulty', 'Input difficulty of the sudoku 1-8?')
        if ok:
            self.difficulty = text
            self.diff_label.setText("Difficulty: {}".format(self.difficulty))

    def open_a_sudoku(self,):
        self.status("Solving a sudoku")
        sudoku_grid = self.sudoku.open_sudoku(int(self.difficulty))

        for i in range(self.grid.count()):
            item = self.grid.itemAt(i)
            if type(item) == QWidgetItem:
                item.widget().setText(str(sudoku_grid[i]))

    def check(self):
        sudoku_to_check = []

        for i in range(self.grid.count()):
            item = self.grid.itemAt(i)
            if type(item) == QWidgetItem:
                sudoku_to_check.append(int(item.widget().text()))

        solved = self.sudoku.check_sudoku(sudoku_to_check)

        if solved:
            self.status("Sudoku solved!")
            msg = QMessageBox()
            msg.setWindowTitle("Sudoku solved")
            msg.setText("Well done! You have correctly solved the sudoku")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec()
        else:
            self.status("Sudoku incorrect")
            msg2 = QMessageBox()
            msg2.setWindowTitle("Sudoku Incorrect")
            msg2.setText("The sudoku is not correct :( please try again...")
            msg2.setIcon(QMessageBox.Critical)
            y = msg2.exec()
    
    def help(self):
        msg = QMessageBox()
        msg.setWindowTitle("Help")
        msg.setText("Start by choosing a difficulty and then pressing the open sudoku button.")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec()

    def status(self, status):
            self.status_label.setText(status)

    def init_grid(self, grid_layout):

        for i in range(1,10):
            for j in range(1,10):
                ij = QLineEdit(str(0))
                ij.setFixedWidth(40)
                font = ij.font()
                font.setPointSize(24)
                ij.setFont(font)
                if i % 3 == 0 and j == 1:
                    ij.setStyleSheet("border : solid black;"
                        "border-width : 1px 1px 4px 4px;")
                elif i % 3 == 0 and j % 3 == 0:
                    ij.setStyleSheet("border : solid black;"
                        "border-width : 1px 4px 4px 1px;")
                elif i % 3 == 0:
                    ij.setStyleSheet("border : solid black;"
                        "border-width : 1px 1px 4px 1px;")
                elif j == 1 and i == 1:
                    ij.setStyleSheet("border : solid black;"
                        "border-width : 4px 1px 1px 4px;")
                elif i == 1 and j % 3 == 0:
                    ij.setStyleSheet("border : solid black;"
                        "border-width : 4px 4px 1px 1px;")
                elif j % 3 == 0:
                    ij.setStyleSheet("border : solid black;"
                        "border-width : 1px 4px 1px 1px;")
                elif j == 1:
                    ij.setStyleSheet("border : solid black;"
                        "border-width : 1px 1px 1px 4px;")
                elif i == 1:
                    ij.setStyleSheet("border : solid black;"
                        "border-width : 4px 1px 1px 1px;")
                else:
                    ij.setStyleSheet("border: 1px solid black;")

                grid_layout.addWidget(ij,i,j)

        return grid_layout







