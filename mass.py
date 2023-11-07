import pygame

import lib

class CollisionMass(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)

        self.image = pygame.Surface([width, height])
        self.image.fill(lib.color.blue)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        pass