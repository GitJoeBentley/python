import pygame, time
from settings import *
from direction import Direction
from random import randint

class Star(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, x: int, y: int) -> None:
        super().__init__()
        self.image = image
        self.image.set_colorkey((4,8,40))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.direction = Direction[0]
        self.last_direction = Direction[0]
        self.speed = 2

    def move(self, direction = Direction[0]):
        if direction == Direction[0]:
            temp = randint(0,20)
            if temp > 9: self.direction = self.last_direction
            elif temp < 9: self.direction = Direction[temp] 
            else: pass
        
        match self.direction:
            case "N": self.rect.centery -= self.speed
            case "S": self.rect.centery += self.speed
            case "E": self.rect.centerx += self.speed
            case "W": self.rect.centerx -= self.speed
            case "NE": 
                self.rect.centerx += self.speed
                self.rect.centery -= self.speed
            case "SE": 
                self.rect.centerx += self.speed
                self.rect.centery += self.speed
            case "NW": 
                self.rect.centerx -= self.speed
                self.rect.centery -= self.speed
            case "SW": 
                self.rect.centerx -= self.speed
                self.rect.centery += self.speed
            case _:
                pass
        self.last_direction = self.direction
        if self.rect.bottom > int(.7 * WINDOW_HEIGHT):
            self.rect.centery -= 10
            self.direction = "N"


    def change_direction(self):
        if self.direction == "S": 
            self.direction = "N"
        elif self.direction == "N": 
            self.direction = "S"
        elif self.direction == "E": 
            self.direction = "W"
        elif self.direction == "W": 
            self.direction = "E"
        elif self.direction == "NE": 
            self.direction = "SW"
        elif self.direction == "NW": 
            self.direction = "SE"
        elif self.direction == "SE": 
            self.direction = "NW"
        elif self.direction == "SW": 
            self.direction = "NE"
        self.move(self.direction)
        self.move(self.direction)
        self.move(self.direction)

    def move_to(self, pos):
        self.rect.center = pos




        





