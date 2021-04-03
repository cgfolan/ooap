import math
import random
SQ = math.sqrt(11)
board_graph: 
    'A1' : {'A2':1,'B1':10, 'B2': SQ},
    'A2' : {'A1':1, 'A3':1,'B1': SQ,'B2':10,'B3':SQ},
    'A3' : {'A2':1, 'B2':SQ, 'B3':10},
    'B1' : {'A1':10,'A2':SQ,'B2':1,'C1':10,'C2':SQ},
    'B2' : {'A1':SQ,'A2':10,'A3':SQ,'B1':1,'B3':1,'C1':SQ,'C2':10,'C3':SQ},
    'B3' : {'A2':SQ,'B2':1,'C2':SQ,'C3':10},
    'C1' : {'B1':10,'B2':SQ},
    'C2' : {'C1':1,'C3':1,'B1':SQ,'B2':10,'B3':SQ}



board_list = [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' ']]

def printboard(): 
    print('_________________________'),
    print('|       |       |       |'),
    print('|',board_list[0],'|',board_list[1],'|',board_list[2],'|'),
    print('|       |       |       |'),
    print('|-----------------------|'),
    print('|       |       |       |'),
    print('|',board_list[3],'|',board_list[4],'|',board_list[5],'|'),
    print('|       |       |       |'),
    print('|-----------------------|'),
    print('|       |       |       |'),
    print('|',board_list[6],'|',board_list[7],'|',board_list[8],'|'),
    print('|       |       |       |'),
    print('|-----------------------|')

last_move = 'first'
occupied_squares = []
play_again = 'y'

while play_again == 'y' or 'Yes':
    #first player chosen at random
    coin_flip = random.randint(0,100)
    if (coin_flip % 2 == 0):
        print('You go first!')
        player_counter = 'X'
    else:
        print('Computer to go first.')
        player_counter = 'O'   
    printboard()
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
        player_move -= 1
        occupied_squares.append(player_move)
        board_list.pop(player_move)
        board_list.insert(player_move,'  X  ')
        # last_move = player_move
        printboard()
        player_counter = 'O'

    while player_counter == 'O':
        if last_move == 'first':
            comp_move = random.randint(0,8)
            occupied_squares.append(comp_move)
            board_list.pop(comp_move)
            board_list.insert(comp_move,'  O  ')
            printboard()
            player_counter = 'X'
        



        


        



  
        

