import pygame
from settings import *


class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.right_image = pygame.image.load("assets/images/orange_fish.png").convert()
        self.right_image.set_colorkey((0, 0, 0))
        self.image = self.right_image
        self.left_image = pygame.transform.flip(self.image, True, False)
        # creating a rectangle that tells where to paint fish
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        print("i am a brand new fish:)")

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        if self.moving_left:
            self.rect.x -= 5
            self.image = self.left_image
        elif self.moving_right:
            self.rect.x += 5
            self.image = self.right_image
        elif self.moving_up:
            self.rect.y -= 5
        elif self.moving_down:
            self.rect.y += 5
        # make sure this puts the fish in a valid position
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > WATER_BOTTOM:  # accounts for sand
            self.rect.bottom = WATER_BOTTOM

