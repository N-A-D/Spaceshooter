import pygame, random

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

        self.context_info = pygame.sprite.Group()

        self.animation_list = pygame.sprite.Group()

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
        return self.health >= 0

    def adjust_speed(self, x, y):
        self.change_x += x
        self.change_y += y

    def draw(self, screen):
        if self.ammunition_list:
            self.ammunition_list.draw(screen)
        if self.context_info:
            self.context_info.draw(screen)
        if self.animation_list:
            self.animation_list.draw(screen)

    def shoot(self):
        pass

    def check_boundaries(self):
        self.rect.x += self.change_x
        wall_hit_list = pygame.sprite.spritecollide(self, self.level.wall_list, False)
        if wall_hit_list:
            for wall in wall_hit_list:
                if self.change_x > 0:
                    self.rect.right = wall.rect.left
                else:
                    self.rect.left = wall.rect.right

        self.rect.y += self.change_y
        wall_hit_list = pygame.sprite.spritecollide(self, self.level.wall_list, False)
        if wall_hit_list:
            for wall in wall_hit_list:
                if self.change_y > 0:
                    self.rect.bottom = wall.rect.top
                else:
                    self.rect.top = wall.rect.bottom

    def check_bullet_collisions(self):
        pass

    def update(self):
        if self.ammunition_list:
            self.ammunition_list.update()
            self.check_bullet_collisions()
        if self.context_info:
            self.context_info.update()
        if self.animation_list:
            self.animation_list.update()
        self.check_boundaries()
