
def print_board(board):
    """Prints the current state of the game board."""
    for row in board:
        print("|".join(row))

def get_move(player):
    """Asks the player for their move and returns it as a tuple (row, col)."""
    while True:
        try:
            row = int(input(f"{player}, choose a row (1-3): ")) - 1
            col = int(input(f"{player}, choose a column (1-3): ")) - 1
            if 0 <= row <= 2 and 0 <= col <= 2:
                return (row, col)
            else:
                print("Invalid move. Please choose a row and column between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

def check_win(board):
    """Checks if the game has been won and returns the winning player (either "X" or "O") or None."""
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    # No winner
    return None

def play_game():
    """Plays a game of Tic Tac Toe."""
    board = [[None] * 3 for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    while True:
        print_board(board)
        move = get_move(players[current_player])
        row, col = move
        if board[row][col] is not None:
            print("That space is already taken. Please choose another.")
            continue
        board[row][col] = players[current_player]
        winner = check_win(board)
        if winner is not None:
            print_board(board)
            print(f"{winner} wins!")
            break
        if all(all(row) for row in board):
            print_board(board)
            print("Tie game!")
            break
        current_player = (current_player + 1) % 2
    play_again = input("Play again? (y/n): ")
    if play_again.lower() == "y":
        play_game()

def print_board(board):
    """Prints the current state of the game board."""
    for row in board:
        print("|".join(str(cell) if cell is not None else " " for cell in row))

play_game()
