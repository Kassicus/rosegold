import pygame

import lib

class Player(pygame.sprite.Sprite):
    def __init__(self, init_x: int, init_y: int):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(init_x, init_y)
        self.vel = pygame.math.Vector2()

        self.hspeed = 0
        self.vspeed = -10

        self.image = pygame.Surface([20, 30])
        self.image.fill(lib.color.white)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.vel.y += self.vspeed
        self.pos += self.vel * lib.deltatime
        self.rect.center = self.pos

        if self.vspeed < lib.gravity:
            self.vspeed += 0.3
        else:
            self.vspeed = lib.gravity