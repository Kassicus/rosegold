import pygame

import level

class World():
    def __init__(self):
        self.levels = []
        self.active_level = None

    def add_level(self, player_init_x: int, player_init_y: int):
        self.levels.append(level.Level(player_init_x, player_init_y, level.test_map))

    def set_active_level(self, index: int):
        self.active_level = self.levels[index]

    def draw(self, surface):
        if self.active_level is not None:
            self.active_level.draw(surface)

    def update(self):
        if self.active_level is not None:
            self.active_level.update()

    # UI to move between levels

    # Logic to start each level

world_one = World()

world_one.add_level(600, 50)
world_one.set_active_level(0)