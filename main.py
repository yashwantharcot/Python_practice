import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = input(f'guess the number{x}:')
        if guess < random_number:
            print('sorry,guess again')
        elif guess > random_number:
            print('soory,guess again')

    print(f'yay,congrats. you have guessed the numberb{random_number}')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'is{guess} the guess is too high')
        if feedback == 'l':
            high = guess - 1
        elif feedback == 'l':
            low = quess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly')

computer_guess(10)