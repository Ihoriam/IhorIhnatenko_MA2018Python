"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    lenth = len(line)
    new_line = list(line)

    merge_help_sort(new_line)
    print new_line
    for idx in range(1, lenth):
        if new_line[idx] == new_line[idx - 1]:
            new_line[idx - 1] += new_line[idx]
            new_line[idx] = 0
    merge_help_sort(new_line)
    return new_line


def merge_help_sort(line):
    lenth = len(line)
    for idx_zero in range(lenth):
        if line[idx_zero] == 0:
            for idx_no_zero in range(idx_zero, lenth):
                if line[idx_no_zero] != 0:
                    line[idx_zero], line[idx_no_zero] = line[idx_no_zero], line[idx_zero]
                    break


class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()
        self.full = False
        self.change = False

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for col in range(self.grid_width)]
                     for row in range(self.grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        res = ''
        for i in range(self.grid_height):
            for j in range(self.grid_width):
                res += str(self.grid[i][j]) + ' '
            res += '\n'
        return res

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        offset = OFFSETS[direction]
        temp_grid = []
        if direction == UP:
            for row in range(self.grid_width):
                temp_line = []
                start = 0
                for col in range(self.grid_height):
                    temp_line.append(self.grid[start][row])
                    start += offset[0]
                temp_line = merge(temp_line)
                temp_grid.append(temp_line)
            for row in range(self.grid_height):
                for col in range(self.grid_width):
                    self.grid[row][col] = temp_grid[col][row]

        if direction == DOWN:
            for row in range(self.grid_width):
                temp_line = []
                start = self.grid_height - 1
                for col in range(self.grid_height):
                    temp_line.append(self.grid[start][row])
                    start += offset[0]
                temp_line = merge(temp_line)
                temp_grid.append(temp_line)
            for row in range(self.grid_height):
                for col in range(self.grid_width):
                    self.grid[row][col] = temp_grid[col][self.grid_height - 1 - row]

        if direction == LEFT:
            for col in range(self.grid_height):
                temp_line = []
                start = 0
                for row in range(self.grid_width):
                    temp_line.append(self.grid[col][start])
                    start += offset[1]
                temp_line = merge(temp_line)
                temp_grid.append(temp_line)
            for row in range(self.grid_height):
                for col in range(self.grid_width):
                    self.grid[row][col] = temp_grid[row][col]

        if direction == RIGHT:
            for col in range(self.grid_height):
                temp_line = []
                start = self.grid_width - 1
                for row in range(self.grid_width):
                    temp_line.append(self.grid[col][start])
                    start += offset[1]
                temp_line = merge(temp_line)
                temp_grid.append(temp_line)
            for row in range(self.grid_height):
                for col in range(self.grid_width):
                    self.grid[row][col] = temp_grid[row][self.grid_width - 1 - col]

        score = 1
        for lst in self.grid:
            for value in lst:
                score *= value
                if score == 0:
                    self.full = False
                    break
                else:
                    self.full = True

        if self.change or not self.full:
            self.new_tile()
            self.change = False

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        prob = []
        for i in range(90):
            prob.append(2)
        for i in range(10):
            prob.append(4)

        while True:
            rand_row = random.randrange(0, self.grid_height)
            rand_col = random.randrange(0, self.grid_width)
            if self.grid[rand_row][rand_col] == 0:
                self.set_tile(rand_row, rand_col,
                              prob[random.randrange(0, 100)])
                break

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

