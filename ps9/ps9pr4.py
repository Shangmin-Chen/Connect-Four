#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#
from time import sleep
import random  
from ps9pr3 import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object.
        """
        assert (checker == 'X' or checker == 'O')
        assert (tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert (lookahead >= 0)

        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ returns a string representing an AIPlayer object.
        """
        return 'Player '+self.checker+' ('+self.tiebreak+', '+str(self.lookahead)+')'

    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the board, and that returns the index of the column with the maximum score.
        """
        potential_cols = []
        max_score = max(scores)
        for i in range(len(scores)):
            if scores[i] == max_score:
                potential_cols += [i]
        if self.tiebreak == 'LEFT':
            return potential_cols[0]
        elif self.tiebreak == 'RIGHT':
            return potential_cols[-1]
        elif self.tiebreak == 'RANDOM':
            return random.choice(potential_cols)

    def scores_for(self, b):
        """ takes a Board object b and determines the called AIPlayer‘s scores for the columns in b and return a list containing one score for each column.
        """
        scores = [0] * (b.width)
        for i in range(b.width):
            if b.can_add_to(i) == False:
                scores[i] = -1
            elif b.is_win_for(self.checker):
                scores[i] = 100
            elif b.is_win_for(self.opponent_checker()):
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50
            else:
                b.add_checker(self.checker, i)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opponent_score = opponent.scores_for(b)
                opponent_max_score = max(opponent_score)
                if opponent_max_score == 100:
                    scores[i] = 0
                elif opponent_max_score == 0:
                    scores[i] = 100
                elif opponent_max_score == 50:
                    scores[i] = 50
                b.remove_checker(i)
        return scores

    def next_move(self, b):
        """ overrides (i.e., replaces) the next_move method that is inherited from Player. Rather than asking the user for the next move, this version of next_move should return the called AIPlayer‘s judgment of its best possible move.
        """
        return self.max_score_column(self.scores_for(b))
