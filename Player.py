from browser import window
from Pawn import Pawn
j = window.jQuery

class Player:

    def __init__(self , color):
        self.color = color
        self.pawns = []
        for i in range (1,5):
            self.pawns.append(Pawn(i, self.color))
        self.home = f'{self.color}-home'
        j(f'.{self.home}').html(self.pawns[0])