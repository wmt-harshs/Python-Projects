import string
import random

if __name__ == "__main__":

    upeer_char = list(string.ascii_uppercase)
    lower_char = list(string.ascii_lowercase)
    number = list(string.digits)
    simbol = list(string.punctuation)

    how_many = int(input("Enter total password you want:- "))
    up = int(input("Enter the uppers case letter you want:- "))
    low = int(input("Enter the lowers case letter you want:- "))
    num = int(input("Enter the numbers letter you want:- "))
    sim = int(input("Enter the simbols you want:- "))

    while how_many !=0:
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
               
        pn = how_many * 2 - how_many   
        print("Your " + str(pn) + " password is:- " + "".join(password))
        pn -= 1
        how_many -= 1