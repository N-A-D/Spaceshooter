"""
Author: Ned Austin Datiles
"""

import pygame, sys
from core import LASER_ANIMATIONS
from random import randint

class Animation(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animation_duration = 100 # Default animation time
        self.time_of_appearance = pygame.time.get_ticks()
        self.image = LASER_ANIMATIONS[randint(0, len(LASER_ANIMATIONS)-1)]["image"]
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y - self.rect.height // 3

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.time_of_appearance > self.animation_duration:
            self.kill()