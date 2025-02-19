# Function to check if a number can be placed in a given position
def is_safe(board, row, col, num):
    # Check if the number is already in the row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if the number is already in the column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check if the number is already in the 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True  # No empty cells left, puzzle is solved

    row, col = empty

    for num in range(1, 10):  # Try numbers 1 to 9
        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):  # Recursively attempt to solve with this number
                return True

            # If placing the number doesn't lead to a solution, backtrack
            board[row][col] = 0

    return False  # Trigger backtracking

# Function to find the next empty cell in the Sudoku board
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Return the position of the first empty cell
    return None

# Function to print the Sudoku board
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# Sample unsolved Sudoku puzzle (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solving the Sudoku
print("Unsolved Sudoku Puzzle:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku Puzzle:")
    print_board(sudoku_board)
else:
    print("\nNo solution exists")
