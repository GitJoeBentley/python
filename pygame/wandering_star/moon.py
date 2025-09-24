import pygame
from settings import *

class Moon(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.image: pygame.Surface = pygame.transform.rotate(pygame.image.load("resources/moon.png").convert_alpha(), 30)
        self.image.set_colorkey((4,8,40))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def move(self, direction):
        if direction == 'right':
            self.rect.centerx += 5
        if direction == 'left':
            self.rect.centerx -= 5
