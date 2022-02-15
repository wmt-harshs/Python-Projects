import time
from player import GeniusComputerPlayer, Human_player

class TicTacToe:

    def __init__(self):
        self.board= [' ' for _ in range(9)] #to rep up 3x3 matrix
        self.current_winner = None #keep track of winner

    def print_board(self):
        #getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod

    def print_board_nums():
        # 0 | 1 | 2 
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == ' ']
        
        '''moves = []
        for (i,spot) in enumerate(self.board):
        ebumerate ==> ['x','x','o'] --> [(0,'x'),(1,'x'),(2,'o')]   
            if spot == ' ':
                moves.append(i)
        return moves '''

    def empty_square(self):
        return ' ' in self.board
    
    def num_empty_square(self):
        return self.board.count(' ')  #count the empty squares

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False 
    
    def winner(self, square, letter):
        #winner if 3 in row anywhere
        # First check the row first  #
        row_ind = square // 3
        row =self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        #  check col #
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #  check diagonal  #
        # but only if the square is an even number [0,2,4,6,8]
        # only possible moves to win a diadonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2,4,6]] #right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        #if all fail
        return False 
 
 
def play(game, x_player, o_player, print_game=True):
    # return the winner of the game
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    
    while game.empty_square():
        #get the move from the valid player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
    
    # function to make a move

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')  

            if game.current_winner:
                if print_game:
                    if letter == 'X':
                        print("You win!!")
                    else:
                        print("You loose!!")
                    # print(letter + ' Win!!')
                return letter    

            # after we made move , yhan alternate letter
            letter = 'O' if letter == 'X' else 'X' # switch player

        # small break
        time.sleep(0.8)
       
    if print_game:
        print("It\'s a tie!")

if __name__ == '__main__':
    x_player = Human_player('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)