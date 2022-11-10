from browser import window
#import random
j = window.jQuery


class Square:

    def __init__(self, html_element, pavement):
        self.html_element = html_element
        self.pavement = pavement
        self.index = len(self.pavement)
        self.pawn: Pawn = None
        j(html_element).on('click', self.send_pawn)

    def get_previous(self):
        return self.pavement[self.index - 1 if self.index > 0 else -1]

    def get_next(self):
        return self.pavement[self.index + 1 if self.index < len(self.pavement) else 0]

    def place_remove_pawn(self, pawn):
        self.pawn = pawn
        my_inner_html = j(self.html_element).html()
        new_inner_html = str(self.pawn) if my_inner_html == '' else ''
        j(self.html_element).html(new_inner_html)

    def get_pawn(self, event):
        print(self.pawn)

    def send_pawn(self, event):
        global target_pawn
        target_pawn = self.pawn
        #print(target_pawn)


class Player:

    def __init__(self, color, home):
        self.color = color
        self.pawns = []
        for i in range(4):
            self.pawns.append(Pawn(i, self.color))
        self.home = home
        for i in range(4):
            self.home[i].place_remove_pawn(self.pawns[i])
            self.pawns[i].square = self.home[i]


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
players.append(red_player)
players.append(blue_player)
players.append(green_player)
players.append(yellow_player)


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
    print('test')
    start_square: Square = pawn.square
    goal_square: Square = pawn.square
    while i < value:
        goal_square = goal_square.get_next()
        i += 1
    start_square.place_remove_pawn(pawn)
    pawn.move(goal_square)
    goal_square.place_remove_pawn(pawn)


def create_value(event):
    value = int(2)#(random.random()*11)+
    j('.text-box').html(f'You rolled a {value}!')
    return value

async def move_turn():
    value = j('.dice-button').on('click', create_value)
    await Square.send_pawn()
    pawn = target_pawn
    move_pawn(pawn, value)
    print(f'I have moved to {pawn.square}')

# def game_loop():
#     while True:
#         current_player = players[0]

start_pawn(red_player.pawns[0])
move_turn()
