import math
import random


A1 = ''
A2 = ''
A3 = ''
B1 = ''
B2 = ''
B3 = ''
C1 = ''
C2 = ''
C3 = ''


Row0 = '       1    2    3 '
Row1 = 'A',A1,A2,A3
Row2 = 'B',B1,B2,B3
Row3 = 'C',C1,C2,C3  

def printboard():
    print(Row0),
    print(Row1),
    print(Row2),
    print(Row3)    

occupied_squares = []

play_again = 'y'

printboard()



while play_again == 'y' or 'Yes':
    #first player chosen at random
    coin_flip = random.randint(0,100)
    if (coin_flip % 2 == 0):
        print('You go first!')
        player_counter = 'X'
    else:
        print('Computer to go first.')
        player_counter = 'O'   

# Ask for player input and check for input errors
    while player_counter == 'X':    
        # Use try block to evaluate for errors
        try:
            player_move =int(input('Pick a box 1-9: '))
            # Check in input in not an int
        except ValueError:
            print('Please pick a number 1-9')
            continue
        # Check if input is within the range 1-9
        if player_move < 0 or player_move > 9:
            print('Illegal move! Try again.')
            continue
        # Check if square is occupied
        if player_move in occupied_squares:
            print('Square already occupied! Try Again.')
        occupied_squares.append(player_move)
        

        


        



  
        

