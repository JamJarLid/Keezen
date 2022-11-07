from Square import Square
from Player import Player
from Pawn import Pawn
from browser import window
j = window.jQuery


# Board initialization
# Create pavement
pavement = []


def create_square(index, html_element):
    pavement.append(Square(html_element, pavement))


j('.tile').each(create_square)

# Create goal lists
red_goal = []
green_goal = []
blue_goal = []
yellow_goal = []


def create_goal(index, html_element):
    css_class = j(html_element).attr('class')
    list = None
    if 'red' in css_class:
        list = red_goal
    elif 'green' in css_class:
        list = green_goal
    elif 'blue' in css_class:
        list = blue_goal
    elif 'yellow' in css_class:
        list = yellow_goal

    list.append(Square(html_element, list))


j('.red-goal-tile').each(create_goal)
j('.green-goal-tile').each(create_goal)
j('.blue-goal-tile').each(create_goal)
j('.yellow-goal-tile').each(create_goal)

# Create home lists
red_home = []
green_home = []
blue_home = []
yellow_home = []


def create_home(index, html_element):
    css_class = j(html_element).attr('class')
    list = None
    if 'red' in css_class:
        list = red_home
    elif 'green' in css_class:
        list = green_home
    elif 'blue' in css_class:
        list = blue_home
    elif 'yellow' in css_class:
        list = yellow_home

    list.append(Square(html_element, list))


j('.red-home').each(create_home)
j('.green-home').each(create_home)
j('.blue-home').each(create_home)
j('.yellow-home').each(create_home)

# Create Players
red_player = Player('red', red_home)
green_player = Player('green', green_home)
blue_player = Player('blue', blue_home)
yellow_player = Player('yellow', yellow_home)


def start_pawn(pawn: Pawn):
    if pawn in red_player.pawns:
        square: Square = pavement[0]
    elif pawn in green_player.pawns:
        square = pavement[12]
    elif pawn in blue_player.pawns:
        square = pavement[24]
    elif pawn in yellow_player.pawns:
        square = pavement[36]
    pawn.square.place_remove_pawn(pawn)
    pawn.move(square)
    square.place_remove_pawn(pawn)


def move_pawn(pawn: Pawn, value):
    i = 0
    start_square: Square = pawn.square
    goal_square: Square = pawn.square
    while i < value:
        goal_square = goal_square.get_next()
        i += 1
    start_square.place_remove_pawn(pawn)
    pawn.move(goal_square)
    goal_square.place_remove_pawn(pawn)


#start_pawn(red_player.pawns[0])
# print(red_player.pawns[0].square.pavement)
#move_pawn(red_player.pawns[0], 5)
#move_pawn(red_player.pawns[0], 4)
print()