# 48 tiles around the board
# 4 tiles for each colors' goal

from Square import Square
from Player import Player
from browser import window
j = window.jQuery


# Square assigment
pavement = []
def create_square(index, html_element):
    pavement.append(Square(html_element, pavement))

j('.tile').each(create_square)
green_pawns = j('.greenPawns').each(create_pawn)
green_player = Player(owned_pawns = green_pawns)

# Creating players
# players= [4]
# def create_player(html_element):
#     if len(players) == 0:
#         players.append(Player(1, 'red', html_element))
#     elif len(players) == 1:
#         players.append(Player(2, 'green', html_element))
#     elif len(players) == 2:
#         players.append(Player(3, 'blue', html_element))
#     else:
#         players.append(Player(4, 'yellow', html_element))

p1 = Player(1, 'red', j())