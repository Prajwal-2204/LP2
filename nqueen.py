def print_board(board):
    for row in board:
        print(" ".join(row))
    print("-" * 20)


print("========== BACKTRACKING : N-QUEEN ==========")

n = int(input("Enter value of N: "))

board = [["." for _ in range(n)] for _ in range(n)]


def is_safe(board, row, col):

    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check left diagonal
    i, j = row - 1, col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False

        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row - 1, col + 1

    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False

        i -= 1
        j += 1

    return True


def solve(row):

    if row == n:
        print("Solution Found:")
        print_board(board)
        return True

    for col in range(n):

        print(f"Trying Row {row}, Col {col}")

        if is_safe(board, row, col):

            board[row][col] = "Q"

            print(f"Placed Q at ({row},{col})")
            print_board(board)

            if solve(row + 1):
                return True

            board[row][col] = "."

            print(f"Backtracking from ({row},{col})")
            print_board(board)

        else:
            print(f"Position ({row},{col}) is not safe")

    return False


if not solve(0):
    print("No Solution Found")


    """Title
N-Queen Problem Using Backtracking in Python
Objective
To place N queens on an N × N chessboard in such a way that no two queens attack each other.

Theory
The N-Queen problem is a famous Constraint Satisfaction Problem. In this problem, we have to place N queens on an N × N chessboard. The condition is that no two queens should be in the same column or diagonal.
A queen in chess can attack in the same row, same column, and both diagonals. In this program, queens are placed row by row. So, there is no need to check the same row because only one queen is placed in each row.
This program uses the backtracking technique. Backtracking means trying one possible position, checking whether it is safe, and then moving forward. If the position causes a problem later, the program removes the queen and tries another position.
The board is represented using a 2D list. A dot . shows an empty position, and Q shows a queen. The is_safe() function checks whether a queen can be placed at a particular row and column. It checks the column, left diagonal, and right diagonal.
If a safe position is found, the queen is placed there and the function recursively tries to place the next queen in the next row. If all queens are placed successfully, the solution is printed.

Important Points

N-Queen Problem
Place N queens on an N × N board.
No two queens should attack each other.

Backtracking
Try one position.
If safe, move to next row.
If not possible later, remove queen and try another position.

Board Representation
. means empty place.
Q means queen is placed.
Safe Position

Position is safe if there is no queen in:
Same column
Left diagonal
Right diagonal

Recursive Function
solve(row) calls itself for the next row.

Base Condition
If row == n, all queens are placed successfully.

Backtracking Step
If next placement fails, queen is removed:
board[row][col] = "."

Output Display
Program prints each step of placing and removing queens.

Algorithm
Start the program.
Read value of N.
Create an N × N board filled with dots.
Start solving from row 0.
For each column in the current row:
Check whether position is safe.
If safe, place queen.
Recursively solve for next row.
If solution fails, remove queen and backtrack.
If all rows are filled with queens, print solution.
If no position works, print “No Solution Found”.
End the program.

Conclusion
This program solves the N-Queen problem using backtracking. It places queens row by row and checks whether each position is safe. If a wrong placement is made, the program backtracks and tries another position. This helps in finding a valid arrangement of queens on the chessboard."""