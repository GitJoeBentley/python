import pygame
import math
from settings import *
from random import randint

class Rock(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, sprite_group: pygame.sprite.Group, rock_group: pygame.sprite.Group) -> None:
        super().__init__()
        image_length = image.get_rect()[2]     
        image.set_colorkey((34,177,76))
        new_length = image_length // randint(5,12)
        image = pygame.transform.scale(image,(new_length,int(.75 * new_length)))

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = find_good_sprite_location(sprite_group)
        sprite_group.add(self)
        rock_group.add(self)

    
