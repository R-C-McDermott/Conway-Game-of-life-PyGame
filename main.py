# Conway's "Game of Life" programmed using the PyGame library v2.0.1 in python 3.6

import pygame
import grid_class as gr
import numpy as np

pygame.init()

WIDTH, HEIGHT = 600, 700
BOTTOM_PANEL = 100
GAME_SURFACE_X, GAME_SURFACE_Y = WIDTH, HEIGHT - BOTTOM_PANEL
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
BLOCK_SIZE = 20
BACKGROUND = (50, 50, 50)
BLOCK_COLOUR = (0, 255, 0)
BORDER_COLOUR = (0, 0, 255)
BLACK = (0, 0, 0)
GEN_FONT = pygame.font.SysFont('consolas', 30)
INSTR_FONT = pygame.font.SysFont('consolas', 12)
FPS = 15

game_instructions = ["Click on any block within the grid to",
                     "add to the starting condition.",
                     "",
                     "press Space to begin the simulation.",
                     "",
                     "Press R to reset the game."]


# Creates a sample starting setup containing 2 stable blocks
start_conditions = np.zeros((GAME_SURFACE_X // BLOCK_SIZE, GAME_SURFACE_Y // BLOCK_SIZE), dtype=int)

start_conditions[6, 6] = 1
start_conditions[6, 7] = 1
start_conditions[7, 6] = 1
start_conditions[7, 7] = 1

start_conditions[5, 20] = 1
start_conditions[5, 21] = 1
start_conditions[6, 20] = 1
start_conditions[6, 21] = 1

start_conditions[6, 13] = 1
start_conditions[6, 12] = 1
start_conditions[7, 13] = 1
start_conditions[5, 14] = 1

start_conditions[4, 18] = 1
start_conditions[5, 18] = 1
start_conditions[6, 18] = 1
start_conditions[7, 18] = 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~ #


def get_coords(grid) -> list:
    x_vals = np.where(grid.grid_array == 1)[1]
    y_vals = np.where(grid.grid_array == 1)[0]
    coords = []
    for i in range(len(x_vals)):
        coords.append((x_vals[i] * BLOCK_SIZE, y_vals[i] * BLOCK_SIZE))
    return coords


def draw_game(grid, generation) -> None:
    WIN.fill(BACKGROUND)
    draw_grid()
    coords = get_coords(grid)
    for x, y in coords:
        pygame.draw.rect(WIN, BLOCK_COLOUR, (x, y, BLOCK_SIZE, BLOCK_SIZE))

    generation_text = GEN_FONT.render(f"Generation: {generation}", True, BLOCK_COLOUR)
    WIN.blit(generation_text, (20, HEIGHT - (BOTTOM_PANEL // 2)))

    for i in range(len(game_instructions)):
        instructions_text = INSTR_FONT.render(game_instructions[i], True, BLOCK_COLOUR)
        WIN.blit(instructions_text, (300, GAME_SURFACE_Y + (i + 1)*10))

    pygame.display.update()


def draw_grid() -> None:
    for x in range(0, GAME_SURFACE_X, BLOCK_SIZE):
        for y in range(0, GAME_SURFACE_Y, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(WIN, BLACK, rect, 1)


def main():
    clock = pygame.time.Clock()
    grid = gr.Grid(GAME_SURFACE_X, GAME_SURFACE_Y, BLOCK_SIZE, start_conditions)
    run = True
    generate = False
    generation = 0
    while run:
        clock.tick(FPS)

        draw_game(grid, generation)

        if generate and sum(sum(grid.grid_array)) != 0:
            grid.next_generation()
            generation += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            # Adds blocks to the game grid before running
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                grid.add_to_array(generate, pos, BLOCK_SIZE)
            if event.type == pygame.KEYUP:
                # Runs the current starting conditions
                if event.key == pygame.K_SPACE:
                    generate = True
                # Resets the game - gives clean array to create shapes
                if event.key == pygame.K_r:
                    generation = 0
                    grid.reset_array()
                    generate = False




if __name__ == "__main__":
    main()


