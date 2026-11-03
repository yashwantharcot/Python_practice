import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scisors")
    computer = random.choice(['r','p','s'])
    if user == computer:
        return 'IT\'s a tie'

    if is_win(user,computer):
        return 'you won!'

    return 'you lost'


def is_win(player, opponent):

    if (player == 'r' and opponent == 's') or 