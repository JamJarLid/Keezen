from browser import window
from Pawn import Pawn
j = window.jQuery


class Player:

    def __init__(self, color, home, move_pawn):
        self.color = color
        self.pawns = []
        for i in range(4):
            pawn = Pawn(i, self.color)
            #j('body').on('click', f'#{pawn.id}', lambda: move_pawn(pawn, 4))
            self.pawns.append(pawn)
        self.home = home
        for i in range(4):
            self.home[i].place_remove_pawn(self.pawns[i])
            self.pawns[i].square = self.home[i]
