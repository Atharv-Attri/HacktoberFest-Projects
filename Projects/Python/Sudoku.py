import random
import numpy as np

#An example grid in case you don't wanna use the sudoku generator.
sudoku_grid = [
            [0, 8, 0, 4, 0, 9, 3, 6, 0],
            [2, 6, 0, 0, 0, 8, 0, 0, 4],
            [0, 7, 0, 0, 0, 1, 0, 2, 0],
            [6, 0, 4, 8, 0, 2, 0, 5, 1],
            [0, 1, 2, 7, 0, 5, 0, 0, 3],
            [0, 0, 0, 1, 0, 0, 4, 8, 0],
            [1, 0, 0, 0, 0, 0, 2, 7, 6],
            [0, 4, 0, 2, 0, 7, 0, 0, 8],
            [7, 2, 8, 0, 0, 0, 0, 0, 5]]

    
def is_possible(y, x, number, grid) :
    #Check each spot in the row to see if is possible to put the number.
    for spot in range(0, 9) :
        if grid[y][spot] == number :
            return False

    #Check each spot in the column to see if is possible to put the number.
    for spot in range(0, 9) :
        if grid[spot][x] == number :
            return False

    square_x_pos = (x//3)*3
    square_y_pos = (y//3)*3

    #Check each square to see if is possible to put the number.
    for row in range(0, 3) :
        for column in range(0, 3) :
            if grid[square_y_pos+row][square_x_pos+column] == number :
                return False
    
    return True


def generate_grid():
    #Takes the example grid and turn into an empty grid.
    global sudoku_grid
    sudoku_grid = [[0 for _ in range(9)] for _ in range(9)]

    #Solve the empty grid generating a brand new grid.
    solve()

    #Select random numbers in the grid to empty.
    for line in sudoku_grid:
        spots_to_empty = random.sample([number for number in range(9)], k=random.randint(5,7))
        
        for spot in spots_to_empty:
            line[spot] = 0
    
    #Prints out the generated grid.
    print(np.matrix(sudoku_grid))


def solve() :
    global sudoku_grid

    #Use a random sequence of numbers from 1 to 9 to prevent backtracking from taking too long on sudokus built to work agaisnt it.
    #A good example would be a sudoku grid whose first row is 9 8 7 6 5 4 3 2 1, since backtracking sudoku solvers typically uses a top-down approach.
    numbers = [number for number in range(1,10)]
    random.shuffle(numbers)
    
    #Search for a empty spot in the grid.
    for y in range(9) :
        for x in range(9) :
            if sudoku_grid[y][x] == 0 :

                #Looks every possible number to fit in that spot.
                for number in numbers:
                    if is_possible(y, x, number, sudoku_grid):
                        sudoku_grid[y][x] = number
                        
                        #Starts to recursively solve, if it results in a dead end, the algorithm returns and turn into a empty spot to start over.
                        if not solve():
                            return False
                        
                        sudoku_grid[y][x] = 0

                return True

generate_grid()

input("\nPress enter to see the solved grid.\n")
solve()
print(np.matrix(sudoku_grid))

#If you want to print the grid in table format.
'''for i in range(len(sudoku_grid)):
    for j in range(len(sudoku_grid[i])):
        if j == 0:
            print('|', end='')
        if i < len(sudoku_grid) - 1:
            print("\u0332" + str(sudoku_grid[i][j]), end='|')
        else:
            print(str(sudoku_grid[i][j]), end='|')
    print(end='\n')'''
