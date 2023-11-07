import pygame

import lib

class Player(pygame.sprite.Sprite):
    def __init__(self, init_x: int, init_y: int):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(init_x, init_y)
        self.vel = pygame.math.Vector2()

        self.hspeed = 250
        self.vspeed = 0

        self.state = 'falling'
        self.can_jump = False

        self.image = pygame.Surface([20, 30])
        self.image.fill(lib.color.white)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def movement_handler(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.vel.x = self.hspeed
        elif keys[pygame.K_a]:
            self.vel.x = -self.hspeed
        else:
            self.vel.x = 0

        for event in lib.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.can_jump:
                        self.vel.y = -500
                        self.state = 'falling'
                        self.can_jump = False

    def update(self):
        self.vel.y += self.vspeed
        self.pos += self.vel * lib.deltatime
        self.rect.center = self.pos

        self.movement_handler()

        if self.state == 'falling':
            if self.vspeed < lib.gravity:
                self.vspeed += 0.3
            else:
                self.vspeed = lib.gravity
        elif self.state == 'standing':
            self.vspeed = 0