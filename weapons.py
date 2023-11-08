import pygame
import math

import lib

class Bullet(pygame.sprite.Sprite):
    def __init__(self, init_x: int, init_y: int, target_x: int, target_y: int, speed: int, damage: int):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(init_x, init_y)
        self.vel = pygame.math.Vector2()
        self.target_pos = pygame.math.Vector2(target_x, target_y)

        self.speed = speed
        self.damage = damage

        self.image = pygame.Surface([3, 3])
        self.image.fill(lib.color.red)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.vel.x, self.vel.y = self.get_vectors()

    def get_vectors(self) -> list:
        distance = [self.target_pos.x - self.pos.x, self.target_pos.y - self.pos.y]
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / normal, distance[1] / normal]
        vectors = [direction[0] * self.speed, direction[1] * self.speed]

        return vectors

    def update(self):
        self.pos += self.vel * lib.deltatime
        self.rect.center = self.pos

class Pistol():
    def __init__(self):
        self.speed = 450
        self.damage = 1

        self.mag_cap = 7
        self.mag = 7

    def shoot(self, init_x: int, init_y: int, target_x: int, target_y: int):
        if self.mag > 0:
            b = Bullet(init_x, init_y, target_x, target_y, self.speed, self.damage)
            lib.friendly_projectiles.add(b)

            self.mag -= 1
        
        else:
            pass #TODO: play empty click sound effect

    def reload(self):
        self.mag = self.mag_cap

    def check_bounds(self):
        if self.pos.x < -100:
            self.kill()
        if self.pos.x > lib.window_size.x + 100:
            self.kill()

        if self.pos.y < -100:
            self.kill()
        if self.pos.y > lib.window_size.y + 100:
            self.kill()