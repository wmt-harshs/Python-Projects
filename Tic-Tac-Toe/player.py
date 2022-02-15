import math
import random
import time

class Player:
    
    # letter is "O" or "X"
    def __init__(self, letter):
        self.letter = letter  

    # players get next move to play
    def  get_move(self, game):
        pass

class Computer_player(Player):
    
    def __init__(self, letter):
        super().__init__(letter) 
    
    def  get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class Human_player(Player):
    
    def __init__(self, letter):
        super().__init__(letter) 
    
    def  get_move(self, game):
        valid_square = False
        Value = None
        while not valid_square:
            square = input('\nYour tern. \nselect choice(0-8): ')
            
            # we'ar going to check correct value 
            # if it is not an intiger than say it's invalid
            # if the number is not avilable than also say invalid.
            
            try:
                Value = int(square)
                if Value not in game.available_moves():
                    raise ValueError
                valid_square = True #if they are successful
            except ValueError:
                        print("Invalid square, Please try again.")
        
        return Value
