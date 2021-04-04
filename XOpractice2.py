import math
import random
SQ = math.sqrt(11)
# board_graph: 
#     'A1' : {'A2':1,'B1':10, 'B2': SQ},
#     'A2' : {'A1':1, 'A3':1,'B1': SQ,'B2':10,'B3':SQ},
#     'A3' : {'A2':1, 'B2':SQ, 'B3':10},
#     'B1' : {'A1':10,'A2':SQ,'B2':1,'C1':10,'C2':SQ},
#     'B2' : {'A1':SQ,'A2':10,'A3':SQ,'B1':1,'B3':1,'C1':SQ,'C2':10,'C3':SQ},
#     'B3' : {'A2':SQ,'B2':1,'C2':SQ,'C3':10},
#     'C1' : {'B1':10,'B2':SQ},
#     'C2' : {'C1':1,'C3':1,'B1':SQ,'B2':10,'B3':SQ}



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


def player_move(move,player_counter):
    occupied_squares.append(move)
    board_list.pop(move)
    board_list.insert(move,player_counter)
    last_move = move
    

last_move = 'first'
occupied_squares = []
play_again = 'y'

while play_again == 'y' or 'Yes':
    #first player chosen at random
    coin_flip = random.randint(1,100)
    if (coin_flip % 2 == 0):
        print('You go first!')
        player_counter = '  X  '
        opposite_counter = '  O  '
        
    else:
        print('Computer to go first.')
        player_counter = '  O  ' 
        opposite_counter = '  X  '  
      
    printboard()    
# Ask for player input and check for input errors
    if player_counter == '  X  ':    
# Use try block to evaluate for errors
            try:
                user_move =int(input('Pick a box 1-9: '))
        # Check if input in not an int
            except ValueError:
                print('Please pick a number 1-9')
                continue
        # Check if input is within the range 1-9
            if user_move < 0 or user_move > 9:
                print('Illegal move! Try again.')
                continue
        # Check if square is occupied
            user_move -= 1
            if user_move in occupied_squares:
                print('Square already occupied! Try Again.')
                continue
            player_move(user_move, player_counter)
            printboard()
            opposite_counter = '  X  '
            player_counter = '  O  '
        
    
    elif player_counter == '  O  ':
            comp_move = random.randint(0,8)
            try:
                if comp_move in occupied_squares:
                    comp_move = random.randint(0,8)
                    continue
            player_move(user_move, player_counter)
            printboard()
            opposite_counter = '  X  '
            player_counter = '  O  '
    


        



        


        



  
        

