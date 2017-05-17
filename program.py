import random

print('---------------------------------------')
print('          GUESS THAT NUMBER            ')
print('---------------------------------------')
print('')

the_number = random.randint(0, 100)
guess = -1

name = input('Player, what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {}, your guess of {} was to low'.format(name, guess))
    elif guess > the_number:
        print('Sorry {}, your guess of {} was to high'.format(name, guess))
    else:
        print("Great work {}, you won, it was {}".format(name, guess))


print('done')
