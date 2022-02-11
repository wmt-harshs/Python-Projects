import random
from Word import Words
import string

def get_valid_word(Word):

    Word = random.choice(Words)
    while "-" in Words or " " in Words:
        Word = random.choice(Words)

    return Word.upper()

def hangman():

    Word = get_valid_word(Words)
    word_letters = set(Word) # letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user guessed

    lives = 10

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        # letter used
        # " ".join(["a","b","c"]) --> "a b c"
        print("you have" , lives , "you have used these letters: ", " ".join(used_letters))

        #what current word is (ie W - R D)
        
        word_list = (letter if letter in used_letters else "-" for letter in Word)
        print("Current Word:"," ".join(word_list))

        #getting user input
        user_letter = input("Guess the letter:- ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print("letter is not in word.")

        elif user_letter in used_letters:
            print("You already guess the word, Try another word.")
    
        else:
            print("Invalid charecter")

    if lives == 0:
        print("You died. The orignal word was ", Word)
    else:
        print("You guessed the word:- ", Word)
hangman()