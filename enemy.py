"""
Author: Ned Austin Datiles
"""

import pygame, math, random
from vehicle import Vehicle
from core import ENEMY_SHIP_TYPES
from ammunition import Laser, Rocket

class Enemy(Vehicle):
    """ Enemy super class definition """

    def __init__(self, type, shot_damage, shot_speed, shot_interval, health):
        super().__init__(ENEMY_SHIP_TYPES[type]["image"], shot_damage=shot_damage,
                         shot_speed=shot_speed, health=health)
        self.reward = None
        self.track_player = False
        self.movement_speed = 0
        self.shooting_time = shot_interval
        self.image_angle = 0

    def get_reward(self):
        return self.reward

    def shoot(self):
        pass

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

    def update(self):
        self.track_player = True
        self.enemy_rotate()
        super().update()

class Drone_1st_class(Enemy):
    """
    Drones represents the first line of enemies the player will meet.
    They are fairly weak in comparison to the player.
    """
    SHOT_SPEED = 4
    SHOT_INTERVAL = 2000
    SHOT_DAMAGE = 5
    HEALTH = 100
    MIN_INDEX = 0
    MAX_INDEX = 4
    MOVEMENT_SPEED = 2

    def __init__(self):
        super().__init__(type=random.randint(self.MIN_INDEX, self.MAX_INDEX),
                         shot_damage=self.SHOT_DAMAGE, shot_speed=self.SHOT_SPEED,
                         shot_interval=self.SHOT_INTERVAL, health=self.HEALTH)
        self.reward = random.randint(self.MIN_INDEX, self.MAX_INDEX) * 10
        self.movement_speed = self.MOVEMENT_SPEED
        self.ammo_type = random.randint(16, 23)

    def shoot(self):
        time_atm = pygame.time.get_ticks()
        if time_atm - self.last_shot_time > self.shooting_time:
            self.last_shot_time = time_atm
            bullet = Laser(self, self.image_angle)
            self.ammunition_list.add(bullet)

class Drone_2nd_class(Enemy):
    SHOT_SPEED = 6
    SHOT_INTERVAL = 1500
    SHOT_DAMAGE = 20
    HEALTH = 250
    MIN_INDEX = 5
    MAX_INDEX = 9
    MOVEMENT_SPEED = 3

    def __init__(self):
        super().__init__(type=random.randint(self.MIN_INDEX, self.MAX_INDEX),
                         shot_damage=self.SHOT_DAMAGE, shot_speed=self.SHOT_SPEED,
                         shot_interval=self.SHOT_INTERVAL, health=self.HEALTH)
        self.reward = random.randint(self.MIN_INDEX, self.MAX_INDEX) * 15
        self.movement_speed = self.MOVEMENT_SPEED
        self.ammo_type = random.randint(0, 4)

    def shoot(self):
        time_atm = pygame.time.get_ticks()
        if time_atm - self.last_shot_time > self.shooting_time:
            self.last_shot_time = time_atm
            bullet = Laser(self, self.image_angle)
            self.ammunition_list.add(bullet)

class Drone_3rd_class(Enemy):
    SHOT_SPEED = 10
    SHOT_INTERVAL = 1350
    SHOT_DAMAGE = 35
    HEALTH = 400
    MIN_INDEX = 10
    MAX_INDEX = 14
    MOVEMENT_SPEED = 6

    def __init__(self):
        super().__init__(type=random.randint(self.MIN_INDEX, self.MAX_INDEX),
                         shot_damage=self.SHOT_DAMAGE, shot_speed=self.SHOT_SPEED,
                         shot_interval=self.SHOT_INTERVAL, health=self.HEALTH)
        self.reward = random.randint(self.MIN_INDEX, self.MAX_INDEX) * 20
        self.movement_speed = self.MOVEMENT_SPEED
        self.ammo_type = random.randint(6, 10)
        self.hasRockets = random.uniform(0, 1) <= .25

    def shoot(self):
        # This class will shoot rockets and lasers
        # The chance that that this ship will have a rocket
        # is 25%
        time_atm = pygame.time.get_ticks()
        if time_atm - self.last_shot_time > self.shooting_time:
            self.last_shot_time = time_atm
            bullet = Laser(self, self.image_angle)
            self.ammunition_list.add(bullet)

class Elite_Drone(Enemy):
    SHOT_SPEED = 12
    SHOT_INTERVAL = 800
    SHOT_DAMAGE = 55
    HEALTH = 550
    MIN_INDEX = 20
    MAX_INDEX = 27
    MOVEMENT_SPEED = 8

    def __init__(self):
        super().__init__(type=random.randint(self.MIN_INDEX, self.MAX_INDEX),
                         shot_damage=self.SHOT_DAMAGE, shot_speed=self.SHOT_SPEED,
                         shot_interval=self.SHOT_INTERVAL, health=self.HEALTH)
        self.reward = random.randint(self.MIN_INDEX, self.MAX_INDEX) * 40
        self.movement_speed = self.MOVEMENT_SPEED
        self.ammo_type = random.randint(16, 23)
        self.hasRockets = random.uniform(0, 1) <= .40

    def shoot(self):
        # This class will shoot rockets and lasers
        # The chance that that this ship will have a rocket
        # is 40%
        time_atm = pygame.time.get_ticks()
        if time_atm - self.last_shot_time > self.shooting_time:
            self.last_shot_time = time_atm
            bullet = Laser(self, self.image_angle)
            self.ammunition_list.add(bullet)