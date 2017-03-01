"""
Author: Ned Austin Datiles
"""
import pygame, random
from vehicle import Vehicle
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, RED
from healthbar import HealthBar
from ammunition import Laser


class Player(Vehicle):
    PLAYER_SHIPS = {
        'RED': [pygame.image.load("Assets\spaceshooter\PNG\playerShip1_red.png"),
                pygame.image.load("Assets\spaceshooter\PNG\playerShip2_red.png"),
                pygame.image.load("Assets\spaceshooter\PNG\playerShip3_red.png"),
                ],
        'BLUE': [
            pygame.image.load("Assets\spaceshooter\PNG\playerShip1_blue.png"),
            pygame.image.load("Assets\spaceshooter\PNG\playerShip2_blue.png"),
            pygame.image.load("Assets\spaceshooter\PNG\playerShip3_blue.png")
        ],
        'GREEN': [
            pygame.image.load("Assets\spaceshooter\PNG\playerShip1_green.png"),
            pygame.image.load("Assets\spaceshooter\PNG\playerShip2_green.png"),
            pygame.image.load("Assets\spaceshooter\PNG\playerShip3_green.png")
        ],
        'ORANGE': [
            pygame.image.load("Assets\spaceshooter\PNG\playerShip1_orange.png"),
            pygame.image.load("Assets\spaceshooter\PNG\playerShip2_orange.png"),
            pygame.image.load("Assets\spaceshooter\PNG\playerShip3_orange.png")
        ]
    }

    DEFAULT_SHOT_DAMAGE = 50
    DEFAULT_SHOT_SPEED = 10
    DEFAULT_PLAYER_MOVEMENT_SPEED = 10
    DEFAULT_SHOOTING_TIME = 100
    POWERUP_DURATION = 5000

    def __init__(self):
        image = pygame.transform.smoothscale(self.PLAYER_SHIPS["ORANGE"][2], (30, 30))
        image.set_colorkey((0, 0, 0))
        super().__init__(image, shot_damage=self.DEFAULT_SHOT_DAMAGE,
                         shot_speed=self.DEFAULT_SHOT_SPEED, health=1000)
        self.score = 0
        self.set_location(WINDOW_WIDTH // 2 - self.rect.width // 2, WINDOW_HEIGHT - 2 * self.rect.height)

        self.has_shield = False

        # Holds a list of shields. Used only for drawing purposes
        self.shield = pygame.sprite.Group()

        # Container for the player's health bar. Only for drawing purposes
        self.health_container = pygame.sprite.Group()
        health_bar = HealthBar(self, (self.rect.width, self.rect.height))
        self.health_container.add(health_bar)

        self.shooting_time = self.DEFAULT_SHOOTING_TIME

        self.has_damage_multiplier = False
        self.damage_increase_time_out = self.POWERUP_DURATION

        self.has_movement_speed_boost = False
        self.speed_boost_time_out = self.POWERUP_DURATION

        # Player's bullet vector. The player's bullets only move downwards on the screen.
        self.bullet_vector = [0, -1]

        self.animation_list = pygame.sprite.Group()

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
        super().draw(screen)
        self.animation_list.draw(screen)
        self.health_container.draw(screen)
        if self.has_shield:
            self.shield.draw(screen)

    def shoot(self):
        time_atm = pygame.time.get_ticks()
        if time_atm - self.last_shot_time > self.shooting_time:
            self.last_shot_time = time_atm
            laser = Laser(self, 0)
            self.ammunition_list.add(laser)

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

    def check_boundaries(self):
        if self.rect.x + self.rect.width > WINDOW_WIDTH or self.rect.x < 0:
            self.change_x *= -1
        if self.rect.y < 0 or self.rect.y + self.rect.height > WINDOW_HEIGHT:
            self.change_y *= -1

    def update(self):
        self.animation_list.update()
        self.health_container.update()
        if self.shield:
            self.shield.update()
        self.handle_keystrokes()
        if self.ammunition_list:
            self.ammunition_list.update()
        self.rect.x += self.change_x
        self.rect.y += self.change_y
