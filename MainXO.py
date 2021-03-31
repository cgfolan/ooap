import math
import random
#resets the board
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

play_again = 'y'

while play_again == 'y' or 'Yes':
    #first player chosen at random
    coin_flip = random.randint(0,100)
    if (coin_flip % 2 == 0):
        print('You go first!')
        player_counter = 1
    else:
        print('Computer to go first.')
        player_counter = 0     

    while player_counter == 1:
        player_move = (input('Pick a number 1-9: '))
        if player_move != '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
            print('Input must be 0-9')
            
        


  
        

