# Tic Tac Toe

board = [' ' for x in range(10)]


def print_board(board):
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("-----------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")


def insert_letter(letter, position):
    board[position] = letter


def space_is_free(position):
    return board[position] == ' '


def is_winner(bo, le):
    return (bo[1] == le and bo[2] == le and bo[3] == le) or \
           (bo[4] == le and bo[5] == le and bo[6] == le) or \
           (bo[7] == le and bo[8] == le and bo[9] == le) or \
           (bo[1] == le and bo[4] == le and bo[7] == le) or \
           (bo[2] == le and bo[5] == le and bo[8] == le) or \
           (bo[3] == le and bo[6] == le and bo[9] == le) or \
           (bo[1] == le and bo[5] == le and bo[9] == le) or \
           (bo[3] == le and bo[5] == le and bo[7] == le)


def player_move():
    run = True
    while run:
        move = input("Please select a position to enter the X between 1 to 9: ")
        try:
            move = int(move)
            if 0 < move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print("Sorry, this space is already occupied.")
            else:
                print("Please type a number between 1 and 9.")
        except:
            print("Please type a number.")


def computer_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)
    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)
    if len(edges_open) > 0:
        move = select_random(edges_open)

    return move


def select_random(lst):
    import random
    ln = len(lst)
    r = random.randrange(0, ln)
    return lst[r]


def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


