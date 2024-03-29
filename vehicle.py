"""
Author: Ned Austin Datiles
"""

import pygame

class Vehicle(pygame.sprite.Sprite):

    def __init__(self, image, shot_damage, shot_speed,  health=1000):
        super().__init__()
        # Load the sprite image
        self.original_image = image
        self.image = self.original_image
        self.rect = self.image.get_rect()

        # This vehicle's level
        self.level = None

        # Vehicle ammunition list
        self.ammunition_list = pygame.sprite.Group()

        # Initialize the vehicle health
        self.health = health

        # Initialize the movement vector
        self.change_x = 0
        self.change_y = 0

        # choose the type of ammunition for this enemy
        self.ammo_type = 0

        # Vehicle's bullet vector
        self.bullet_vector = None

        # Shot speed
        self.shot_speed = shot_speed

        # Shot damage
        self.shot_damage = shot_damage

        self.shooting_time = 0

        # Time of last shot
        self.last_shot_time = pygame.time.get_ticks()

    def set_location(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def sustain_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def adjust_speed(self, x, y):
        self.change_x += x
        self.change_y += y

    def draw(self, screen):
        if self.ammunition_list:
            self.ammunition_list.draw(screen)

    def shoot(self):
        pass

    def check_boundaries(self):
        pass

    def update(self):
        pass
