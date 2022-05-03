

# Architechture of the application


## Structure of the application

![](./photos/class_diagram.png)

## Logic of the program


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

