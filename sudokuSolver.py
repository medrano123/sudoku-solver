def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet and represents it w -1
    # return row, col touple or (None,None) if there aren't any.

    #indeces are 0-8

    for r in range(9):
        for c in range(9): 
            if puzzle[r][c] == 0: #index 9 is 0-1
                return r,c

    return None,None # if no spaces in the puzzle are 0 (-1)


def is_valid(puzzle,guess,row,col):
     #figures out if valid or not
     #Return true if valid

      #sudoku rules if that number exists in that row or coulumn or 3x3 square then its not valid
      #start with row since its easiest

    row_vals = puzzle[row]

    if guess in row_vals:
        return False
    
    #column time
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col]) # for loop goes through rows and then it will append at each row/col that value
    # similarly
    # col_vals = [puzzle[i][col] for i in range(9)] 

    if guess in col_vals:
        return False

    #square time 3x3
    #have to figure out where we are
    row_start = (row // 3) * 3 # 1//3 = 0 ; 5 //3 = 1....
    col_start = (col // 3) * 3
    # basically this find which chunk we are in since there are 9, 3x3 chunks
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # if hasent returned false yet means its true
    return True

def sudoku_solver(puzzle):
    #Solve using backtrackimg
    #the puzzle is a list of lists
    #return if there is a solution
    #Step 1: Chose a place on the puzzle to make a guess
    row, col = find_next_empty(puzzle)
    #step 1.1 : if nowhere else to go then we are done as only valid inputs are allowed
    if row is None:
        return True # as we are done
    #step 2: if there is an empty spot then lets make a guess 1-9  

    for guess in range(1,10):
        #step 3: check if valid guess

        if is_valid(puzzle,guess,row,col):
            # if it is valid then we want to place it there 
            puzzle[row][col] = guess
            #step 4 recursively call this function

            if sudoku_solver(puzzle):
                return True

    #step 5 if not valid or guess doesnt solve then we need to backtrack
        puzzle[row][col] = -1 #reset guess
    # if none work then return false as its unsolvable
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(sudoku_solver(example_board))
    print(example_board)