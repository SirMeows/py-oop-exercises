import numpy as np
from inspect import CORO_CREATED
from types import coroutine

# coordinates = [(x,y) for x in range(10) for y in range(10)]
directions = ['n', 'e', 's', 'w']
turns = ('l', 'r')
max_x = 10
max_y = 10

def win(contestant):
    print(f"{contestant} wins")

class Bird:

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def __str__(self):
        return 'bird'

    def move_north(self):
        self.position[1] -= 1

    def move_east(self):
        self.position[0] += 1

    def move_south(self):
        self.position[1] += 1

    def move_west(self):
        self.position[0] -= 1

    def change_direction(self, index):
        self.direction = index % len(directions)

    def turn_left(self):
        new_index = directions.index(self.direction) -1
        self.change_direction(self, new_index)

    def turn_right(self):
        new_index = directions.index(self.direction) +1
        self.change_direction(self, new_index)
    
    def move(self):
        if self.direction == 'n':
            self.move_north()
        elif self.direction == 'e':
            self.move_east()
        elif self.direction == 's':
            self.move_south()
        else:
            self.direction == 'w'
            self.move_west()

    def declare_winner(self, pig):

        if self.position == pig.position:
            print('bird eats the pig')
        else:
            print('boohoo, bird fails')

class Pig:

    def __init__(self, position):
        self.position = position

    def __str__(self):
        return 'pig'

""" def draw_board(bird_pos, pig_pos):

    bird_symbol = 'B'
    pig_symbol = 'P'

    symbols = ['*'] * len(coordinates)
    
    for c in coordinates:

        i = coordinates.index(c)
        
        if c == (bird_pos):
            symbols[i] = bird_symbol
        if c == pig_pos:
            symbols[i] = pig_symbol
   
    splitted = np.array_split(symbols, 10)

    # TODO: print only elements, not arrays
    for arr in splitted:
        print(arr)   """

class Board:
    # TODO: Add random start positions
    bird = Bird((0,0), directions[0])
    pig = Pig((9,9))

    # draw_board(bird.position, pig.position)

class Workspace:

    commands = []

    def print_instructions():
        print('try to eat the pig by moving to its square! press f to move forward, press r to turn right, press l to turn left')

    # def add_command(input):
        
class Game:

    # runs app

    board = Board()
    workspace = Workspace()


    # determines whether bird wins or loses

print(coordinates)