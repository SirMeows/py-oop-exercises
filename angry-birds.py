import numpy as np

from inspect import CORO_CREATED
from types import coroutine


directions = [('n', 'north'), ('e', 'east'), ('s', 'south'), ('w', 'west')]

def win(contestant):
    print(f"{contestant} wins")


class Bird:

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def __str__(self):
        return 'bird'

class Pig:

    def __init__(self, position):
        self.position = position

    def __str__(self):
        return 'pig'

def draw_board(bird_pos, pig_pos):

    bird_symbol = 'B'
    pig_symbol = 'P'

    coordinates = [(x,y) for x in range(10) for y in range(10)]
    symbols = ['*'] * len(coordinates)
    
    for c in coordinates:

        i = coordinates.index(c)
        
        if c == (bird_pos):
            symbols[i] = bird_symbol
        if c == pig_pos:
            symbols[i] = pig_symbol
   
    splitted = np.array_split(symbols, 10)

    # TODO: print only elements, not arrays
    for elem in splitted:
        print(elem)  

class Board:
    # TODO: Add random start positions
    bird = Bird((0,0), directions[0])
    pig = Pig((9,9))

    draw_board(bird.position, pig.position)

class Workspace:

    commands = []

    def print_instructions():
        print('try to eat the pig by moving to its square! press f to move forward, press r to turn right, press l to turn left')

    # def add_command(input):
        

board = Board()

print(board.bird, board.pig)