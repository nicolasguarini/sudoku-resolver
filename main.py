from solver import Solver
import os

def main():
    """ EXAMPLE GRID:
    sudoku_grid = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    """

    grid = input_grid()

    solver = Solver(grid=grid)
    if solver.solve():
        solver.print_board()
    else:
        print("There's no solution of this board")

def input_grid():
    grid = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]

    for i in range(0, 9):
        for j in range(0, 9):
            print("Insert cell ", j+1, " of line ", i+1, ": (enter '0' for empty cell")

            number = int(input())

            if number != 0:
                grid[i][j] = number

    clear()
    return grid

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
                
if __name__ == "__main__":
    main()