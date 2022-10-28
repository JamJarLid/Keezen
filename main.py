# 48 tiles around the board
# 4 tiles for each colors' goal

from Square import Square

# Square assigment algoritm
pavement = []
for row in range(1, 14):
    for col in range(1, 14):
        if row == 1:
            if col <= 5 and col >= 9:
                pavement.append(Square(col, row))
        elif row >= 2 and row <= 4:
            if col == 5 or col == 9:
                pavement.append(Square(col, row))
        elif row == 5:
            if col <= 5 or col >= 9:
                pavement.append(Square(col, row))
        elif row >= 6 and row <= 8:
            if col == 1 or col == 13:
                pavement.append(Square(col, row))
        elif row == 9:
            if col <= 5 or col >= 9:
                pavement.append(Square(col, row))
        elif row >= 10 and row <= 12:
            if col == 5 or col == 9:
                pavement.append(Square(col, row))
        else:
            if col <= 5 and col >= 9:
                pavement.append(Square(col, row))

    def find_square(col, row):
        for s in pavement:
            if col == s.column:
                if row == s.row:
                    return s
        return None


print(pavement)