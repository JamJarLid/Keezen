class Square:
    entrance: Square
    exits: Square
    column = 0
    row = 0

    def __init__(self, column, row):
        self.column = column
        self.row = row