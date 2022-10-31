from browser import window
j = window.jQuery


class Square:
    # entrance = self.get_previous()
    # exits:[Square]

    def __init__(self, html_element, pavement):
        self.html_element = html_element
        self.pavement = pavement
        self.index = len(self.pavement)
        j(html_element).on('click', self.click)

    def click(self, event):
        self.draw_pawn()

    def get_previous(self):
        return self.pavement[self.index - 1 if self.index > 0 else -1]

    def get_next(self):
        return self.pavement[self.index + 1 if self.index < len(self.pavement) else 0]
    
    def place_pawn(self):
        my_inner_html = j(self.html_element).html()
        new_inner_html = 'X' if my_inner_html == '' else ''
        j(self.html_element).html(new_inner_html)

    # def draw_pawn(self):
    #     j(self.html_element).html(f'<div style="color: {self.color}"> X</div>')
