

# Architechture of the application


## Structure of the application

![](./photos/class_diagram.png)

## Logic of the program

The logic of the application is handled by the Sudoku and Utilities classes.

```mermaid
 classDiagram
      Sudoku "*" --> "1" Utilities
      class Utilities{
        solver
        check_row
        check_grid
      }
      class Sudoku{
          check_sudoku
          open_sudoku
          solve 
      }
```




## Core functionalities described as sequence diagrams

### Opening a sudoku to solve

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant Sudoku
  participant Data
  User->>UI: Click "choose difficulty"
  UI->>Sudoku: ask_difficulty()
  Sudoku->> Data: open_sudoku(difficulty)
  Data-->> Sudoku: sudoku
  Sudoku-->> UI: sudoku
```

### Solving and checking the sudoku

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant Sudoku
  participant Utilities
  User->>UI: Clicks "check a sudoku"
  UI->>Sudoku: check()
  Sudoku->> Utilities: check_sudoku(sudoku)
  Utilities-->> Sudoku: sudoku
  Sudoku-->> UI: sudoku
```

## Data used in the application

Sudokus are loaded into the application from a CSV-file containing unsolved sudokus.
Dataset obtained from kaggle.com and a link to the complete data is found on the README.