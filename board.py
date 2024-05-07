from init import *

# Begins the Game with Print Statements and User Input for User's Symbol
def begin_game():
    print("Welcome to Airplane Mode Tic Tac Toe")

    input_turn = input("Who starts first: X | O: ")
    while input_turn not in (SYMBOL_X, SYMBOL_O):
        input_turn = input("Wrong Symbol: Who starts first: X | O: ")

    print("Game Input Format: X4 | O7 | QUIT")
    input_board = [str(i) for i in range(1,10)]
    print_board(input_board)
    return input_turn

# Checks if the game is over by a win
# Returns True if game is over by a win, else returns False
def game_over(board):
    win_conditions = [
        # Rows
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        # Columns
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        # Diagonals
        (0, 4, 8), (2, 4, 6)
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]]:
            if board[condition[0]] != " ":
                return True
    return False

# Checks if the game is over by a draw
# Returns True if game is over by a draw, else returns False
def game_draw(board):
    return " " not in board

# Flips the current player symbol between X and O.
# If the current turn is X, it returns O and vice versa,
def flip_current_turn(current_turn):
    return SYMBOL_O if current_turn == SYMBOL_X else SYMBOL_X

# Prints the board in Readable Game Format to the Terminal (3x3 Grid)
def print_board(board):
    for i in range(len_board):
        if (i % 3 == 0 and i != 0):
            print("|")
        print("|",board[i], end = "", sep="")
    print("|\n")

def minimax(board, depth, alpha, beta, maximizing_player):
    # Base cases
    if game_over(board):
        if maximizing_player:
            return -1  # (O) wins
        else:
            return 1   # (X) wins
    elif game_draw(board):
        return 0    # Draw

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(len_board):
            if board[i] == " ":
                board[i] = SYMBOL_O
                curr_eval = minimax(board, depth + 1, alpha, beta, False)
                board[i] = " "
                max_eval = max(max_eval, curr_eval)
                alpha = max(alpha, curr_eval)
                if beta <= alpha:
                    break  # Beta cutoff
        return max_eval
    else:
        minEval = float('inf')
        for i in range(len_board):
            if board[i] == " ":
                board[i] = SYMBOL_X
                curr_eval = minimax(board, depth + 1, alpha, beta, True)
                board[i] = " "
                minEval = min(minEval, curr_eval)
                beta = min(beta, curr_eval)
                if beta <= alpha:
                    break  # Alpha cutoff
        return minEval

def bot_move(board, bot_symbol):
    best_move = -1
    best_eval = float('-inf') if bot_symbol == SYMBOL_O else float('inf')
    for i in range(len_board):
        if board[i] == " ":
            board[i] = bot_symbol
            curr_eval = minimax(board, 0, float('-inf'), float('inf'), bot_symbol != SYMBOL_O)
            board[i] = " "
            if (bot_symbol == SYMBOL_O and curr_eval > best_eval) or (bot_symbol == SYMBOL_X and curr_eval < best_eval):
                best_eval = curr_eval
                best_move = i
    return best_move
