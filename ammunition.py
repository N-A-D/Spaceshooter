"""
Author: Ned Austin Datiles
"""
import pygame
from core import AMMO_TYPES, LASER_ANIMATIONS
from constants import BLACK, WINDOW_HEIGHT, WINDOW_WIDTH
from animations import Animation

class Ammunition(pygame.sprite.Sprite):
    """ Ammunition class definition"""
    def __init__(self, owner, angle, shot_damage, shot_speed, type=0):
        super().__init__()
        self.owner = owner  # from where did this shot come from
        self.original_image = AMMO_TYPES[type]["image"]
        self.angle = angle
        if self.angle != 0:
            self.original_image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.original_image.set_colorkey(BLACK)
        self.image = self.original_image
        self.rect = self.image.get_rect()

        self.set_location(self.owner.rect.x + self.owner.rect.width // 2 - self.rect.width//2,
                          self.owner.rect.y + self.owner.rect.height // 2 + self.rect.height // 2)

        # Set the damage
        self.damage = shot_damage
        # We need floats since integers are not the best for calculating directions
        self.float_x = self.rect.x
        self.float_y = self.rect.y
        self.change_x = self.owner.bullet_vector[0] * shot_speed
        self.change_y = self.owner.bullet_vector[1] * shot_speed

        if self.change_x == 0 and self.change_y == 0:
            self.change_y = shot_speed


    def set_location(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def get_impact(self):
        return self.damage

    def set_impact(self, damage):
        self.damage = damage

    def draw(self, screen):
        pass

    def update(self):
        self.float_x += self.change_x
        self.float_y += self.change_y
        self.rect.x = int(self.float_x)
        self.rect.y = int(self.float_y)

        if self.rect.x < -10 or self.rect.x > WINDOW_WIDTH - 10 or self.rect.y > WINDOW_HEIGHT + 10 or self.rect.y < -10:
            self.kill()

class Laser(Ammunition):
    DEFAULT_TRAVEL_SPEED = 10
    DEFAULT_DAMAGE = 10
    def __init__(self, owner, angle):
        super().__init__(owner=owner, angle=angle, shot_damage=self.DEFAULT_DAMAGE,
                         shot_speed=self.DEFAULT_TRAVEL_SPEED, type=owner.ammo_type)


class Rocket(Ammunition):
    DEFAULT_TRAVEL_SPEED = 5
    DEFAULT_DAMAGE = 100
    def __init__(self, owner, angle):
        super().__init__(owner=owner, angle=angle, shot_damage=self.DEFAULT_DAMAGE,
                         shot_speed=self.DEFAULT_TRAVEL_SPEED, type=owner.ammo_type)