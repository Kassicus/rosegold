import pygame

import lib
import player

class Level():
    def __init__(self, player_init_x: int, player_init_y: int):
        self.player_container = pygame.sprite.Group()

        self.player_container.add(player.Player(player_init_x, player_init_y))

    def draw(self, surface):
        self.player_container.draw(surface)

    def update(self):
        self.player_container.update()

    # Level objects

    # Enemies

    # Level completion goals

    # Level specific UI