import pygame
from pygame.rect import Rect
from settings import *


class Tile():
    def __init__(self, position: (int, int)):
        self.pos = position
        self.tile = Rect(position, (64, 64))
        self.letter = None
        self.color = White                      # tile color
        self.font = pygame.font.Font(None, 48)

    def draw(self, window):
        if self.letter:            
            letter_text = self.font.render(self.letter, True, self.letter_color)
            letter_rect = letter_text.get_rect()
            letter_rect.center = self.tile.center
            pygame.draw.rect(window, self.color, self.tile)
            window.blit(letter_text, letter_rect)
        else:
            pygame.draw.rect(window, White, self.tile)
    
    def set_letter(self, letter: str):
        self.letter = letter

    def set_color(self, color):
        self.color = color
        if color in (Green, Yellow, Grey):
            self.letter_color = White
        else:
            self.letter_color = Black
