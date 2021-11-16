# grid class

import numpy as np
from scipy.ndimage import convolve


class Grid:
    def __init__(self, x_dim, y_dim, block_size, start_conditions):
        self.x_dim = x_dim # GAME_SURFACE_X
        self.y_dim = y_dim # GAME_SURFACE_Y
        self.block_size = block_size
        self.grid_x_coord = int(self.x_dim / self.block_size)
        self.grid_y_coord = int(self.y_dim / self.block_size)
        self.grid_array = start_conditions
        self.reset = start_conditions

    # Resets game array to array of zeros (empty)
    def reset_array(self):
        self.grid_array = np.zeros((self.grid_x_coord, self.grid_y_coord), dtype=int)

    # Adds block to array given the coordinates of a mouse click
    def add_to_array(self, generate, pos, block_size):
        if not generate:
            row = pos[1] // block_size
            column = pos[0] // block_size
            if self.grid_array[row, column] == 1:
                self.grid_array[row, column] = 0
            else:
                self.grid_array[row, column] = 1

    # Convolution map of the game grid to determine the outcome of the next generation
    def convolution_map(self):
        kernel = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]])

        c = convolve(self.grid_array, kernel, mode="constant")
        return c

    # Updates the game grid from the values contained in the convolution array given the rules of the game
    def next_generation(self):
        con_map = self.convolution_map()

        for x in range(self.grid_x_coord):
            for y in range(self.grid_y_coord):
                if con_map[x, y] > 3:
                    self.grid_array[x, y] = 0
                if con_map[x, y] < 2:
                    self.grid_array[x, y] = 0
                if con_map[x, y] == 3 and self.grid_array[x, y] == 0:
                    self.grid_array[x, y] = 1
                if con_map[x, y] in [2, 3] and self.grid_array[x, y] == 1:
                    self.grid_array[x, y] = 1


