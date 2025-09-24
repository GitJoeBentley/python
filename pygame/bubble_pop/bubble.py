import pygame, time
from settings import *
#from direction import Direction
from random import randint

class Bubble(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, position: (int, int), direction: (float, float) = (0,0), 
                 size: float = 1.0, speed: int = 7, bounce = False) -> None:
        super().__init__()
        self.image = image
        size = int(100*size)
        self.image = pygame.transform.scale(self.image,(size,size))
        self.radius = size // 2
        #print("radius = ", self.radius)

        self.image.set_colorkey((4,8,40))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.direction = direction
        self.size = size
        self.speed = speed
        self.bounce = bounce

    def move(self):
        deltax = int(self.direction[0] * self.speed)
        deltay = int(self.direction[1] * self.speed)
        self.rect.centerx = self.rect.centerx + deltax
        self.rect.centery = self.rect.centery + deltay
        if deltax == 0 and deltay == 0:
            self.speed += 1
        if (self.bounce):
            if self.rect.right >= WINDOW_WIDTH or self.rect.left <= 0:
                self.direction = (-self.direction[0], self.direction[1])
            if self.rect.top <= 0 or self.rect.bottom >= int(0.931 * WINDOW_HEIGHT):
                self.direction = (self.direction[0], -self.direction[1])
    
    def out_of_bounds(self) -> bool:
        if self.rect.right >= WINDOW_WIDTH or self.rect.left <= 0:
                return True
        if self.rect.top <= 0 or self.rect.bottom >= int(0.931 * WINDOW_HEIGHT):
                return True
        return False




