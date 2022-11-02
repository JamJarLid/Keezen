from browser import window
from Pawn import Pawn
j = window.jQuery


class Square:

    def __init__(self, html_element, pavement):
        self.html_element = html_element
        self.pavement = pavement
        self.index = len(self.pavement)
        self.pawn:Pawn = None

    def get_previous(self):
        return self.pavement[self.index - 1 if self.index > 0 else -1]

    def get_next(self):
        return self.pavement[self.index + 1 if self.index < len(self.pavement) else 0]

    def place_pawn(self):
        my_inner_html = j(self.html_element).html()
        new_inner_html = str(self.pawn) if my_inner_html == '' else ''
        j(self.html_element).html(new_inner_html)
        self.pawn.square = self

    