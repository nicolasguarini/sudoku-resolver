class Solver:
    def __init__(self, grid):
        self.grid = grid

    def solve(self):
        for i in range(1,10): #cycle through the numbers
            for j in range(0,9): #cycle through the entire grid
                for k in range(0,9):
                    if self.grid[j][k] == 0: #empty slot
                        pass

    def check_number_present(self, number, j, k):
        #check row
        for i in range(0, 9):
            if self.grid[j][i] == number:
                return True
        
        #check column
        for i in range(0, 9):
            if self.grid[i][k] == number:
                return True
     
        #check box
        box = []

        if j <= 2: #first row
            if k <= 2: #first column
                box = self.isolate_box(j1=0, j2=2, k1=0, k2=2)
            elif k >= 3 and k <= 5: #second column
                box = self.isolate_box(j1=0, j2=2, k1=3, k2=5)
            elif k >= 6 and k <= 8: #third column
                box = self.isolate_box(j1=0, j2=2, k1=6, k2=8)
        elif j >= 3 and j <= 5: #second row
            if k <= 2: #first column
                box = self.isolate_box(j1=3, j2=5, k1=0, k2=2)
            elif k >= 3 and k <= 5: #second column
                box = self.isolate_box(j1=3, j2=5, k1=3, k2=5)
            elif k >= 6 and k <= 8: #third column
                box = self.isolate_box(j1=3, j2=5, k1=6, k2=8)
        elif j >= 6 and j <= 8: #third row
            if k <= 2: #first column
                box = self.isolate_box(j1=6, j2=8, k1=0, k2=2)
            elif k >= 3 and k <= 5: #second column
                box = self.isolate_box(j1=6, j2=8, k1=3, k2=5)
            elif k >= 6 and k <= 8: #third column
                box = self.isolate_box(j1=6, j2=8, k1=6, k2=8)

        if number in box:
            return True

        return False

    def isolate_box(self, j1, j2, k1, k2):
        box = []

        for j in range(j1, j2+1):
            for k in range(k1, k2+1):
                box.append(self.grid[j][k])
                
        return box


