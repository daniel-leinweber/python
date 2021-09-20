#!/usr/bin/env python3


import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while (guess != random_number):
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Congrats! You have guessed the number {random_number} correctly!')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'The computer guessed your number, {guess}, correctly!')


if __name__ == '__main__':
    game = input('Do you want to guess a number (M), or should the computer guess your number (C)? ').lower()

    if game == 'm':
        high = int(input('Please choose the maximum number: '))
        guess(high)
    elif game == 'c':
        high = int(input('Please choose the maximum number: '))
        computer_guess(high)
    else:
        print(f'Option {game} is not a valid game! Please restart...')
