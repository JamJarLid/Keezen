from Square import Square
from Player import Player
from browser import window
j = window.jQuery


# Board initialization
pavement = []
def create_square(index, html_element):
    pavement.append(Square(html_element, pavement))

j('.tile').each(create_square)

red_goal = []
green_goal = []
blue_goal = []
yellow_goal = []

def create_goal(index, html_element):
    css_class = j(html_element).attr('class')
    list = None
    if 'red' in css_class: list = red_goal
    elif 'green' in css_class: list = green_goal
    elif 'blue' in css_class: list = blue_goal
    elif 'yellow' in css_class: list = yellow_goal

    list.append(Square(html_element, list))

j('.red-goal-tile').each(create_goal)
j('.green-goal-tile').each(create_goal)
j('.blue-goal-tile').each(create_goal)
j('.yellow-goal-tile').each(create_goal)

red_player = Player('red')
green_player = Player('green')
blue_player = Player('blue')
yellow_player = Player('yellow')