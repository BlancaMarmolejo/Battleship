import numpy as np
import random

# making a board 
def create_board(size):
    return np.full((size,size), " ")

# Create random ship
def create_ship_rand(eslora, size):
    ship_rand = []
    row_rand = random.randint(0,9)
    col_rand = random.randint(0,9)
    ship_rand.append((row_rand,col_rand))
    orient = random.choice(["N","S","E","W"])

    while len(ship_rand) < eslora:
        if orient == "E":
            col_rand = col_rand - 1 
        elif orient == "W":
            col_rand = col_rand + 1
        elif orient == "N":
            row_rand = row_rand - 1
        elif orient == "S":
            row_rand = row_rand + 1

        if row_rand not in range(size) or col_rand not in range(size):
            row_rand = random.randint(0,9)
            col_rand = random.randint(0,9)
            ship_rand = []
            ship_rand.append((row_rand,col_rand))
        else:
            ship_rand.append((row_rand,col_rand))

    return ship_rand

# check a boat doesn't overlap any other boat already on the board
def overlap(ship_rand, board, size):
    ship_rand_check = True
    for spot in ship_rand:
        if board[spot] != " ":
            ship_rand_check = False
            
    if ship_rand_check == False:
        overlap(create_ship_rand(len(ship_rand), size), board, size)
                
    elif ship_rand_check == True:
        return place_ship(ship_rand, board)
    
# Place ship on the board
def place_ship(ship, board):
    for pos in ship:
        board[pos] = "O"
    return board

# Printing boardgame
def print_board(board_player, board_com):

    print("\n Player board \n")
    print(board_player)

    print("\n COM board \n")
    hidden_board = board_com.copy()
    hidden_board[hidden_board == "O"] = " "
    print(hidden_board)
    # print(board_com) # Uncomment for spying on the enemy :)

# Manual input for the player
def player_turn_choose():
    row = int(input("Please enter the row number from 0 to 9: "))
    column = int(input("Please enter the column number from 0 to 9: "))
    spot = (row, column)
    return spot

#Random input for COM
def com_turn():
    row = random.randint(0,9)
    column = random.randint(0,9)
    spot = (row, column)
    return spot


# Checking the fired shots
def shot(spot, board, player_turn):
    if board[spot] == "O":
        board[spot] = "X"
        print("Hit!")
        hit = True # Flagged so there is another shot
        

    elif board[spot] == " ":
        board[spot] = "-"
        print("Miss!")
        hit = False
        
# When input is taken, force to choose another spot
    else:
        if player_turn == True:
            print('Spot already taken!')
            spot = player_turn_choose()
        else:
            print('Random COM again')
            spot = com_turn()
        
        board, hit = shot(spot, board, player_turn)
        
    return board, hit

# Checking number of lives and if there is a winner
def check_winner(board):
    lives = np.count_nonzero(board == "O")       
    if lives == 0:
        win = True
    else:
        win = False
    return win
