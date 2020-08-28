# HyPy Sudoku Game and Solver

A python module with both a sudoku game and a sudoku solver.

The GUI is built with pygame.


## Running

### Solving the sudoku yourself
- Run *[`__main__.py`](__main__.py)*
- From the console enter option 1 (*Solve Sudoku*).

This will open the game GUI.

### Program solving the sudoku
- Run *[`__main__.py`](__main__.py)*
- From the console enter option 2 (*Let the computer solve it*).

This should open the game GUI and the program starts filling in the puzzles.

## Sudoku solver

<img src="images/python sudoku solver.gif" width="500em" hspace=10 vspace=10/>

## Sudoku game

<img src="images/python sudoku game.png" width="500em" hspace=10 vspace=10/>


## Files
- gui (contains scripts responsible for drawing the UI)
    - [cell.py](gui/cell.py) (handles rendering & state of specific digit entry cells)
    - [board.py](gui/board.py) (handles rendering of the sudoku board)
- solver (contains script used to solve the puzzle)
	- [solver.py](solver/solver.py) (solves sudoku by backtracking)
- images (contains screenshots of this module)
- [app.py](app.py) (handles the game logic)
- [`__main__.py`](__main__.py) (application's entry point)
