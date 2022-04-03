from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from gui.components.mainwindow import Ui_Sudoku

from sudoku import Sudoku

class MainWindow(QMainWindow, Ui_Sudoku):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        # Init sudoku grid
        self.grid = self.findChild(QGridLayout, "gridLayout")
        self.init_grid(self.grid)
        self.grid.setSpacing(0)

        #Initialize buttons
        self.check = self.findChild(QPushButton, "check_sudoku")
        self.open = self.findChild(QPushButton, "open_sudoku")

        #Connect buttons to functions
        self.check.clicked.connect(Sudoku.check_sudoku)
        self.open.clicked.connect(Sudoku.open_sudoku)

        self.show_layout(self.grid)


    def init_grid(self, grid_layout):
        for i in range(1,10):
            for j in range(1,10):
                ij = QLineEdit("0")
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


    def show_layout(self,grid):
        for i in range(grid.count()):
            item = grid.itemAt(i)
            if type(item) == QWidgetItem:
                print("Index: {} Value: {}".format(i, item.widget().text()))






