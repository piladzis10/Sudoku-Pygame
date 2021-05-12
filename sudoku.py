sudoku = [
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,1,2,3],
   [0,0,0,0,0,0,4,0,5],
   [0,0,0,0,0,1,6,7,8],
]

def valid(sudoku,number, position):
    #validation for column
    for i in range(len(sudoku)):
        if sudoku[i][position[1]] == number and position[0] != i:
            return False
        
    #validation for rows
    for i in range(len(sudoku[0])):
        if sudoku[position[0]][i] == number and position[1] != i:
            return False
    
    #validation for box
    box_position_x = position[0] // 3 * 3
    box_position_y = position[1] // 3 * 3

    for i in range(box_position_x, box_position_x + 3):
        for j in range(box_position_y, box_position_y+3):
            if sudoku[i][j] == number and (i != position[0] and j != position[1]):
                return False

    return True

def find_empty(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i,j)
    return None

def solve(sudoku):
    find = find_empty(sudoku)
    if not find:
        return True
    else:
        row,col = find
    for i in range(1,10):
        if valid(sudoku, i, (row, col)):
            sudoku[row][col] = i

            if solve(sudoku):
                return True
            
            sudoku[row][col] = 0
    return False
        
def print_board(sudoku):
    for i in range(1,10):
        for j in range(1,10):
            if j == 9:
                print(sudoku[int(i-1)][int(j-1)])
            elif j % 3 == 0 and j != 9:
                print(sudoku[int(i-1)][int(j-1)], " ! ", end=" ")
            else:
                print(sudoku[int(i-1)][int(j-1)], end=" ")
        if i % 3 == 0 and i != 9:
            print("- - - - - - - - - - - - -")

solve(sudoku)
print_board(sudoku)
