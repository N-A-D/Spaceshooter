import pygame

class HealthBar(pygame.sprite.Sprite):
    BARHEIGHT = 5
    def __init__(self, player):
        super().__init__()
        self.player = player
        # Base image holds the original length of the health bar
        self.base_image = pygame.Surface((self.player.rect.width,
                                    self.BARHEIGHT))
        self.image = self.base_image
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y + self.player.rect.height + self.BARHEIGHT

    def update(self):
        # Adjust the size of the health bar according to current
        # health
        if self.player.is_alive():
            new_length_bar = (self.base_image.get_rect().width * self.player.health / 1000)
            self.image = pygame.Surface((new_length_bar, self.BARHEIGHT))
            self.image.fill((0, 204, 204))
            self.rect.x = self.player.rect.x
            self.rect.y = self.player.rect.y + self.player.rect.height + self.BARHEIGHT