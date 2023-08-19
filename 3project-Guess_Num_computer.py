import random

def computter_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c':
        
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is [ {guess} ] number is too high [ H ], too low [ L ], correct [ C ] ??')
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'the computer guessed your number {guess} correctly')


computter_guess(50)