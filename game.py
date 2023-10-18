import pygame
import time
import sys

# DIMENSIONS
TILE_SIZE = 64  # tiles are square height == width
SCREEN_WIDTH = 8 * TILE_SIZE
SCREEN_HEIGHT = 8 * TILE_SIZE
SAND_HEIGHT = 20

# COLORS
WATER_COLOR = (106, 238, 252)
SAND_COLOR = (100, 25, 0)
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)

pygame.draw.rect(screen, SAND_COLOR,
                 (0, SCREEN_HEIGHT-SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))
sand = pygame.image.load("assets/images/sand.png").convert()
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
sand_top.set_colorkey((0, 0, 0))
for i in range(SCREEN_WIDTH // TILE_SIZE):   # double divide for int
    screen.blit(sand, (TILE_SIZE * i, SCREEN_HEIGHT-TILE_SIZE))
    screen.blit(sand_top, (TILE_SIZE * i, SCREEN_HEIGHT-(2*TILE_SIZE)))

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("thanks for playing!")
            pygame.quit()
            sys.exit()
        pygame.display.flip()
