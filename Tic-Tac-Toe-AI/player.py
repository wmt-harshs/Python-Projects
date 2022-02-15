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
            square = input(self.letter + '\nYour tern. \nselect choice(0-8): ')

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

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #randomly choose one
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter # yourself
        other_player = 'O' if player == 'X' else 'X' # other player

        #First check if previous move is a winner
        if state.current_winner == other_player:

            #to work minimax correctly we want to store possition and score because we want to track score
            return {'position': None,
                    'score': 1 * (state.num_empty_square() + 1) if other_player == max_player else -1 * (state.num_empty_square() + 1)
                    }

        elif not state.num_empty_square(): # no empty square
            return { 'position': None, 'score': 0 }

        if player == max_player:
            best = {'position':None, 'score': -math.inf } # each score should maximize
        else:
            best = { 'position':None, 'score': math.inf } # each score should miniimize

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            
            state.make_move(possible_move, player)
            
            # step 2: recurse using minimax to simulate a game after making that move
            
            sim_score = self.minimax(state, other_player)
            
            # step 3: undo the move

            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            
            # step 4: update the dictionaries if necessary
            if player == max_player: #trying to maximize the max_player
                if sim_score['score'] > best['score']:
                    best = sim_score 
            else:
                if player == max_player: #but to minimize the other_player
                    if sim_score['score'] < best['score']:
                        best = sim_score 
        
        return best  