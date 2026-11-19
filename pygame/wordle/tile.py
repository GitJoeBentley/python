import pygame
from pygame.rect import Rect
from settings import *


class Tile():
    def __init__(self, position: (int, int), color = White):
        self.pos = position
        self.tile = Rect(position, (64, 64))
        self.letter = None
        self.letter_rect = None
        self.color = color                      # tile color

    def draw(self, window):
        if self.letter:    
            letter_text = Font48.render(self.letter, True, self.letter_color)        
            self.letter_rect = letter_text.get_rect()
            self.letter_rect.center = self.tile.center
            pygame.draw.rect(window, self.color, self.tile)
            window.blit(letter_text, self.letter_rect)
        else:
            pygame.draw.rect(window, self.color, self.tile)
    
    def set_letter(self, letter: str):
        self.letter = letter

    def set_color(self, color):
        self.color = color
        if color in (Green, Yellow, Grey):
            self.letter_color = White
        else:
            self.letter_color = Black

    def flip(self, percent) -> None:
        print("Flipping", self.letter, "by", percent)
        self.tile.scale_by(1, percent)
        self.letter_rect.scale_by(1, percent)

    def move_vertical(self, delta: int):
        self.pos = (self.pos[0], self.pos[1] + delta)

