
import random

def guess(x):

    randum_number = random.randint(1,x)
    guess = 0
    while guess != randum_number:
        guess = int(input("Enter a guess nnumber:- "))
        if guess < randum_number:
            print("Sorry guess again,too low number.")
        elif guess > randum_number:
            print("Sorry guess again,too high number.")

    print("Good, you sucess to guess the number.")

guess(10)