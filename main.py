from browser import window, aio
from network_brython import send, connect, close
import random
j = window.jQuery

# game_state = {
#     'me': None,
#     'opponent_1': None,
#     'opponent_2': None,
#     'opponent_3': None,
#     'is_server': None,
#     'shared': {
#         'player_1': '',
#         'player_2': '',
#         'player_3': '',
#         'player_4': '',
#         'red_pawn_1': '',
#         'red_pawn_2': '',
#         'red_pawn_3': '',
#         'red_pawn_4': '',
#         'green_pawn_1': '',
#         'green_pawn_2': '',
#         'green_pawn_3': '',
#         'green_pawn_4': '',
#         'blue_pawn_1': '',
#         'blue_pawn_2': '',
#         'blue_pawn_3': '',
#         'blue_pawn_4': '',
#         'yellow_pawn_1': '',
#         'yellow_pawn_2': '',
#         'yellow_pawn_3': '',
#         'yellow_pawn_4': '',
#         'pavement': '',
#         'homes': '',
#     }
# }


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
        global pavement, shared
        if value is not None:
            if value == 1 or value == 6:
                if self in pavement:
                    move_pawn(self.pawn)
                    #send(game_state['shared'])
                else:
                    start_pawn(self.pawn)
                    #send(game_state['shared'])
            elif self in pavement:
                move_pawn(self.pawn)
                #send(game_state['shared'])
                


class Player:

    def __init__(self, color, name, home):
        global players
        self.color = color
        self.name = name
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

#Server initialization
# def get_opponent_and_decide_game_runner(user, message):
#     global red_player, green_player, blue_player, yellow_player
#     # who is the server (= the creator of the channel)
#     if 'created the channel' in message:
#         name = message.split("'")[1]
#         game_state['is_server'] = red_player = Player('red', name, red_home) == game_state['me']
#     # who is the opponent (= the one that joined that is not me)
#     if 'joined channel' in message:
#         name = message.split(' ')[1]
#         if name != game_state['me']:
#             game_state['opponent_1'] = blue_player = Player('blue', name, blue_home)
#         elif name != game_state['opponent_1']:
#             game_state['opponent_2'] = green_player = Player('green', name, green_home)
#         elif name != game_state['opponent_2']:
#             game_state['opponent_3'] = yellow_player = Player('yellow', name, yellow_home)


# # handler for network messages
# def on_network_message(timestamp, user, message):
#     if user == 'system':
#         get_opponent_and_decide_game_runner(user, message)
#     # key_downs (only of interest to the server)
#     global keys_down_me, keys_down_opponent
#     if game_state['is_server']:
#         if user == game_state['me'] and type(message) is list:
#             keys_down_me = set(message)
#         if user == game_state['opponent'] and type(message) is list:
#             keys_down_opponent = set(message)
#     # shared state (only of interest to the none-server)
#     if type(message) is dict and not game_state['is_server']:
#         game_state['shared'] = message
#         #redraw board?


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
homes  =[red_home, green_home, blue_home, yellow_home]

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
        pawn.square.place_remove_pawn(pawn)
        pawn.move(square)
        square.place_remove_pawn(pawn)
        # shared[f'{pawn.color}_pawn_{pawn.id[1]}'] = pawn
        # shared['pavement'] = pavement
        # shared['homes'] = homes
        next_player()


def move_pawn(pawn: Pawn):
    global value, player_index, current_player, shared
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
        # shared[f'{pawn.color}_pawn_{pawn.id[1]}'] = pawn
        # shared['pavement'] = pavement
        # shared['homes'] = homes
        next_player()


def create_value(event):
    global value, current_player, pavement
    if value is None:
        value = random.randint(1, 6)
        j('.text-box').html(f'{current_player.name} player, you rolled a {value}!')
        print(f'Value: {value}')
        if value != 1 and value != 6:
            for square in pavement:
                if square.pawn is not None and square.pawn.color == current_player.color:
                    break
            #send(game_state['shared'])
            next_player()


def next_player():
    global value, player_index, current_player
    value = None
    if player_index < len(players)-1:
        player_index += 1
    else:
        player_index = 0
    current_player = players[player_index]
    print(f'Next player #: {current_player.name}')

# Initial values
#shared = game_state['shared']
red_player = None
green_player = None
blue_player = None
yellow_player = None

player_index = 0
value = None
j('.dice-button').on('click', create_value)


#Init
j('.message').hide()
red_player = Player('red', 'red',red_home)
green_player = Player('green', 'green', green_home)
blue_player = Player('blue', 'blue', blue_home)
yellow_player = Player('yellow', 'yellow', yellow_home)
current_player: Player = players[0]

# start before game
# async def start():
#     global current_player
#     # hide some things initially
#     j('.wait, .board').hide()
#     # show the content/body (hidden by css)
#     j('body').show()
#     # connect to network
#     game_state['me'] = input('Your user name:')
#     # note: adding prefix so I don't disturb
#     # other class mates / developers using the same
#     # network library
#     channel = 'jamjarlid_keezen_' + input('Channel:')
#     connect(channel, game_state['me'], on_network_message)
#     j('.wait').show()
#     # wait for an opponent
#     while game_state['opponent_1'] == None:
#         # and game_state['opponent_2'] == None\
#         #     and game_state['opponent_3'] == None:
#         await aio.sleep(1 / 10)
#     j('.wait').hide()
#     j('.board').show()
#     # start game if i am the server
#     if game_state['is_server']:
#         shared['player_1'] = game_state['me']
#         shared['player_2'] = game_state['opponent_1']
#         shared['player_3'] = game_state['opponent_2']
#         shared['player_4'] = game_state['opponent_3']
#         shared['red_pawn_1'] = players[0].pawns[0]
#         shared['red_pawn_2'] = players[0].pawns[1]
#         shared['red_pawn_3'] = players[0].pawns[2]
#         shared['red_pawn_4'] = players[0].pawns[3]
#         shared['blue_pawn_1'] = players[1].pawns[0]
#         shared['blue_pawn_2'] = players[1].pawns[1]
#         shared['blue_pawn_3'] = players[1].pawns[2]
#         shared['blue_pawn_4'] = players[1].pawns[3]
#         shared['green_pawn_1'] = players[2].pawns[0]
#         shared['green_pawn_2'] = players[2].pawns[1]
#         shared['green_pawn_3'] = players[2].pawns[2]
#         shared['green_pawn_4'] = players[2].pawns[3]
#         shared['yellow_pawn_1'] = players[3].pawns[0]
#         shared['yellow_pawn_2'] = players[3].pawns[1]
#         shared['yellow_pawn_3'] = players[3].pawns[2]
#         shared['yellow_pawn_4'] = players[3].pawns[3]
#         shared['pavement'] = pavement
#         shared['homes'] = homes
#         current_player = players[0]
    

# # start the program by using aio.run
# aio.run(start())
