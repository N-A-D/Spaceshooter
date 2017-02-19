import pygame, copy

from constants import BLACK

class Shield(pygame.sprite.Sprite):
    """ Defines a shield """
    def __init__(self, owner, image,  health):
        super().__init__()
        # Initialize shield attributes
        self.health = health
        self.owner = owner

        # load the shield image
        self.original_image = image
        self.image = self.original_image

        # Set shield location
        self.rect = copy.deepcopy(self.owner.rect)
        self.rect.x -= 10
        self.rect.y -= 10

    def sustain_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health >= 0

    def increase_health(self, increase):
        self.health += increase

    def update(self):
        if self.angle != 0:
            self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
            self.image.set_colorkey(BLACK)
        self.rect.x += self.owner.change_x
        self.rect.y += self.owner.change_y