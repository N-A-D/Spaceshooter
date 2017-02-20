"""
Author: Ned Austin Datiles
"""

import pygame, sys
from core import LASER_ANIMATIONS
from random import randint

class Animation(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.animation_duration = 100 # Default animation time
        self.time_of_appearance = pygame.time.get_ticks()
        self.image = image
        self.rect = self.image.get_rect()

    def set_location(self, x, y):
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y - self.rect.height // 3

    def has_disappeared(self):
        return pygame.time.get_ticks() - self.time_of_appearance > self.animation_duration

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.time_of_appearance > self.animation_duration:
            self.kill()