import random

directions = ['n', 'e', 's', 'w']
start_orientation = 'n'
max_x = 10
max_y = 10
valid_commands = ['f', 'r', 'l']
instructions = 'You are facing {start_orientation}.\nPress f to move forward\nPress r to turn right.\nPress l to turn left.\nPress enter d when you have plotted the whole course.'

def declare_winner(contestant):
    print(f"{contestant} wins")
   
class Bird:

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.glyph = 'B'

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

    def turn_left(self):
        new_index = directions.index(self.direction) -1
        self.direction = directions[new_index % len(directions)]

    def turn_right(self):
        new_index = directions.index(self.direction) +1
        self.direction = directions[new_index % len(directions)]
    
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


class Pig:

    def __init__(self, position):
        self.position = position
        self.glyph = 'P'

    def __str__(self):
        return 'pig'    


class Board:

    def row_to_str(self, row):
        return'\t'.join([str(cell) for cell in row])

    def positions_arr(self):
        arr = [[('*') for i in range(max_y)] for j in range(max_x)]
        return arr

    def render_animal(self, animal, board_repr ):
        x, y = (animal.position[0], animal.position[1])
        board_repr[y][x] = animal.glyph         

    def draw_board(self, bird, pig):
        pos_arr = self.positions_arr()

        self.render_animal(pig, pos_arr)
        self.render_animal(bird, pos_arr)

        print('\n'.join(
            [self.row_to_str(row) for row in pos_arr]
            ))


class Workspace:

    def print_instructions(self):
        print('Try to eat the pig by moving to its square!\nchain commands to create path and then reveal theresult\n' + instructions)

    def create_commands_list(self):
        commands = []
        command = input()

        while command != 'd':
            if not command in valid_commands:
                print('That is not a valid command.\n' + instructions)
            else:
                commands.append(command)
                command = input()
        return commands
     
class Game:

    def __init__(self):

        self.bird = Bird([self._rnd(max_x), self._rnd(max_y)], start_orientation)
        self.pig = Pig([self._rnd(max_x), self._rnd(max_y)])   
        self.board = Board()
        self.workspace = Workspace()

    def _rnd(self, max_size):
        return random.randint(0, max_size)

    def initialize(self):
        self.board.draw_board(self.bird, self.pig)
        self.workspace.print_instructions()

    def play(self):
        commands = self.workspace.create_commands_list()

        for action in commands:
            if action == 'f':
                self.bird.move()
            elif action == 'r':
                self.bird.turn_right()
            elif action == 'l':
                self.bird.turn_left()
            else:
                print('error: unknown input')

    def determine_winner(self):
        self._determine_winner(self.bird, self.pig)

    def _determine_winner(self, bird, pig):

        winner = ''

        if bird.position == pig.position:
            winner = bird
        elif bird.position != pig.position:
            winner = pig
        else:
            print('error')

        declare_winner(winner)

        self.board.draw_board(bird, pig)

game = Game()   

game.initialize()
game.play()
game.determine_winner()