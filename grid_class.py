# block class

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


    def print_array(self):
        print(self.grid_array)


    def convolution_map(self):
        kernel = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]])

        c = convolve(self.grid_array, kernel, mode="constant")
        return c


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


