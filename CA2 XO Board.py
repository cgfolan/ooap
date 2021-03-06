import math
import random

play_again = 'y'


# List of empty cells to populate the board
board_list = [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' ']]

#function to display the game board
def printboard(): 
    """ 
    Prints the current board.
    """
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

#Tracks occupied squares to check user imput against, as well as computer squares 
occupied_squares = []
comp_occupied_squares = []

#function to randomly choose first player, player is always X

coin = random.randint(1,100)

def coin_toss():
    if (coin % 2 == 0):
        print('You go first!')
    else:
        print('Computer to go first')
        

def player_move(move, player):
    """
    takes the player/computer's input, marks it as occupied,
    adds the appropriate marker to the board,
    and returns the updated board"""
    occupied_squares.append(move)
    board_list.pop(move)
    board_list.insert(move, player)
    printboard()
    
    

def reset(player):
    """
    resets all relevant variables and lists for a new game
    """
    global board_list
    global occupied_squares
    global play_again
    board_list = board_list = [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' ']]
    occupied_squares = []
    player = ''
    play_again = input('Want to play again y/n?')    
    
def checkwin(player):
    """
    Checks all winning possibilites for a 3x3 board of X's and O's.
    Uses the length of occupied squares list to begin checking at
    5 turns, the fewest possible moves before a win condition in
    X's and O's. Also ends the game/
    """
    global board_list
    global occupied_squares
    global play_again
    if len(occupied_squares) > 4  :
        if  (board_list[0] == board_list[1] == board_list[2] == player or
            board_list[3] == board_list[4] == board_list[5] == player or
            board_list[6] == board_list[7] == board_list[8] == player or
            board_list[0] == board_list[3] == board_list[6] == player or
            board_list[1] == board_list[4] == board_list[7] == player or
            board_list[2] == board_list[5] == board_list[8] == player or
            board_list[0] == board_list[4] == board_list[8] == player or
            board_list[2] == board_list[4] == board_list[6] == player):
            if player == '  X  ':
                print('You win!')
            else:
                print('You lose!')
            reset(player)

def drawcheck(occupied_squares,player):
    """
    Checks for a draw condition and prints accordingly. Ends the current game
    """
    if len(occupied_squares) == 9:
        print('Draw!')
        reset(player)


def winning_pairs():
    """
    Checks through the occupied and computer_occupied lists to evaluate if any number 0-8 would return win state.
    Chooses random move otherwise.
    """
    global comp_move
    global occupied_squares
    global comp_occupied_squares
    comp_move = -1
    if ((1 and 2) or (4 and 7) or (3 and 6) in comp_occupied_squares) and (0 not in occupied_squares) and (comp_move == -1):
        comp_move = 0
    elif ((0 and 3) or (4 and 7) in comp_occupied_squares) and (1 not in occupied_squares) and (comp_move == -1):
        comp_move = 1
    elif ((0 and 1) or (4 and 6) or (5 and 8) in comp_occupied_squares) and (2 not in occupied_squares) and (comp_move == -1):
        comp_move = 2
    elif ((0 and 6) or (4 and 5) in comp_occupied_squares) and (3 not in occupied_squares) and (comp_move == -1):
        comp_move = 3
    elif ((0 and 8) or (1 and 7) or (2 and 6) or (3 and 5) in comp_occupied_squares) and (4 not in occupied_squares) and (comp_move == -1):
        comp_move = 4
    elif ((2 and 8) or (3 and 4) in comp_occupied_squares) and (5 not in occupied_squares) and (comp_move == -1):
        comp_move = 5
    elif ((0 and 3) or (2 and 4) or (7 and 8) in comp_occupied_squares) and (6 not in occupied_squares) and (comp_move == -1):
        comp_move = 6
    elif ((6 and 8) or (1 and 4) in comp_occupied_squares) and (7 not in occupied_squares) and (comp_move == -1):
        comp_move = 7
    elif ((6 and 7) or (0 and 4) or (2 and 4) in comp_occupied_squares) and (8 not in occupied_squares) and (comp_move == -1):
        comp_move = 8
    elif comp_move == -1:
        comp_move = random.randint(0,8)
    elif len(occupied_squares) < 4:
        comp_move = random.randint(0,8)



# Assigns who's playing first
if (coin % 2 == 0):
    player = '  X  '
    opponent = '  O  '
else:
    player = '  O  '
    opponent = '  X  ' 
    coin_toss()
    

while play_again == 'y':
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
            checkwin(player)
            drawcheck(occupied_squares,player)
            #sets player to computer
            player = '  O  '
        # Computer turn
        elif  player == '  O  ':
            winning_pairs()
            #randomly selects move in early stage of game
            if len(occupied_squares) < 4 :
                 comp_move = random.randint(0,8)
                 while comp_move in occupied_squares:
                    comp_move = random.randint(0,8)
            player_move(comp_move,player)
            comp_occupied_squares.append(comp_move)
            checkwin(player)
            drawcheck(occupied_squares,player)
            #sets player to user
            player = '  X  '

                        