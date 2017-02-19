"""
Author: Ned Austin Datiles
"""

import pygame, math
from vehicle import Vehicle
from core import ENEMY_SHIP_TYPES
from textInfo import Text
from ammunition import Ammunition
from animations import Animation
from constants import RED

class Enemy(Vehicle):
    """ Enemy class definition """
    DEFAULT_ENEMY_SHOT_DAMAGE = 50
    DEFAULT_ENEMY_SHOT_SPEED = 10
    DEFAULT_ENEMY_SHOOTING_TIME = 3000
    # Note: the fastest that the enemies can shoot at is 200 milliseconds

    def __init__(self, type_, health=200):
        super().__init__(ENEMY_SHIP_TYPES[type_]["image"], shot_damage=self.DEFAULT_ENEMY_SHOT_DAMAGE,
                         shot_speed=self.DEFAULT_ENEMY_SHOT_SPEED, health=health)
        self.reward = health
        self.track_player = False

        self.shooting_time = self.DEFAULT_ENEMY_SHOOTING_TIME

        # Vehicle's image_angle
        self.image_angle = 0

    def get_reward(self):
        return self.reward

    def shoot(self):
        time_atm = pygame.time.get_ticks()
        if time_atm - self.last_shot_time > self.shooting_time:
            self.last_shot_time = time_atm
            bullet = Ammunition(self, self.image_angle, self.shot_damage, self.shot_speed, self.ammo_type)
            self.ammunition_list.add(bullet)

    def enemy_rotate(self):
        if self.track_player:
            # Find the distance between this enemy and the player in the x and y direction.
            diff_x = self.level.player.rect.x - self.rect.x
            diff_y = self.level.player.rect.y - self.rect.y
            # Find the angle to rotate this enemy by
            # we negate diff_x because the player can move side to side
            # and so it would sometimes have an x coordinate less than this enemies ship
            # and then a second later have one that is greater.
            # -90 ensures that the ship is upright.
            self.image_angle = int(math.degrees(math.atan2(diff_y, -diff_x))) - 90
            # We need radians to calculate the projectile trajectory.
            rad = math.radians(self.image_angle + 90)
            self.bullet_vector = [-math.cos(rad), math.sin(rad)]
            self.shoot()
            self.image = pygame.transform.rotozoom(self.original_image, self.image_angle, 1)
            self.image_angle = self.image_angle % 360


    def check_bullet_collisions(self):
        if self.ammunition_list:
            hit_player = pygame.sprite.spritecollide(self.level.player, self.ammunition_list, False)
            if hit_player:
                for bullet in hit_player:
                    self.context_info.add(Text(self.level.player, bullet.get_impact(), RED))
                    self.level.player.sustain_damage(bullet.get_impact())
                    self.ammunition_list.remove(bullet)
                    self.animation_list.add(Animation(bullet.rect.x, bullet.rect.y))
            for bullet in self.ammunition_list:
                wall_hit_list = pygame.sprite.spritecollide(bullet, self.level.wall_list, False)
                if wall_hit_list:
                    self.ammunition_list.remove(bullet)


    def update(self):
        distance = math.sqrt((self.level.player.rect.x - self.rect.x) ** 2 + (self.level.player.rect.y - self.rect.y) ** 2)
        if distance < 600:
            self.track_player = True
            self.enemy_rotate()
        else:
            self.track_player = False
        self.check_bullet_collisions()
        super().update()