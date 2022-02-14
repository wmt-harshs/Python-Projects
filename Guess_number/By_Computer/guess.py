
import random

def guess(x):
    
    randum_number = random.randint(0,x)
    guess = x + 1
    while guess != randum_number:
        guess = int(input(f"Enter a guess number between 1 and {x}:- "))
        if guess < randum_number:
            print("Sorry guess again,too low number.")
        elif guess > randum_number:
            print("Sorry guess again,too high number.")

    print("Good, you sucess to guess the number.")

x = int(input("Enter highest number:- "))
guess(x)