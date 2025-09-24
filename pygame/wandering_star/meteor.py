import pygame
from settings import *
from random import randint
from direction import Direction

class Meteor():
    def __init__(self) -> None:
        self.started: bool = False
        self.original_image: pygame.Surface = pygame.image.load("resources/white_star.png").convert_alpha()
        
        #self.rect = self.image.get_rect()
        self.whoosh_sound = pygame.mixer.Sound("resources/my_whoosh.wav")
        self.whoosh_sound.set_volume(0.25)      
        self.direction: Direction
        self.speed: int
        self.duration: int = 0

    def start(self):
        self.started = True
        meteor_size = randint(4,6)
        self.image = pygame.transform.scale(self.original_image,(meteor_size,meteor_size))
        self.rect = self.image.get_rect()
        self.whoosh_sound.play()
        self.rect.center = (WINDOW_WIDTH // 2 + 
                            randint(-WINDOW_WIDTH // 4, WINDOW_WIDTH // 4), 
                            WINDOW_HEIGHT // 2 + randint(-WINDOW_HEIGHT // 6, WINDOW_HEIGHT // 6))
        self.direction = Direction[randint(1,8)]
        #self.speed: int = 3 + randint(1,4)
        self.speed: int = 10 + randint(0,12)
        self.duration = 10 + randint(0,10)

    def move(self):
        self.duration -= 1
        if self.duration == 0:
            self.started = False
            return
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
        
