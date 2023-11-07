import pygame

class Colors():
    def __init__(self):
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)

color = Colors()
window_size = pygame.math.Vector2(1920, 1080)

events = None
deltatime = 0
framerate = 120

gravity = 8