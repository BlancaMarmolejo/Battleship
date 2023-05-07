from functions import *
from variables import *

# Setting up the game, creating two random boards


board_player = create_board(size)
board_com = create_board(size)

for ship_es in ship_es_list:
    boaty = create_ship_rand(ship_es, size)
    overlap(boaty, board_player, size)

for ship_es in ship_es_list:
    boaty = create_ship_rand(ship_es, size)
    overlap(boaty, board_com, size)


# Starting the game
winner = False #Flag when a player has no lives, so the active player wins
player_turn = True #Flag when it's first player's turn
first_turn = True #Flag so the first while loop doesn't change the active player 


print('Welcome to battleship')
print_board(board_player, board_com)

# While loop running until one of the players has no lives
while winner == False:

# First round is skipped, then following rounds are swaped between player and COM.
    if first_turn == True:
        first_turn = False
    else:
        if player_turn == True:
            player_turn = False
        else:
            player_turn = True

# Player's turn
    if player_turn == True:
        print('Your turn, player')
        hit = True #Flagged when there is a hit so we can shoot again
        while hit == True:
            hit = False #Disabled so the player can shoot at lease once. Must earn next shoots
            spot = player_turn_choose() #Player choose the firing coordenates
            board_com, hit = shot(spot, board_com, player_turn) #Enemy board updated with the last shot. When hit, then we can run another shot
            winner = check_winner(board_com) #Check the number of lives the enemy has left
            print_board(board_player, board_com)
            if winner == True: #Check so we don't fire again when winning
                break

# COM's turn
    else:
        print('COM turn')
        hit = True
        while hit == True:
            hit = False
            spot = com_turn() #COM get random spots
            board_player, hit = shot(spot, board_player, player_turn)
            winner = check_winner(board_player)
            print_board(board_player, board_com)
            if winner == True: 
                break
    

# Once there is a winner, a message for the player
if player_turn == True:
    print('You won')
else:
    print('You lose')

