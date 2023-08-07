#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.

class Player:
    def __init__(self, checker):
        """ constructs a new Player object by initializing the checker and num_move attributes:
        """
        assert(checker == 'X' or checker == 'O')
        
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ returns a string indicating which checker the Player object is using.
        """
        return "Player " + self.checker
    
    def opponent_checker(self):
        """ returns a one-character string representing the checker of the Player object’s opponent. The method may assume that the calling Player object has a checker attribute that is either 'X' or 'O'.
        """
        if self.checker == 'O':
            return 'X'
        return 'O'
        
    def next_move(self, b):
        """ accepts a Board object b as a parameter and returns the column where the player wants to make the next move.
        """
        while True:
            user_col = input("Enter a column: ")
            if b.can_add_to(int(user_col)):
                self.num_moves += 1
                return int(user_col)
            print("Try again!")
