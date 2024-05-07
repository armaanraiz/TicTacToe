# Tic Tac Toe - 1v1 Battle in Terminal
from board import *

# Begin Game
input_turn = begin_game()

# Main Game Loop
game_running = True
current_turn = input_turn
while(game_running):
    try:        
        print("Best Move for", current_turn,": ", bot_move(board, current_turn) + 1)
        user = input("Enter X(num) | O(num) | QUIT: ")

        if user.lower() == "quit":
            print("Game Aborted... So sad to see you go")
            game_running = False
            continue
        
        if not(int(user[1]) >= 1 and int(user[1]) <= 9):
            print("Wrong Coordinates | Range is [1,9] ")
            continue
        
        if current_turn != user[0]:
            print("Incorrect Symbol")
            continue

        if user[0] == SYMBOL_X:
            if board[int(user[1])-1] == " ":
                board[int(user[1])-1] = SYMBOL_X
            else:
                print("A symbol is already present at this coordinate")
                continue
        elif user[0] == SYMBOL_O:
            if board[int(user[1])-1] == " ":
                board[int(user[1])-1] = SYMBOL_O
            else:
                print("A symbol is already present at this coordinate")
                continue
        else:
            print("Incorrect Symbol")
            continue
        
        print_board(board)

        if game_over(board):
            print(f"Game Over, {current_turn[0]} Won")
            game_running = False
        elif game_draw(board):
            print("Game Over, It's a Draw")
            game_running = False
        else:
            current_turn = flip_current_turn(current_turn)

    except Exception as error:
        print("Error")
        continue
        
