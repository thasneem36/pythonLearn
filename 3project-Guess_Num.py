import random

def guess(x):
    
    random_num = random.randint(1,x)
    
    guess = 0
    while guess != random_num:
        
        guess = int(input(f'Guess the number of 1 to {x}: '))
        if guess < random_num:
            print('Sorry Too low')
        elif guess > random_num:
            print('Sorry too high')
    
    print('congrats. you win. you have guessed the right number')
            
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low #could also be high b/c low = high
                    
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C) ?'.lower)
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
            
    print(f'the computer guessed {guess} correctly!')
            
computer_guess(10)