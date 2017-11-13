print('Let\'s get ready to FizzBuzz!!!')
while True:
    num = int(input('What number would you like to check? '))
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 ==0:
        print('Buzz')
    else:
        print('...')
    while True:
        play = raw_input('Play again? (y/n): ').lower()
        if play in ('y', 'n'):
            break
        print ('Invalid response, please enter y/n.')
    if play == 'y':
        continue
    else:
        print ('Thanks for playing!')
        break
