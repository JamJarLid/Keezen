from browser import window
from Square import Square
j = window.jQuery


class Pawn:
    square = None

    def __init__(self, id, color):
        self.id = f'{color[0]}{id}'
        self.color = color

    def move(self, square: Square):
        if self.square != None:
            self.square.pawn = None
        self.square = square

    def _move_pawn(self):
        self.move_pawn(6)
        print('I moved')

    def __str__(self):
        return f"""
            <div class="pawn" id="{self.id}" style="color: {self.color}"> &#9823; </div>"""
