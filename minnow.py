import pygame
from settings import *


class Minnow:
    def __init__(self, x, y):
        self.right_image = pygame.image.load("assets/images/purple_fish.png").convert()
        self.right_image.set_colorkey((0, 0, 0))
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.image = self.right_image
        # creating a rectangle that defines where to paint my fish
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = True
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


