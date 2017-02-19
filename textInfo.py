import pygame

class Text(pygame.sprite.Sprite):
    FONT_SIZE = 7
    DISPLAY_TIME = 100
    def __init__(self, owner, value, color):
        super().__init__()
        self.owner = owner
        self.font = pygame.font.Font(
            "Assets/Fonts/kenpixel_future.ttf", self.FONT_SIZE)
        self.image = self.font.render("-"+str(value), True, color)
        self.rect = self.image.get_rect()
        self.rect.x = self.owner.rect.x
        self.rect.y = self.owner.rect.y - 5
        self.appearance_time = pygame.time.get_ticks()
        self.appearance_duration = self.DISPLAY_TIME

    def update(self):
        current_time = pygame.time.get_ticks()
        self.rect.x += self.owner.change_x
        self.rect.y += self.owner.change_y
        if current_time - self.appearance_time > self.appearance_duration:
            self.kill()