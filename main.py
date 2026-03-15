import random
import colorama
from colorama import Fore,Style,init

init(autoreset=True)

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " ",]

def display_board():
    print()
    print(Fore.BLUE + board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    win_condititons = [
        [0,1,2], [3,4,5], [6,7,8], #rows
        [0,3,6], [1,4,7], [2,5,8], #columns
        [0,4,8], [2,4,6] #diag
    ]

    for conditions in win_condititons:
        if board[conditions[0]] == player and \
        board[conditions[1]] == player and \
        board[conditions[2]] == player:
            return True
        return False
    

def draw():
    return " " not in board


def ai_move():
    empty_position= []
    for i in range(len(board)):
        if board[i] == " ":
            empty_position.append(i)
    move = random.choice(empty_position)
    return move

        
player_symbol = input("Choose symbol(X/O) :".upper())
if player_symbol == "X":
    ai_symbol = "O"
else:
    ai_symbol = "O"
current_player = "X"

while True:
    display_board()
    if current_player == player_symbol:
        position = int(input(f"Your Turn {player_symbol}. Choose a position 1-9 : ")) -1
        if board[position] != " ":
            print("Position is already taken. TRY AGAIN!")
            continue
        board[position] = player_symbol
    else:  #ai's turn
        position = ai_move()
        board[position] = ai_symbol
        print(f"Ai chose number {position +1}")


    #check winner

    if check_winner(current_player):
        display_board()
        if current_player == player_symbol:
            print("You win!")
        else:
            print("You lost")
        break
    if draw():
        display_board()
        print("Draw boring")
        break

    #switching user

    current_player = ai_symbol if current_player == player_symbol else player_symbol
