# 48 tiles around the board
# 4 tiles for each colors' goal

from Square import Square
from browser import window
j = window.jQuery


# Square assigment algoritm
pavement = []
def create_square(index, html_element):
    pavement.append(Square(html_element, pavement))

j('.tile').each(create_square)


def find_square(col, row):
    for s in pavement:
        if col == s.column:
            if row == s.row:
                return s
    return None


print(pavement)
