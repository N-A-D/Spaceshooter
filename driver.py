"""
Author: Ned Austin Datiles
"""
import pygame
from ships import *
from combat_tools import *
from constants import WINDOW_WIDTH, WINDOW_HEIGHT
#from game_environment_objects import *
from level import *
from random import randint

class Game:
    """
    Game class contains all the elements on the entire game
    """
    def __init__(self):
        # Create a player and put it into a drawing container
        self.player = Player(randint(0, len(PLAYER_SHIP_TYPES) - 1))
        # Initial player locations
        self.player.set_location(WINDOW_WIDTH // 2 - self.player.rect.width // 2,
                                 WINDOW_HEIGHT - 1.5 * self.player.rect.height)
        self.player_container = pygame.sprite.Group()
        self.player_container.add(self.player)
        """
        # Create the game levels
        self.level_list = self.generate_levels()
        # Index into the level list
        self.current_level_index = 0
        # Current game level
        self.current_level = self.level_list[self.current_level_index]
        """

    def draw(self, screen):
        self.current_level.draw(screen)
        self.player.draw_equipment(screen)
        self.player_container.draw(screen)

    def update(self):
        self.current_level.check_world_condition()
        self.current_level.update()
        self.player_container.update()

    def generate_levels(self):
        pass

    def controls_screen(self):
        pass

    def credits_screen(self):
        pass

    def start_screen(self, screen):
        start_screen_font = pygame.font.Font("Assets/Fonts/kenpixel_future.ttf", 70)
        end_font = pygame.font.Font("Assets/Fonts/kenpixel_blocks.ttf", 15)
        clock = pygame.time.Clock()
        while True:
            screen.fill(BLACK)
            start_screen_surf = start_screen_font.render("Espacio", True, WHITE)
            start_screen_rect = start_screen_surf.get_rect()
            start_screen_rect.center = (int(WINDOW_WIDTH // 2)), (int(WINDOW_HEIGHT // 2) - 50)
            screen.blit(start_screen_surf, start_screen_rect)

            end_screen_surf = end_font.render("Press any key to continue...", True, WHITE)
            end_screen_rect = end_screen_surf.get_rect()
            end_screen_rect.center = WINDOW_WIDTH // 2, WINDOW_HEIGHT - 2 * end_screen_rect.height
            screen.blit(end_screen_surf, end_screen_rect)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            clock.tick(60)

    def pause_screen(self, screen):
        paused_font = pygame.font.Font("Assets/Fonts/kenpixel_future.ttf", 50)
        clock = pygame.time.Clock()
        while True:
            screen.fill(BLACK)
            paused_surf = paused_font.render("PAUSED", True, WHITE)
            paused_rect = paused_surf.get_rect()
            paused_rect.center = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
            screen.blit(paused_surf, paused_rect)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            clock.tick(60)

def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    clock = pygame.time.Clock()

    game = Game()
    game.start_screen(screen)
    game.pause_screen(screen)

if __name__ == "__main__":
    main()
