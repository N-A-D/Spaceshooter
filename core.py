"""
Author: Ned Austin Datiles
"""

import pygame

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



POWER_UPS = {
    'BOLT': [
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\powerupBlue_bolt.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\powerupRed_bolt.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\powerupYellow_bolt.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\powerupGreen_bolt.png")
    ],
    'SHIELD': [
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\powerupBlue_shield.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\powerupRed_shield.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\powerupYellow_shield.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\powerupGreen_shield.png")
    ],
    'STAR': [
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\powerupBlue_star.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\powerupRed_star.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\powerupYellow_star.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\powerupGreen_star.png")
    ],
    'RANDOM': [
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\powerupBlue.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\powerupRed.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\powerupYellow.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\powerupGreen.png")
    ],
    'CREDITS': [
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\credit_bronze.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\credit_silver.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Power-ups\credit_gold.png")
    ]
}

METEORS = {
    'BROWN': [
        pygame.image.load("Assets\spaceshooter\PNG\Meteors\meteorBrown_big1.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Meteors\meteorBrown_big2.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Meteors\meteorBrown_big3.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Meteors\meteorBrown_big4.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Meteors\meteorBrown_med1.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Meteors\meteorBrown_med3.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Meteors\meteorBrown_small1.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Meteors\meteorBrown_small2.png")
    ],
    'GREY': [
        pygame.image.load("Assets\spaceshooter\PNG\Meteors\meteorGrey_big1.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Meteors\meteorGrey_big2.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Meteors\meteorGrey_big3.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Meteors\meteorGrey_big4.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Meteors\meteorGrey_med1.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Meteors\meteorGrey_med2.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Meteors\meteorGrey_small1.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Meteors\meteorGrey_small2.png")
    ]
}

LASERS = {
    'BLUE': [
        pygame.image.load("Assets\spaceshooter\PNG\Lasers\laserBlue16.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Lasers\laserBlue08.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Lasers\laserBlue10.png")
    ],
    'RED': [
        pygame.image.load("Assets\spaceshooter\PNG\Lasers\laserRed16.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Lasers\laserRed08.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Lasers\laserRed10.png")
    ],
    'GREEN': [
        pygame.image.load("Assets\spaceshooter\PNG\Lasers\laserGreen10.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Lasers\laserGreen16.png"),
        pygame.image.load("Assets\spaceshooter\PNG\Lasers\laserGreen14.png")
    ]
}

ROCKETS = [

]

print("Ship: %r" % PLAYER_SHIPS["RED"])
