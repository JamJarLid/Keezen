from browser import window
import Square
j = window.jQuery

class Pawn:
    square: Square = None 

    def __init__(self, id, color):
        self.id = f'{color[0]}{id}'
        self.color = color

    def move(self, square):
        


        square.pawn = self
        self.square.pawn = None
        # my_inner_html = j(self.html_element).html()
        # new_inner_html = str(self) if my_inner_html == '' else ''
        # j(self.html_element).html(new_inner_html)

    def set_position(self, position):
        self.position = position

    def __str__(self):
        return f"""
            <div class="pawn" id="{self.id}" style="color: {self.color}"> &#9823; </div>"""
    
