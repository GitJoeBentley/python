import pygame
from pygame.rect import Rect
from settings import *


class Key():
    def __init__(self, letter: str, position: (int, int)):
        self.pos = position
        self.key = Rect(position, KeySize)
        self.letter = letter
        self.color = LightGrey                      # key color

    def draw(self, window):
        if self.letter:            
            letter_text = KeyboardFont.render(self.letter, True, Black)
            letter_rect = letter_text.get_rect()
            letter_rect.center = self.key.center
            pygame.draw.rect(window, self.color, self.key,border_radius = 5)
            window.blit(letter_text, letter_rect)
    
    def set_letter(self, letter: str):
        self.letter = letter

    def set_color(self, color):
        self.color = color