class Pawn:

    def __init__(self, id, color):
        self.id = f'{color[0]}{id}'
        self.color = color

    def __str__(self):
        return f"""
            <div class="pawn" id="{self.id}" style="color: {self.color}"> &#9823; </div>"""
