from ps9pr1 import *
from ps9pr2 import *
from ps9pr3 import *
from ps9pr4 import *
b = Board(6, 7)
b.add_checkers('1211244445')
AIPlayer('X', 'LEFT', 2).scores_for(b)
