import random

def play():

    user = input(f"Select your choise:- \nFor Rock type(r),\nFor Paper type(p),\nFor scissior type(s)\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "It\'s tie!!!"

    elif Is_win(user,computer):
        return "You win!"

    else:     
        return "You Lost!"


def Is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "p" and opponent == "r" ) or (player == "s" and opponent == "p"):
        return True 

print(play())