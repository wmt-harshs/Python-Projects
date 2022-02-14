import random

number = int(input("Enter the number of Paasword you want:- "))

character = int(input("Enter the number of character you want:- "))

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()[]{}/\+-?|'

print(f"Your {number} different passwords are:- ")


for pas in range(number):
    password = ''
    for c in range(character):
        password += random.choice(chars)

    print(f"password = {password}")