import random

def play():
    user = input("'r' for rocks, 's' for scissors and 'p' for paper ")
    computer = random.choice(['r','p','s'])
    
    if user==computer:
        return 'its a tie '
    if is_win(user,computer):
        return 'you won u '
    
def is_win(player,opponent):
    
    if(player=='r' and opponent=='s') or (player=='s' and opponent=='p') \
        or (player=='p' and opponent=='r'):
            return True
print(play())