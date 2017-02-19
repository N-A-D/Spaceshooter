"""
Author: Ned Austin Datiles
"""

import pygame

class HealthBar(pygame.sprite.Sprite):
    BARHEIGHT = 5
    def __init__(self, owner, dimensions):
        super().__init__()
        self.owner = owner
        # Base image holds the original length of the health bar
        self.base_image = pygame.Surface((dimensions[0], dimensions[1]))
        self.image = self.base_image
        self.image.fill((0, 255, 0))
        self.image.set_colorkey((0, 255, 0))
        self.rect = self.image.get_rect()

        self.rect.x = self.owner.rect.x
        self.rect.y = self.owner.rect.y + self.owner.rect.height + self.BARHEIGHT

    def set_location(self, location):
        """
        Sets the location of the health bar
        :param location: tuple that contains the x and y coordinates
        :return:
        """
        self.rect.x, self.rect.y = location
    def update(self):
        # Adjust the size of the health bar according to current
        # health
        if self.owner.is_alive():
            new_length_bar = (self.base_image.get_rect().width * self.owner.health / 1000)
            self.image = pygame.Surface((new_length_bar, self.BARHEIGHT))
            self.image.fill((0, 255, 0))
            self.image.convert_alpha(self.image)
            self.rect.x = self.owner.rect.x
            self.rect.y = self.owner.rect.y + self.owner.rect.height + self.BARHEIGHT
        else:
            self.kill()
            self.owner.kill()