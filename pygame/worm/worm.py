import pygame
from settings import *

class Worm(pygame.sprite.Sprite):
    def __init__(self, sprite_group) -> None:
        super().__init__()
        self.image = pygame.image.load("resources/wormhead.png").convert_alpha()
        self.segment_image = pygame.image.load("resources/wormsegment.png").convert_alpha()
        self.image.set_colorkey((34,177,76))
        self.segment_image.set_colorkey((34,177,76))
        self.rect = self.image.get_rect()
        self.rect.center = (WindowWidth // 2, WindowHeight // 2)
        self.direction = "Up"
        self.speed = 16
        sprite_group.add(self)
        self.last_segment_location = self.rect.center
        self.segments = []
        for i in range(0,3):
            self.add_segment(sprite_group)

    def add_segment(self, sprite_group):
        segment = Segment(self.segment_image, self.last_segment_location)
        self.last_segment_location = segment.rect.center
        self.segments.append(segment)
        sprite_group.add(segment)


    def move(self, rock_group, apple) -> str:
        # move the first segment to the current head location
        #self.segments[0].rect.center = self.rect.center
        save_head_location = self.rect.center
        collide_with = None

        # move the head
        match self.direction:
            case "Up":
                self.rect.centery -= self.speed
            case "Down":
                self.rect.centery += self.speed
            case "Left":
                self.rect.centerx -= self.speed
            case "Right":
                self.rect.centerx += self.speed
        
        # advance the remaining segments
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].rect.center = self.segments[i-1].rect.center
        self.segments[0].rect.center = save_head_location

        if self.out_of_bounds():
            self.reverse_direction()
            collide_with = 'edge'
        if self.hit_a_rock(rock_group):
            self.reverse_direction()
            collide_with = "rock"
        if pygame.sprite.collide_rect(self, apple):
            apple.kill()
            collide_with = "apple"
        
        return collide_with

    def out_of_bounds(self) -> bool:
        if self.rect.centery <= 0:
            out = True
        elif self.rect.centery >= BackgroundHeight - 8:
            out = True
        elif self.rect.centerx <= 0:
            out = True
        elif self.rect.centerx >= WindowWidth:
            out = True
        else:
            out = False
        return out
    
    def hit_a_rock(self, rock_group) -> bool:
        if pygame.sprite.spritecollide(self,rock_group, False):
             #self.reverse_direction()
             return True
        return False

    def reverse_direction(self):
        match self.direction:
            case "Up": self.direction = "Down"
            case "Down": self.direction = "Up"
            case "Left": self.direction = "Right"
            case "Right": self.direction = "Left"

class Segment(pygame.sprite.Sprite):
    def __init__(self, image, last_segment_location) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (last_segment_location[0], last_segment_location[1] + 16)
        