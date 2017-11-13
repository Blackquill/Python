import random
import os

fruit = ['apple', 'banana', 'orange', 'coconut', 'strawberry', 'lime', 'grapefruit', 'lemon', 'kumquat', 'blueberry', 'melon']

while True:
    word = random.choice(fruit)
    wrong_guesses = []
    right_guesses = []
    while len(wrong_guesses) < 7 and len(right_guesses) != len(list(word)):
        for letter in word:
            if letter in right_guesses:
                print(letter, end='')
            else:
                print("_", end='')
        print('')
        print('Strikes {}/7'.format(len(wrong_guesses)))
        print('')
        
        guess = input("What letter would you like to guess? ").lower()

        if len(guess) != 1:
            print('You can only guess one letter!')
            continue
        elif guess in wrong_guesses or guess in right_guesses:
            print("You already guessed that letter!")
            continue
        elif not guess.isalpha():
            print("You can only guess letters!")
            continue
        
        if guess in word:
            right_guesses.append(guess)
            if len(right_guesses) == len(list(word)):
                print("You win! The word was {}".format(word))
                break
        else:
            wrong_guesses.append(guess)
    else:
        print("You lose. The word was {}".format(word))
        
    
