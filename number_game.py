import random


#max_num = int(input("Enter the maximum guess number: "))
secret_num = random.randint(1, 10)
tries = 5

while tries != 0:
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))

        except ValueError:
            print("Please enter a number")
            continue
        else:
            break
    tries -= 1
    if guess == secret_num:
        print("You got it! {} was the number!".format(secret_num))
        while True:
            play = input('Play again? (y/n): ').lower()
            if play in ('y', 'n'):
                break
            print ('Invalid response, please enter y/n.')
        if play == 'y':
            secret_num = random.randint(1, 10)
            tries = 5
            continue
        else:
            print ('Thanks for playing!')
            break
    elif tries == 0:
        print("Sorry, the number was {}!".format(secret_num))
        while True:
            play = input('Play again? (y/n): ').lower()
            if play in ('y', 'n'):
                break
            print ('Invalid response, please enter y/n.')
        if play == 'y':
            secret_num = random.randint(1, 10)
            tries = 5
            continue
        else:
            print ('Thanks for playing!')
            break
        break
    elif guess < secret_num:
        print("{} is too low! {} guesses remaining.\n".format(guess, tries))
        continue
    elif guess > secret_num:
        print("{} is too high! {} guesses remaining.\n".format(guess, tries))
