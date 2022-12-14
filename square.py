from browser import window
from Pawn import Pawn
import main
j = window.jQuery


class Square:

    def __init__(self, html_element, pavement):
        self.html_element = html_element
        self.pavement = pavement
        self.index = len(self.pavement)
        self.pawn: Pawn = None
        j(html_element).on('click', self.self_pawn)

    def get_previous(self):
        return self.pavement[self.index - 1 if self.index > 0 else -1]

    def get_next(self):
        return self.pavement[self.index + 1 if self.index < len(self.pavement) else 0]

    def place_remove_pawn(self, pawn):
        self.pawn = pawn
        my_inner_html = j(self.html_element).html()
        new_inner_html = str(self.pawn) if my_inner_html == '' else ''
        j(self.html_element).html(new_inner_html)

    def get_pawn(self, event):
        print(self.pawn)
        
    def send_pawn(self, event):
        main.target_pawn = self.pawn
        print(self.pawn)
