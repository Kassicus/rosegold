import pygame

import lib
import player
import mass

class Level():
    def __init__(self, player_init_x: int, player_init_y: int, terrain_map: list):
        self.player_container = pygame.sprite.Group()
        self.terrain_container = pygame.sprite.Group()

        self.player = player.Player(player_init_x, player_init_y)

        self.player_container.add(self.player)

        for mass in terrain_map:
            self.terrain_container.add(mass)

    def do_collision(self):
        collision_tollerance = 15

        for t in self.terrain_container:
            if self.player.rect.colliderect(t.rect):
                if abs(self.player.rect.left - t.rect.right) < collision_tollerance:
                    self.player.vel.x = 0
                    self.player.pos.x = t.rect.right + self.player.rect.width / 2
                if abs(self.player.rect.right - t.rect.left) < collision_tollerance:
                    self.player.vel.x = 0
                    self.player.pos.x = t.rect.left - self.player.rect.width / 2
                if abs(self.player.rect.top - t.rect.bottom) < collision_tollerance:
                        self.player.vel.y = 0
                        self.player.pos.y = t.rect.bottom + self.player.rect.height / 2

                if self.player.state != 'standing':
                    if abs(self.player.rect.bottom - t.rect.top) < collision_tollerance:
                        self.player.vel.y = 0
                        self.player.vspeed = 0
                        self.player.pos.y = t.rect.top - self.player.rect.height / 2
                        self.player.state = 'standing'
                        self.player.can_jump = True
            else:
                self.player.state = 'falling'

            for p in lib.friendly_projectiles:
                if p.rect.colliderect(t.rect):
                    p.kill()

    def draw(self, surface):
        self.player_container.draw(surface)
        self.terrain_container.draw(surface)

    def update(self):
        self.player_container.update()
        self.terrain_container.update()

        self.do_collision()

    # Level objects

    # Enemies

    # Level completion goals

    # Level specific UI


# Terrain Groups

test_map = [
    mass.CollisionMass(0, 0, lib.window_size.x, 20),
    mass.CollisionMass(0, lib.window_size.y - 20, lib.window_size.x, 20),
    mass.CollisionMass(0, 20, 20, lib.window_size.y - 40),
    mass.CollisionMass(lib.window_size.x - 20, 20, 20, lib.window_size.y - 40),
    mass.CollisionMass(100, 100, lib.window_size.x - 200, 20)
]