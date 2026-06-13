import pygame
from pygame.rect import Rect
from settings import *


class Tile():
    def __init__(self, position: (int, int)):
        self.pos = position
        self.tile = Rect(position, (64, 64))
        self.letter = None
        #self.letter_color = Black
        self.color = White                      # tile color
        self.font = pygame.font.Font(None, 48)

    def draw(self, window):
        if self.letter:            
            letter_text = self.font.render(self.letter, True, self.letter_color)
            letter_rect = letter_text.get_rect()
            letter_rect.center = self.tile.center
            if self.color == White:
                pygame.draw.rect(window, DarkGrey, self.tile, 2)
            else:
                pygame.draw.rect(window, self.color, self.tile)
            window.blit(letter_text, letter_rect)
        else:
            # draw only the tile border
            pygame.draw.rect(window, LightGrey, self.tile, 2)

    
    def set_letter(self, letter: str):
        self.letter = letter

    def set_color(self, color):
        self.color = color
        if color in (Green, Yellow, Grey):
            self.letter_color = White
        else:
            self.letter_color = Black
        
