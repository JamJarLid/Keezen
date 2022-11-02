from browser import window
from Pawn import Pawn
j = window.jQuery


class Square:
    # entrance = self.get_previous()
    # exits:[Square]

    def __init__(self, html_element, pavement):
        self.html_element = html_element
        self.pavement = pavement
        self.index = len(self.pavement)
        j(html_element).on('click', self.click)
        self.p = Pawn(1, 'blue')

    def click(self, event):
        self.place_pawn()

    def get_previous(self):
        return self.pavement[self.index - 1 if self.index > 0 else -1]

    def get_next(self):
        return self.pavement[self.index + 1 if self.index < len(self.pavement) else 0]

    def place_pawn(self):
        my_inner_html = j(self.html_element).html()
        new_inner_html = str(self.p) if my_inner_html == '' else ''
        j(self.html_element).html(new_inner_html)
