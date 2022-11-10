from browser import window
from Pawn import Pawn
j = window.jQuery


class Player:

    def __init__(self, color, home):
        self.color = color
        self.pawns = []
        for i in range(4):
            self.pawns.append(Pawn(i, self.color))
        self.home = home
        for i in range(4):
            self.home[i].place_remove_pawn(self.pawns[i])
            self.pawns[i].square = self.home[i]
