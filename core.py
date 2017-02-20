"""
Author: Ned Austin Datiles
"""
from xml.dom.minidom import parse
import xml.dom.minidom
import pygame

def create_sprite_list(DOMTree, List):
    TextureAtlas = DOMTree.documentElement
    SubTextures = TextureAtlas.getElementsByTagName("SubTexture")
    # A list of sprites
    SPRITE_LIST = []

    for SubTexture in SubTextures:
        name = SubTexture.getAttribute("name")
        x = int(SubTexture.getAttribute("x"))
        y = int(SubTexture.getAttribute("y"))
        width = int(SubTexture.getAttribute("width"))
        height = int(SubTexture.getAttribute("height"))
        for item in List:
            if item in name and "damage" not in name:
                sprite = {"name": name, "x": x, "y": y, "width": width, "height": height}
                SPRITE_LIST.append(sprite)
    return SPRITE_LIST

def load_images(sprite_list, scale, sprite_sheet):
    image = None
    for i in range(len(sprite_list)):
        image = pygame.Surface([
            sprite_list[i]["width"], sprite_list[i]["height"]
        ])
        image.blit(sprite_sheet, [0, 0], [
            sprite_list[i]["x"], sprite_list[i]["y"],
            sprite_list[i]["width"], sprite_list[i]["height"]
        ])
        if scale:
            image = pygame.transform.smoothscale(image, scale)
        image.set_colorkey((0,0,0))
        if "spaceBuilding" in sprite_list[i]["name"]:
            image = pygame.transform.flip(image, False, True)
        sprite_list[i]["image"] = image

def manipulate_sprite_sheet():
    DOMTree = xml.dom.minidom.parse("Assets/sheet.xml")

    # A list of all the player ships
    PLAYER_SHIP_LIST = create_sprite_list(DOMTree, ["playerShip"])

    # A list of all enemy ships
    ENEMY_SHIP_LIST = create_sprite_list(DOMTree, ["enemy"])

    # A list of different meteors
    METEOR_LIST = create_sprite_list(DOMTree, ["meteor"])

    # A list of different types of lasers
    LASER_LIST = create_sprite_list(DOMTree, ["laserBlue02.png","laserBlue03.png","laserBlue04.png","laserBlue05.png","laserBlue12.png","laserBlue13.png","laserBlue14.png","laserBlue15.png","laserGreen02.png","laserGreen03.png","laserGreen04.png","laserGreen05.png","laserGreen06.png","laserGreen07.png","laserGreen08.png","laserGreen09.png","laserRed02.png","laserRed03.png","laserRed04.png","laserRed05.png","laserRed12.png","laserRed13.png","laserRed14.png","laserRed15.png"])

    # A list of all the different power ups
    POWER_UP_LIST = create_sprite_list(DOMTree, ["powerup", "things"])

    # A list of shields
    SHIELD = create_sprite_list(DOMTree, ["shield1.png", "shield2.png", "shield3.png"])
    SHIELD.reverse()

    LASER_ANIMATIONS = create_sprite_list(DOMTree, [
        'laserBlue08.png', 'laserBlue09.png', 'laserBlue10.png',
        'laserBlue11.png', 'laserGreen01.png', 'laserGreen14.png',
        'laserGreen15.png', 'laserGreen16.png', 'laserRed08.png',
        'laserRed09.png', 'laserRed10.png', 'laserRed11.png'
    ])

    DOMTree = xml.dom.minidom.parse("Assets/sheet2.xml")

    # Other enemy sprites not found in the original sprite sheet
    ENEMY_LIST_EXTRA = create_sprite_list(DOMTree, ["spaceShip"])

    sheet1 = pygame.image.load("Assets/sheet.png")
    sheet2 = pygame.image.load("Assets/sheet2.png")
    load_images(LASER_ANIMATIONS, (16, 16), sheet1)
    load_images(PLAYER_SHIP_LIST, (25, 25), sheet1)
    load_images(ENEMY_SHIP_LIST, (25, 25), sheet1)
    load_images(METEOR_LIST, None, sheet1)
    load_images(LASER_LIST, (2, 7), sheet1)
    load_images(POWER_UP_LIST, None, sheet1)
    load_images(SHIELD, (45, 45), sheet1)
    load_images(ENEMY_LIST_EXTRA, (25, 25), sheet2)

    ENEMY_SHIP_LIST.extend(ENEMY_LIST_EXTRA)

    return PLAYER_SHIP_LIST, ENEMY_SHIP_LIST, METEOR_LIST, LASER_LIST, POWER_UP_LIST, SHIELD, LASER_ANIMATIONS

PLAYER_SHIP_TYPES, ENEMY_SHIP_TYPES, METEOR_TYPES, \
AMMO_TYPES, POWER_UP_TYPES, SHIELD, LASER_ANIMATIONS = manipulate_sprite_sheet()