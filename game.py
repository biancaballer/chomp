import pygame
import time
import sys

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Chomp!")
screen.fill((106, 238, 252))

pygame.draw.rect(screen, (100, 25, 0), (0, 380, 400, 400))
pygame.display.flip()
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("thanks for playing!")
            pygame.quit()
            sys.exit()

