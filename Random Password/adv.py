import string
import random

if __name__ == "__main__":

    upeer_char = list(string.ascii_uppercase)
    lower_char = list(string.ascii_lowercase)
    number = list(string.digits)
    simbol = list(string.punctuation)

    up = int(input("Enter the uppers case letter you want:- "))
    low = int(input("Enter the lowers case letter you want:- "))
    num = int(input("Enter the numbers letter you want:- "))
    sim = int(input("Enter the simbols you want:- "))

    pass_up = random.sample(upeer_char, k = up)
    pass_low = random.sample(lower_char, k = low)
    pass_num = random.sample(number, k = num)
    pass_sim = random.sample(simbol, k = sim)

    password = []   
    password.extend(list(pass_up))
    password.extend(list(pass_low))
    password.extend(list(pass_num))
    password.extend(list(pass_sim))

    #random.shuffle(password, k=len(password))
    random.shuffle(password)
    print("Your password is:- " + "".join(password))
    