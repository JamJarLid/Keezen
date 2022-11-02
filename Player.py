from browser import window
from Pawn import Pawn
j = window.jQuery

class Player:

    def __init__(self , color):
        self.color = color
        self.pawns = []
        for i in range (1,5):
            self.pawns.append(Pawn(i, self.color))
        self.home = f'.{self.color}-home'
        for i in range(0, 4):
            j(self.home).append(str(self.pawns[i]))