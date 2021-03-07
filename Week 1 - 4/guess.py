import random
min = 1
max = 10

play_again = 'yes'

while play_again == 'yes' or play_again == 'y' or play_again == 'yeah':
    guess = int(input('Pick a Number from 1 to 10: '))
    comp_guess = random.randint(min, max)
    print(guess)
    print(comp_guess)
    if comp_guess == guess:
        print('You Won!')
    elif comp_guess != guess:
        print('Bad Luck...')
    play_again = input('Want to play again?')

print('Bye for now...')