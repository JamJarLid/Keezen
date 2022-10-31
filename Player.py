from browser import window
j = window.jQuery

class Player:

    def __init__(self ,p_nr, color, html_element):
        self.p_nr = p_nr
        self.color = color
        self.html_element = html_element
        j(html_element).on('click', self.click)

    def click(self, event):
        self.draw_pawn()

    def move_pawn(self):
        j(self.html_element).html(f'<div style="color: {self.color}"> X</div>')