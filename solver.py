class Solver:
    def __init__(self, grid):
        self.grid = grid

    def solve(self):
        empty_cell = self.find_empty_cell()

        if empty_cell == None: #if there is no empty cell in the grid, the sudoku is solved
            return True 
        else:
            y, x = empty_cell

        for i in range(1, 10): #cycle through the numbers from 1 to 9
            if self.check_valid_position(number=i, x=x, y=y):
                self.grid[y][x] = i

                if self.solve(): #recursive called this method, to try to get to the solution form this point 
                    return True
                else:
                    self.grid[y][x] = 0 #if there's no solution with that number in that position, that position's number is reset

        return False
                

    def find_empty_cell(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.grid[i][j] == 0:
                    return (i, j)
        
        return None

    def check_valid_position(self, number, x, y):
        #check current row
        for i in range(0, 9):
            if self.grid[y][i] == number:
                return False

        #check current column
        for i in range(0, 9):
            if self.grid[i][x] == number:
                return False

        #check current box
        box_x = x // 3
        box_y = y // 3

        if box_x == 0: 
            box_starting_x = 0
        elif box_x == 1:
            box_starting_x = 3
        else: 
            box_starting_x = 6

        if box_y == 0:
            box_starting_y = 0
        elif box_y == 1:
            box_starting_y = 3
        else:
            box_starting_y = 6
         
        for i in range(box_starting_y, box_starting_y + 3):
            for j in range(box_starting_x, box_starting_x + 3):
                if self.grid[i][j] == number:
                    return False

        return True

    def print_board(self):
        for i in range(0, 9): 
            for j in range(0, 9):
                if (i == 3 and j == 0) or (i == 6 and j == 0):
                    print("-----------------------")

                if j == 3 or j == 6:
                    print(" | ", end="")

                print(self.grid[i][j], end=" ")

                if j == 8:
                    print("")
                
                
                
