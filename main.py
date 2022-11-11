from browser import window
from network_brython import send, connect, close
import random
j = window.jQuery


class Square:

    def __init__(self, html_element, square_list):
        self.html_element = html_element
        self.square_list = square_list
        self.index = len(self.square_list)
        self.pawn: Pawn = None
        j(html_element).on('click', self.choose_pawn)

    def get_previous(self):
        return self.square_list[self.index - 1 if self.index > 0 else -1]

    def get_next(self):
        return self.square_list[self.index + 1 if self.index < len(self.square_list) else 0]

    def place_remove_pawn(self, pawn):
        self.pawn = pawn
        my_inner_html = j(self.html_element).html()
        new_inner_html = str(self.pawn) if my_inner_html == '' else ''
        j(self.html_element).html(new_inner_html)

    def get_pawn(self, event):
        print(self.pawn)

    def choose_pawn(self, event):
        global pavement
        if value is not None:
            if value == 1 or value == 6:
                if self in pavement:
                    move_pawn(self.pawn)
                else:
                    start_pawn(self.pawn)
            elif self in pavement:
                move_pawn(self.pawn)


class Player:

    def __init__(self, color, home):
        global players
        self.color = color
        self.pawns = []
        for i in range(4):
            self.pawns.append(Pawn(i, self.color))
        self.home = home
        for i in range(4):
            self.home[i].place_remove_pawn(self.pawns[i])
            self.pawns[i].square = self.home[i]
        players.append(self)


class Pawn:
    square = None

    def __init__(self, id, color):
        self.id = f'{color[0]}{id}'
        self.color = color

    def move(self, square: Square):
        if self.square != None:
            self.square.pawn = None
        self.square = square

    def _move_pawn(self):
        self.move_pawn(6)
        print('I moved')

    def __str__(self):
        return f"""
            <div class="pawn" id="{self.id}" style="color: {self.color}"> &#9823; </div>"""

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

# Add all squares to square_store
square_store = []
square_store.append(pavement)
square_store.append(red_goal)
square_store.append(red_home)
square_store.append(green_goal)
square_store.append(green_home)
square_store.append(blue_goal)
square_store.append(blue_home)
square_store.append(yellow_goal)
square_store.append(yellow_home)


# Create Players
players = []
red_player = Player('red', red_home)
green_player = Player('green', green_home)
blue_player = Player('blue', blue_home)
yellow_player = Player('yellow', yellow_home)


def start_pawn(pawn: Pawn):
    global value, player_index, current_player
    if value is not None:
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
        next_player()


def move_pawn(pawn: Pawn):
    global value, player_index, current_player
    if value is not None and pawn.square is not None:
        step = 0
        start_square: Square = pawn.square
        goal_square: Square = pawn.square
        while step < value:
            goal_square = goal_square.get_next()
            step += 1
        start_square.place_remove_pawn(pawn)
        pawn.move(goal_square)
        goal_square.place_remove_pawn(pawn)
        next_player()


def create_value(event):
    global value, current_player
    if value is None:
        value = random.randint(1, 6)
        j('.text-box').html(f'{current_player.color} player, you rolled a {value}!')
        print(f'Value: {value}')
        if value != 1 and value != 6:
            for square in pavement:
                if square.pawn is not None and square.pawn.color == current_player.color:
                    break
            next_player()


def next_player():
    global value, player_index, current_player
    value = None
    if player_index < len(players)-1:
        player_index += 1
    else:
        player_index = 0
    current_player = players[player_index]
    print(f'Next player #: {player_index}')


current_player: Player = players[0]
player_index = 0
value = None
j('.dice-button').on('click', create_value)
