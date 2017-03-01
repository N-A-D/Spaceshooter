"""
Author: Ned Austin Datiles
"""

import pygame, math, random
from vehicle import Vehicle
from ammunition import Laser
from constants import WINDOW_WIDTH

class Enemy(Vehicle):
    """ Enemy super class definition """
    ENEMY_SHIPS = {
        'GRUNTS': [[pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyBlack1.png"),
                    pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyBlack2.png"),
                    pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyBlack3.png"),
                    pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyBlack4.png"),
                    pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyBlack5.png")
                    ],
                   [
                       pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyBlue1.png"),
                       pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyBlue2.png"),
                       pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyBlue3.png"),
                       pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyBlue4.png"),
                       pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyBlue5.png")
                   ],
                   [
                       pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyGreen1.png"),
                       pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyGreen2.png"),
                       pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyGreen3.png"),
                       pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyGreen4.png"),
                       pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyGreen5.png"),
                   ],
                   [
                       pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyRed1.png"),
                       pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyRed2.png"),
                       pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyRed3.png"),
                       pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyRed4.png"),
                       pygame.image.load("Assets\spaceshooter\PNG\Enemies\enemyRed5.png")
                   ]
                   ],

        'JACKALS': [
            pygame.image.load("Assets\spaceshooter3\PNG\Sprites\Ships\spaceShips_001.png"),
            pygame.image.load("Assets\spaceshooter3\PNG\Sprites\Ships\spaceShips_002.png"),
            pygame.image.load("Assets\spaceshooter3\PNG\Sprites\Ships\spaceShips_003.png"),
            pygame.image.load("Assets\spaceshooter3\PNG\Sprites\Ships\spaceShips_004.png"),
            pygame.image.load("Assets\spaceshooter3\PNG\Sprites\Ships\spaceShips_005.png"),
            pygame.image.load("Assets\spaceshooter3\PNG\Sprites\Ships\spaceShips_006.png"),
            pygame.image.load("Assets\spaceshooter3\PNG\Sprites\Ships\spaceShips_007.png"),
            pygame.image.load("Assets\spaceshooter3\PNG\Sprites\Ships\spaceShips_008.png"),
            pygame.image.load("Assets\spaceshooter3\PNG\Sprites\Ships\spaceShips_009.png")

        ],
        'ELITES': [
            [

                pygame.image.load("Assets\spaceshooter2\Red\Elite_red1.png")
            ],
            [

                pygame.image.load("Assets\spaceshooter2\Blue\Elite_blue1.png")

            ]
        ],
        'BRUTES': [
            [

                pygame.image.load("Assets\spaceshooter2\Red\Brute_red.png")

            ],
            [

                pygame.image.load("Assets\spaceshooter2\Blue\Brute_blue.png")
            ]
        ],
        'Corvette': [

                pygame.image.load("Assets\spaceshooter2\Blue\Communicationship_blue.png"),


                    pygame.image.load("Assets\spaceshooter2\Red\Communicationship_red.png")
                ]
    }
    def __init__(self, shot_damage=10, shot_speed=10, shot_interval=1000, health=200):
        image = pygame.transform.smoothscale(self.ENEMY_SHIPS["Corvette"][0], (200, 200))
        image.set_colorkey((0, 0, 0))
        super().__init__(image, shot_damage=shot_damage,
                         shot_speed=shot_speed, health=health)
        self.reward = 10
        self.track_player = False
        self.movement_speed = 0
        self.shooting_time = shot_interval
        self.image_angle = 0
        self.change_x, self.change_y = 0, 0

    def get_reward(self):
        return self.reward

    def shoot(self):
        time_atm = pygame.time.get_ticks()
        if time_atm - self.last_shot_time > self.shooting_time:
            self.last_shot_time = time_atm
            laser = Laser(self, self.image_angle)
            self.ammunition_list.add(laser)

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

    def check_boundaries(self):
        if self.rect.x + self.rect.width > WINDOW_WIDTH or self.rect.x < 0:
            self.change_x *= -1

    def update(self):
        self.enemy_rotate()
        self.ammunition_list.update()
        if self.track_player:
            self.rect.x += self.change_x
            self.rect.y += self.change_y

            self.check_boundaries()

            if self.level.player.rect.y - self.rect.y + self.rect.height < 350:
                self.change_y = 0
            else:
                if self.level.player.rect.y - self.rect.y + self.rect.height < 0:
                    self.change_y = -1 * self.movement_speed
                else:
                    self.change_y = self.movement_speed