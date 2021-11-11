# Conway's "Game of Life" programmed using the PyGame library v2.0.1 in python 3.6

import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
BACKGROUND = (50, 50, 50)
BLOCK_COLOUR = (0, 255, 0)
BORDER_COLOUR = (0, 0, 255)
BLACK = (0, 0, 0)
# GAME_FONT = pygame.font.SysFont('Times New Roman', 30)
FPS = 60


def draw_game() -> None:
    WIN.fill(BACKGROUND)
    draw_grid()
    pygame.display.update()


def draw_grid() -> None:
    block_size = 20  # Set the size of the grid block - Ensure it is a multiple of window dimensions
    for x in range(0, WIDTH, block_size):
        for y in range(0, HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(WIN, BLACK, rect, 1)


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        draw_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False


if __name__ == "__main__":
    main()


