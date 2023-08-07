#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

def process_move(p, b):
    """ takes two parameters: a Player object p for the player whose move is being processed, and a Board object b for the board on which the game is being played.
    """
    # Print a message that specifies whose turn it is:
    print(str(p) + "'s turn")
    # Obtain player p‘s next move by using p to call the appropriate Player method.
    next_move = p.next_move(b)
    # Apply the move to the board by using b to call the appropriate Board method.
    b.add_checker(p.checker, next_move)
    # Print a blank line, and then print board b.
    print('\n' + str(b))
    # Check to see if the move resulted in a win or a tie by using the appropriate methods in b.
    if b.is_win_for(p.checker) == True:
        print(str(p) + ' wins in ' + str(p.num_moves) + ' moves.\nCongratulations!')
        return True
    elif b.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False

class RandomPlayer(Player):
    """ Define a class called RandomPlayer that can be used for an unintelligent computer player that chooses at random from the available columns.
    """
    def __init__(self, checker):
        # inherit
        super().__init__(checker)

    # return the index of that randomly selected column.
    def next_move(self, b):
        while True:
            random_number = random.choice(range(b.width))
            if b.can_add_to(random_number):
                self.num_moves += 1
                return random_number
