"""
Author: Ned Austin Datiles
"""
import pygame
from vehicle import Vehicle
from core import PLAYER_SHIP_TYPES
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, RED
from healthbar import HealthBar
from ammunition import Ammunition
from animations import Animation
from textInfo import Text

class Player(Vehicle):
    DEFAULT_SHOT_DAMAGE = 50
    DEFAULT_SHOT_SPEED = 10
    DEFAULT_PLAYER_MOVEMENT_SPEED = 6
    DEFAULT_SHOOTING_TIME = 200
    POWERUP_DURATION = 5000

    def __init__(self, type=0, has_shield=False):
        super().__init__(PLAYER_SHIP_TYPES[type]["image"], shot_damage= self.DEFAULT_SHOT_DAMAGE,
                         shot_speed= self.DEFAULT_SHOT_SPEED, health=1000)
        self.score = 0
        self.set_location(WINDOW_WIDTH // 2 - self.rect.width // 2, WINDOW_HEIGHT - 2 * self.rect.height)

        self.has_shield = has_shield

        # Holds a list of shields. Used only for drawing purposes
        self.shield = pygame.sprite.Group()

        # Container for the player's health bar. Only for drawing purposes
        self.health_container = pygame.sprite.Group()
        health_bar = HealthBar(self)
        self.health_container.add(health_bar)

        self.shooting_time = self.DEFAULT_SHOOTING_TIME

        self.has_damage_multiplier = False
        self.damage_increase_time_out = self.POWERUP_DURATION

        self.has_movement_speed_boost = False
        self.speed_boost_time_out = self.POWERUP_DURATION

        # Player's bullet vector. The player's bullets only move downwards on the screen.
        self.bullet_vector = [0, -1]

    def increase_shot_damage(self, multiplier):
        pass

    def increase_shot_rate(self, multiplier):
        pass

    def increase_health(self, health_bonus):
        self.health += health_bonus

    def increase_score(self, amount):
        self.score += amount

    def get_score(self):
        return self.score

    def draw(self, screen):
        self.health_container.draw(screen)
        super().draw(screen)
        if self.has_shield:
            self.shield.draw(screen)

    def shoot(self):
        time_atm = pygame.time.get_ticks()
        if time_atm - self.last_shot_time > self.shooting_time:
            self.last_shot_time = time_atm
            bullet = Ammunition(self, 0, self.shot_damage, self.shot_speed, self.ammo_type)
            self.ammunition_list.add(bullet)

    def handle_keystrokes(self):
        # Key pressed
        keys_down = pygame.key.get_pressed()
        self.change_x = 0
        self.change_y = 0

        # Left - Right movement
        if keys_down[pygame.K_LEFT]:
            self.adjust_speed(-self.DEFAULT_PLAYER_MOVEMENT_SPEED, 0)
        elif keys_down[pygame.K_RIGHT]:
            self.adjust_speed(self.DEFAULT_PLAYER_MOVEMENT_SPEED, 0)

        # Up - Down movement
        if keys_down[pygame.K_UP]:
            self.adjust_speed(0, -self.DEFAULT_PLAYER_MOVEMENT_SPEED)
        elif keys_down[pygame.K_DOWN]:
            self.adjust_speed(0, self.DEFAULT_PLAYER_MOVEMENT_SPEED)

        # Firing signal
        if keys_down[pygame.K_SPACE]:
            self.shoot()

    def check_bullet_collisions(self):
        if self.ammunition_list:
            for bullet in self.ammunition_list:
                enemy_hit_list = pygame.sprite.spritecollide(bullet, self.level.enemy_list, False)
                if enemy_hit_list:
                    self.ammunition_list.remove(bullet)
                    for enemy in enemy_hit_list:
                        enemy.sustain_damage(bullet.get_impact())
                        if not(enemy.is_alive()):
                            self.increase_score(enemy.get_reward())
                            self.level.enemy_list.remove(enemy)

            for bullet in self.ammunition_list:
                wall_hit_list = pygame.sprite.spritecollide(bullet, self.level.wall_list, False)
                if wall_hit_list:
                    self.ammunition_list.remove(bullet)

            for bullet in self.ammunition_list:
                debris_hit_list = pygame.sprite.spritecollide(bullet, self.level.debris_list, False)
                if debris_hit_list:
                    self.ammunition_list.remove(bullet)
                    for debris in debris_hit_list:
                        debris.sustain_damage(bullet.get_impact())
                        if not(debris.is_alive()):
                            self.level.debris_list.remove(debris)

    def update(self):
        self.health_container.update()
        if self.shield:
            self.shield.update()
        self.check_bullet_collisions()
        self.handle_keystrokes()
        super().update()
