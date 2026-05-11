def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    current_player = "X"

    print("=== Two Player Tic-Tac-Toe ===")
    print("Player 1 = X")
    print("Player 2 = O")
    print("Enter row and column numbers between 0 and 2")

    while True:
        print_board(board)

        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))

            if row not in range(3) or col not in range(3):
                print("Invalid position! Try again.")
                continue

            if board[row][col] != " ":
                print("Cell already occupied! Try again.")
                continue

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter valid numbers!")

play_game()


"""Title
Two Player Tic-Tac-Toe Game in Python

Objective
To create a two-player Tic-Tac-Toe game in Python where players take turns placing symbols on a 3 × 3 board and the program checks for a winner or draw condition.

Theory
Tic-Tac-Toe is a simple two-player game played on a 3 × 3 grid. One player uses the symbol X and the other uses O. Players take turns placing their symbols in empty cells. The player who first places three matching symbols in a row, column, or diagonal wins the game.
This program implements the Tic-Tac-Toe game using Python lists, loops, functions, and conditional statements. The game board is represented using a 2D list where each cell initially contains a blank space " ".
The print_board() function is used to display the current game board after every move. It formats the board properly using rows and columns.
The check_winner() function checks whether a player has won the game. It checks:

All rows
All columns
Main diagonal
Opposite diagonal


If any row, column, or diagonal contains the same symbol (X or O), the function returns True.
The is_draw() function checks whether the board is completely filled without any winner. If no empty spaces are left, the game becomes a draw.
The main game logic is inside the play_game() function. It continuously takes input from players using a loop. The program also checks for:


Invalid positions

Already occupied cells

Invalid input values

After every move:
The board is updated.
Winner condition is checked.
Draw condition is checked
Current player changes.

The game ends when a player wins or the match becomes a draw.
Important Points

Tic-Tac-Toe Game
Two-player board game.
Played on 3 × 3 grid.

Players
Player 1 uses X.
Player 2 uses O.

Game Board
Represented using 2D list

Board Display
print_board() prints current board state.
Winner Checking
Checks rows, columns, and diagonals.

Draw Condition
Game is draw if board is full and no winner exists.


Input Validation
Checks valid row and column values.


Occupied Cell Check
Prevents overwriting existing moves.
Turn Switching
Players alternate after every move.
Exception Handling
try-except handles invalid numeric input.


Applications
Game development basics
Logic building
Python practice project

Algorithm
Start the program.
Create an empty 3 × 3 board.
Set current player as X.
Display game instructions.
Repeat until game ends:
Print the board.
Take row and column input.
Validate input position.
Check whether cell is empty.
Place current player symbol.
Check winner condition.
Check draw condition.
Switch player.
Print winner or draw message.
End the program.


Conclusion
This program implements a two-player Tic-Tac-Toe game using Python. It demonstrates the use of functions, loops, lists, conditions, and exception handling to manage game logic. The program successfully checks winning conditions, draw situations, and player turns interactively."""