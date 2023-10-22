import pygame
from settings import *


class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.right_image = pygame.image.load("assets/images/orange_fish.png").convert()
        self.right_image.set_colorkey((0, 0, 0))
        self.image = self.right_image
        self.left_image = pygame.transform.flip(self.image, True, False)

        self.x = x
        self.y = y
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        print("i am a brand new fish:)")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        if self.moving_left:
            self.x -= 3
            self.image = self.left_image
        elif self.moving_right:
            self.x += 3
            self.image = self.right_image
        elif self.moving_up:
            self.y -= 3
        elif self.moving_down:
            self.y += 3
        # make sure this puts the fish in a valid position
        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_WIDTH - TILE_SIZE:
            self.x = SCREEN_WIDTH - TILE_SIZE
        if self.y < 0:
            self.y = 0
        elif self.y > SCREEN_HEIGHT - TILE_SIZE:
            self.y = SCREEN_HEIGHT - TILE_SIZE
# make it not touch the sand and update to pic on phone
