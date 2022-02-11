import random

def Guess_by_computer(x):

    low = 1
    high = x
    feedback = " "

    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)  
        else:
            guess = low #high

        feedback = input(f"Is {guess} is high(H) or lower(L) or correct(C)??  ").lower()

        if feedback == "h":
            high = guess - 1

        elif feedback == "l":
            low = guess + 1
    
    print(f"Yes,computer is guess the correct number :- {guess}")

Guess_by_computer(10)