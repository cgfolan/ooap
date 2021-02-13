# Exercise 1
import random
min = 1
max = 10

play_again = 'Yes'

while play_again == 'Yes':
    user = int(input('Pick a number 1-10: '))
    comp = random.randint(min, max)

    while user != comp:
        if user > comp:
            print('Too High')
        else:
            print('Too Low')
        user = int(input('Guess again: '))     
    print('Correct!')
    play_again = input('Want to play again? ')       