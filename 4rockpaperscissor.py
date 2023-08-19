import random

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True


def play():
    user = input("what's your choice! 'r' for rock, 'p' for paper, 's' for scissors : ")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        print('it\'s tie')
        
    elif is_win(user, computer):
        print('You Win!')
    else:
        print ("you lost!")
    
play()