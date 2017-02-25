"""
Author: Ned Austin Datiles
"""
import pygame, sys, random
from player import Player
from enemy import Elite_Drone
from animations import Animation
from constants import *


class Wall(pygame.sprite.Sprite):
    """
    Wall class definition
    """
    def __init__(self, Attributes):
        super().__init__()
        self.image = pygame.Surface([Attributes[2], Attributes[3]])
        self.rect = self.image.get_rect()
        self.image.fill(Attributes[4])
        self.rect.x = Attributes[0]
        self.rect.y = Attributes[1]

class Level(object):
    """
    Level base class.
    """
    ENEMY_FIRE_EVENT = pygame.USEREVENT + 7
    def __init__(self, player):
        self.world_shift = 0                     # How much the world has shifted so far
        self.level_limit = 2000                  # default level limit
        self.enemy_fire_time = 1000              # default firing time in milliseconds
        self.enemies_can_fire = False            # Enemies cannot fire unless this is true
        self.wall_list = pygame.sprite.Group()   # list all boundaries surrounding the play area
        self.enemy_list = pygame.sprite.Group()  # list of all enemies in the level
        self.debris_list = pygame.sprite.Group() # list of debris found on the map. Includes powers + asteroids
        self.player = player                     # the player of the current level
        self.animation_list = pygame.sprite.Group()

        # Sets the wall's colour
        self.theme = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        boundaries = [[0, -self.level_limit, WINDOW_WIDTH, 5, self.theme], # Top
                      [0, -self.level_limit, 5, self.level_limit + WINDOW_HEIGHT, self.theme], # left
                      [WINDOW_WIDTH - 5, -self.level_limit, 5, self.level_limit + WINDOW_HEIGHT, self.theme],
                      [0, WINDOW_HEIGHT - 5, WINDOW_WIDTH, 5, self.theme]
                      ]

        for boundary in boundaries:
            wall = Wall(boundary)
            self.wall_list.add(wall)

    def generate_spawn_locations(self):
        pass

    def set_level_limit(self, level_limit):
        self.level_limit = level_limit

    def shift_world(self, shift_y):
        self.world_shift += shift_y
        if self.player.rect.y + self.player.rect.height > WINDOW_HEIGHT or self.world_shift < self.level_limit:
            for wall in self.wall_list:
                wall.rect.y += shift_y
            for enemy in self.enemy_list:
                enemy.rect.y += shift_y
            for debris in self.debris_list:
                debris.rect.y += shift_y

    def check_world_condition(self):
        # Shifts the world upwards when the player moves up halfway on the screen
        if self.player.rect.y <= WINDOW_HEIGHT // 2 + self.player.rect.height:
            diff = WINDOW_HEIGHT // 2 + self.player.rect.height - self.player.rect.y
            self.player.rect.y = WINDOW_HEIGHT // 2 + self.player.rect.height
            self.shift_world(diff)
        # Shift the world downwards when the player is moving backwards on the screen
        if self.player.rect.y > WINDOW_HEIGHT - self.player.rect.height:
            diff = (WINDOW_HEIGHT - self.player.rect.height) - self.player.rect.y
            self.player.rect.y = WINDOW_HEIGHT - self.player.rect.height
            self.shift_world(diff)

    def draw(self, screen):
        for enemy in self.enemy_list:
            enemy.draw(screen)
        self.enemy_list.draw(screen)
        self.wall_list.draw(screen)
        self.debris_list.draw(screen)
        self.animation_list.draw(screen)

    def check_bullet_collisions(self):
        if self.player.ammunition_list:
            for bullet in self.player.ammunition_list:
                enemy_hit_list = pygame.sprite.spritecollide(bullet, self.enemy_list, False)
                if enemy_hit_list:
                    self.animation_list.add(Animation(bullet.rect.x, bullet.rect.y + bullet.rect.height))
                    self.player.ammunition_list.remove(bullet)
                    for enemy in enemy_hit_list:
                        enemy.sustain_damage(bullet.get_impact())
                        if not(enemy.is_alive()):
                            self.player.increase_score(enemy.get_reward())
                            self.enemy_list.remove(enemy)

            # for bullet in self.ammunition_list:
            #    debris_hit_list = pygame.sprite.spritecollide(bullet, self.level.debris_list, False)
            #    if debris_hit_list:
            #        self.ammunition_list.remove(bullet)
            #        for debris in debris_hit_list:
            #            debris.sustain_damage(bullet.get_impact())
            #            if not(debris.is_alive()):
            #                self.level.debris_list.remove(debris

        for enemy in self.enemy_list:
            if enemy.ammunition_list:
                hit_player = pygame.sprite.spritecollide(self.player,\
                                                         enemy.ammunition_list, False)
                if hit_player:
                    for bullet in hit_player:
                        self.animation_list.add(Animation(bullet.rect.x, bullet.rect.y))
                        self.player.sustain_damage(bullet.get_impact())
                        enemy.ammunition_list.remove(bullet)
    def update(self):
        self.animation_list.update()
        self.check_world_condition()
        self.check_bullet_collisions()
        self.debris_list.update()
        self.enemy_list.update()
        self.wall_list.update()

class Level01(Level):
    def __init__(self, player):
        super().__init__(player)

        for i in range(50, WINDOW_WIDTH - 50, 50):
            for j in range(-100, -50, 50):
                enemy = Elite_Drone()
                enemy.set_location(i, j)
                enemy.level = self
                enemy.track_player = False
                self.enemy_list.add(enemy)

def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    all_sprite_list = pygame.sprite.Group()
    player = Player()
    all_sprite_list.add(player)

    level = Level01(player)
    player.level = level

    pygame.time.set_timer(level.ENEMY_FIRE_EVENT, level.enemy_fire_time)
    while True:
        level.enemies_can_fire = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == level.ENEMY_FIRE_EVENT:
                print(len(player.ammunition_list))
                print(clock.get_fps())
                level.enemies_can_fire = True
        level.update()
        all_sprite_list.update()

        screen.fill(BLACK)
        level.draw(screen)
        player.draw(screen)
        all_sprite_list.draw(screen)

        pygame.display.update()

        clock.tick(FPS)


if __name__ == "__main__":
    main()
