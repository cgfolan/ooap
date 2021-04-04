import math
import random

SQ = math.sqrt(11)

board_graph: {
    '0' : {'1': 1,'3': 10, '4': SQ},
    '1' : {'0': 1, '2': 1,'3': SQ,'4': 10,'5': SQ},
    '2' : {'1': 1, '4': SQ, '5': 10},
    '3' : {'0': 10,'1': SQ,'4': 1,'6': 10,'7': SQ},
    '4' : {'0': SQ,'1': 10,'2': SQ,'3': 1,'5': 1,'6': SQ,'7': 10,'8': SQ},
    '5' : {'1': SQ,'4': 1,'7': SQ,'8': 10},
    '6' : {'3': 10,'4': SQ},
    '7' : {'6': 1,'8': 1,'3': SQ,'4': 10,'5': SQ},
    '8' : {'4': SQ, '5': 10, '7': 1}
}

# List of empty cells to populate the board
board_list = [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' ']]

#function to display the game board
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

#Tracks the last square played for search purposes. Set to str in case of computer playing first
last_square = 'first_move'

#Tracks occupied squares to check user imput against
occupied_squares = []

#function to randomly choose first player, player is always X

coin = random.randint(1,100)

def coin_toss():
    if (coin % 2 == 0):
        print('You go first!')
    else:
        print('Computer to go first')
        

def player_move(move, player):
    occupied_squares.append(move)
    board_list.pop(move)
    board_list.insert(move, player)
    last_square = move

play_again = 'Yes'

last_square = random.randint(0,8)

while play_again == 'Yes' or 'y':
    if (coin % 2 == 0):
        player = '  X  '
        opponent = '  O  '
    else:
        player = '  O  '
        opponent = '  X  ' 
    coin_toss()
    

    while player == '  X  ' or '  O  ':
        printboard()
        if player == '  X  ':
            #Take input from user and check to see if valid
            try:
                user_move =int(input('Pick a box 1-9: '))
            except ValueError:
                print('Please pick a number 1-9')
                continue
                 # Check if input is within the range 1-9
            if user_move < 1 or user_move > 9:
                print('Illegal move! Try again.')
                continue
                # Check if square is occupied
            user_move -= 1
            if user_move in occupied_squares:
                print('Square already occupied! Try Again.')
                continue
            player_move(user_move, player)
            last_square = user_move
            printboard()
            print(occupied_squares)
            player = '  O  '
        
        elif  player == '  O  ':
            comp_move = random.randint(0,8)
            while comp_move in occupied_squares:
                comp_move = random.randint(0,8)
            player_move(comp_move,player)
            last_square = comp_move
            print(occupied_squares)    
            player = '  X  '