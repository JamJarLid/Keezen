class Square:
    entrance: Square
    exits:[Square]

    def __init__(self, column, row):
        self.column = column
        self.row = row
    
    def parse_coordinate(self.column, self.row):
        self.coordinates = f"grid-area: {self.column} / {self.row}"

    