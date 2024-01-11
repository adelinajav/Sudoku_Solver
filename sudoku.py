#finds the next row, col on the puzzle that's not filled yet 
#all the empty spaces rep -1
def empty(puzzle):
    for x in range(9):
        for y in range(9):
            if puzzle[x][y] ==-1:
                return x, y
    return None, None 

#figures out if the guess at the row/col is a valid guess with True or False
def is_valid(puzzle, guess, row, col):
    rowval = puzzle[row]
    if guess in rowval:
        return False
    
    colval = []
    for i in range(9):
        colval.append(puzzle[i][col])
    if guess in colval:
        return False
    

    rowstart = (row//3) *3
    colstart = (col//3) *3

    for r in range(rowstart, rowstart+3):
        for c in range(colstart, colstart+3):
            if puzzle[r][c] == guess:
                return False

    return True

#using backtracking to solve this sudoku puzzle
def solver(puzzle):
    row, col = empty(puzzle)

    if row is None:
        return True
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solver(puzzle):
                return True
        puzzle[row][col] = -1
    
    return False


#example:
example = [
    [5, 3, -1, -1, 7, -1, -1, -1, -1],
    [6, -1, -1, 1, 9, 5, -1, -1, -1],
    [-1, 9, 8, -1, -1, -1, -1, 6, -1],
    [8, -1, -1, -1, 6, -1, -1, -1, 3],
    [4, -1, -1, 8, -1, 3, -1, -1, 1],
    [7, -1, -1, -1, 2, -1, -1, -1, 6],
    [-1, 6, -1, -1, -1, -1, 2, 8, -1],
    [-1, -1, -1, 4, 1, 9, -1, -1, 5],
    [-1, -1, -1, -1, 8, -1, -1, 7, 9]
]

solver(example)
for row in example:
    print(row)
    
