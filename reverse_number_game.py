import random

tries = 5
guess_list = list(range(1, 10))

print("Guess a number from 1 to 10 and I will try and guess it!")

while tries != 0:   
    comp_guess = random.choice(guess_list)
    while True:
        check = str(input("I guess {}! Did I get it? y/n ".format(comp_guess)))
        if check in ('y', 'n'):
            break
        print('Invalid response, please enter y/n.')    
    tries -= 1
    if check.lower() == 'y':
        print("I guessed right! Your number is {}".format(comp_guess))
        while True:
            play = input('Play again? (y/n): ').lower()
            if play in ('y', 'n'):
                break
            print ('Invalid response, please enter y/n.')
        if play == 'y':
            tries = 5
            continue
        else:
            print ('Thanks for playing!')
            break
    else:
        high_low = input("Too high/low? ").lower()
        if high_low == "high":
            for num in guess_list[:]:
                if num >= comp_guess:
                    guess_list.remove(num)
        else:
            for num in guess_list[:]:
                if num <= comp_guess:
                    guess_list.remove(num)
