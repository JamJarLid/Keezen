#48 tiles around the board
#4 tiles for each colors' home

pavement = {}
for i in range(1,49):
    pavement[i] = [f'pos {i}']

red_goal = {}
for i in range(1,5):
    red_goal[i] = [f'goal {i}']

green_goal = {}
for i in range(1, 5):
    green_goal[i] = [f'goal {i}']

yellow_goal = {}
for i in range(1, 5):
    yellow_goal[i] = [f'goal {i}']

blue_goal = {}
for i in range(1, 5):
    blue_goal[i] = [f'goal {i}']

print(f'pavement {pavement}')
print(f'red goal {red_goal}')
print(f'green goal {green_goal}')
print(f'yellow goal {yellow_goal}')
print(f'blue goal {blue_goal}')