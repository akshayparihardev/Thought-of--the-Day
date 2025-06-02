# Four in a Row Game
rows = 6
columns = 7

# Function for Initializing the game board with empty spaces
def create_board():
    board = []
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append('#')
        board.append(row)
    return board

# Function for printing the board in a user-friendly way
def print_board(board):
    for r in range(rows):
        print("|", end="")
        for c in range(columns):
            if board[r][c] == '#':
                print("   |", end="")
            else:
                print(f" {board[r][c]} |", end="")
        print()
    print("  1   2   3   4   5   6   7")

# Function to Check if the move of the user is valid
def valid_move(board, col):
    if col < 0 or col >= columns:
        print("Invalid Column Number , Please enter a number between 1 and 7")
        return False
    if board[0][col] != '#':
        print("Cannot place token here , The Column is not Empty")
        return False
    return True

# Function to place the piece in the board
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Function to find the lowest empty spot availbale to drop piece
def find_lowest_empty_spot(board, col):
    for i in range(rows - 1, -1, -1):
        if board[i][col] == '#':
            return i
    return None

# Function to check if the game is over
def check_win(board, row, col, piece):
    # Checking horizontal (rows) for win
    for r in range(rows):
        for c in range(columns - 3):
            if all(board[r][c + i] == piece for i in range(4)):
                return True

    # Checking vertical (columns) for win
    for r in range(rows - 3):
        for c in range(columns):
            if all(board[r + i][c] == piece for i in range(4)):
                return True

    # Checking diagonal ↘️ for win
    for r in range(rows - 3):
        for c in range(columns - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True

    # Checking diagonal ↗️ for win
    for r in range(3, rows):
        for c in range(columns - 3):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True

# Function to check if it's a Tie or the board is full
def is_board_full(board):
    for r in range(rows):
        for c in range(columns):
            if board[r][c] == '#':
                return False
    return True

# Function to run a Four in a Row game
def play_game():
    Player1 = 'X'
    Player2 = 'O'
    turn = 0
    board = create_board()
    print_board(board)

    while True:
        current_piece = Player1 if turn == 0 else Player2
        print(f"Player1 {current_piece}'s turn.")
        while True:
            user_input = input("Enter the column Number you want to place the Piece : (1-7) or 'quit' to exit: ")
            # 'quit' if the user does not want to play
            if user_input.lower() == 'quit':
                print("Game exited. Thanks for playing!")
                return
            try:
                col = int(user_input) - 1
            except ValueError:  # Any value other than the number like @ # $ will result in asking for a valid integer again
                print("Please enter a valid integer between 1 and 7 or 'quit'.")
                continue
            if valid_move(board, col):
                break
            else:
                print("Invalid Move")

        row = find_lowest_empty_spot(board, col)
        drop_piece(board, row, col, current_piece)
        print_board(board)

        if check_win(board, row, col, current_piece):
            print(f"Player {current_piece} Wins !")
            break

        if is_board_full(board):
            print("It's a Draw / Tie!")
            break

        turn = 1 if turn == 0 else 0

# Main Program
while True:
    try:
        play_game()
        # Replay option after a game ends
        while True:
            again = input("Would you like to play again? (y/n): ").strip().lower()
            if again in ['y', 'yes']: 
                break
            elif again in ['n', 'no']:
                print("Thanks for playing! Goodbye!")
                exit()
            else:
                print("Please enter 'y' for yes or 'n' for no.")
    # Handling Ctrl+C (KeyboardInterrupt) 
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
        exit()
