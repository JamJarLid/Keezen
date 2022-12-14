from browser import window, aio
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
        if self.index > 0:
            return self.square_list[self.index -1]
        else:
            return self.square_list[-1]

    def get_next(self):
        if self.index + 1 < len(self.square_list):
            return self.square_list[self.index +1]
        elif self.square_list == pavement: 
            return self.square_list[0]
        else:
            print("Illegal move: too many steps to take")

    def place_remove_pawn(self, pawn):
        self.pawn = pawn
        my_inner_html = j(self.html_element).html()
        new_inner_html = str(self.pawn) if my_inner_html == '' else ''
        j(self.html_element).html(new_inner_html)


    def choose_pawn(self, event):
        global pavement, shared
        if self.pawn.color == current_player.color:
            if value is not None:
                if value == 1 or value == 6:
                    if self in pavement:
                        move_pawn(self.pawn)
                    else:
                        start_pawn(self.pawn)
                elif self in pavement:
                    move_pawn(self.pawn)


class Player:
    def __init__(self, color, name, home):
        global players
        self.color = color
        self.name = name
        self.pawns = []
        self.home = home
        for i in range(4):
            self.pawns.append(Pawn(i, self.color, self.home))
        for i in range(4):
            self.home[i].place_remove_pawn(self.pawns[i])
            self.pawns[i].square = self.home[i]
        players.append(self)


class Pawn:
    square = None

    def __init__(self, id, color, home):
        self.id = f'{color[0]}{id}'
        self.color = color
        self.home = home

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
homes = [red_home, green_home, blue_home, yellow_home]


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
players = []


def start_pawn(pawn: Pawn):
    global value, player_index, current_player, shared
    if value is not None:
        if pawn in red_player.pawns:
            square: Square = pavement[0]
        elif pawn in green_player.pawns:
            square = pavement[12]
        elif pawn in blue_player.pawns:
            square = pavement[24]
        elif pawn in yellow_player.pawns:
            square = pavement[36]
        # To knock a player off:
        if square.pawn is not None:
            knocked_pawn = square.pawn
            for home_square in square.pawn.home:
                if home_square.pawn is None:
                    square.place_remove_pawn(knocked_pawn)
                    square.pawn.move(home_square)
                    home_square.place_remove_pawn(knocked_pawn)
                    break
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
        step_list = []
        illegal = "Illegal move: choose another pawn or press pass"
        while step < value:
            # Check for goal position
            if goal_square == pavement[47] and pawn.color == 'red':
                goal_square = red_goal[0]
                step += 1
            elif goal_square == pavement[11] and pawn.color == 'green':
                goal_square = green_goal[0]
                step += 1
            elif goal_square == pavement[23] and pawn.color == 'blue':
                goal_square = blue_goal[0]
                step += 1
            elif goal_square == pavement[35] and pawn.color == 'gold':
                goal_square = yellow_goal[0]
                step += 1
            else:
                goal_square = goal_square.get_next()
                step_list.append(goal_square)
                step += 1
        # Home tiles blocking the path
        if pavement[0] in step_list:
            if pavement[0].pawn.color == 'red': print(illegal)
            else: pass
        elif pavement[12] in step_list:
            if pavement[12].pawn.color == 'green': print(illegal)
            else: pass
        elif pavement[24] in step_list:
            if pavement[24].pawn.color == 'blue': print(illegal)
            else: pass
        elif pavement[12] in step_list:
            if pavement[36].pawn.color == 'gold': print(illegal)
            else: pass
        else:
        # To knock a player off:
            if goal_square.pawn is not None:
                knocked_pawn: Pawn = goal_square.pawn
                for home_square in goal_square.pawn.home:
                    if home_square.pawn is None:
                        goal_square.place_remove_pawn(knocked_pawn)
                        goal_square.pawn.move(home_square)
                        home_square.place_remove_pawn(knocked_pawn)
                        break
            start_square.place_remove_pawn(pawn)
            pawn.move(goal_square)
            goal_square.place_remove_pawn(pawn)
            next_player()


def create_value(event):
    global value, current_player, pavement
    if value is None:
        value = random.randint(1, 6)
        j('.text-box').html(f'{current_player.name} player, you rolled a {value}!')
        print(f'Value: {value}')
        if value != 1 and value != 6:
            for square in pavement:
                if square.pawn is not None:
                    if square.pawn.color == current_player.color:
                        break
            else: next_player()


def next_player():
    global value, player_index, current_player
    is_win = win_check()
    if is_win == True:
        print(f'{current_player.name} has won!')
    else:
        value = None
        if player_index < len(players)-1:
            player_index += 1
        else:
            player_index = 0
        current_player = players[player_index]
        print(f'Next player: {current_player.name}')


def win_check():
    global current_player
    for square in current_player.home:
        if square.pawn is None:
            return False
    else: return True
    

def pass_round(event):
    next_player()

# Initial values
red_player = None
green_player = None
blue_player = None
yellow_player = None
player_index = 0
value = None
j('.dice-button').on('click', create_value)
j('.pass-button').on('click', pass_round)


#Init
j('.message').hide()
red_player = Player('red', 'red', red_home)
green_player = Player('green', 'green', green_home)
blue_player = Player('blue', 'blue', blue_home)
yellow_player = Player('gold', 'yellow', yellow_home)
current_player: Player = players[0]