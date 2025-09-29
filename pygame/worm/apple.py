import pygame
from settings import *
from random import randint

class Apple(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, sprite_group: pygame.sprite.Group) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = find_good_sprite_location(sprite_group)
        #self.rect.center = (randint(50, WindowWidth - 40), randint(50, BackgroundHeight - 30))
        sprite_group.add(self)