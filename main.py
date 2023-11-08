import pygame

import lib
import world

pygame.init()

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode([lib.window_size.x, lib.window_size.y])
        pygame.display.set_caption("Project Rose Gold")

        self.running = True
        self.clock = pygame.time.Clock()
        lib.events = pygame.event.get()

        self.worlds = []

        self.worlds.append(world.world_one)

        self.active_world = self.worlds[0]

    def start(self):
        while self.running:
            self.events()
            self.draw()
            self.update()

    def events(self):
        lib.events = pygame.event.get()

        for event in lib.events:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False

    def draw(self):
        self.screen.fill(lib.color.black)

        self.active_world.draw(self.screen)

        lib.friendly_projectiles.draw(self.screen)

    def update(self):
        self.active_world.update()

        lib.friendly_projectiles.update()

        pygame.display.update()
        lib.deltatime = self.clock.tick(lib.framerate) / 1000

if __name__ == '__main__':
    game = Game()
    game.start()
    pygame.quit()