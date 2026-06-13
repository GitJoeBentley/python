import pygame
from key import Key
from pygame.rect import Rect
from settings import *

class Keyboard:
    def __init__(self, window):
        self.keys  = {}
        first_row = "QWERTYUIOP"
        for i in range(len(first_row)):
            self.keys[first_row[i]] = Key(first_row[i], (.185 * GameSize[0] +  i * (KeySize[0] + 4), 0.71 * GameSize[1]))
        second_row = "ASDFGHJKL"
        for i in range(len(second_row)):
            self.keys[second_row[i]] = Key(second_row[i], (.213 * GameSize[0] +  i * (KeySize[0] + 4), 0.7875 * GameSize[1]))
        third_row = "ZXCVBNM"
        for i in range(len(third_row)):
            self.keys[third_row[i]] = Key(third_row[i], (.272 * GameSize[0] +  i * (KeySize[0] + 4), 0.86 * GameSize[1]))
        self.enterKey = Rect((.167 * GameSize[0], 0.86 * GameSize[1]), (72, 52))
        #self.enterKeyFont = pygame.font.Font(None, 18)
        #self.enter_key_text = self.enterKeyFont.render("ENTER", True, Black)
        self.enter_key_text = Font18.render("ENTER", True, Black)
        self.enter_key_rec = self.enter_key_text.get_rect()
        self.enter_key_rec.center = (.216 * GameSize[0], 0.896 * GameSize[1])
        self.backspaceKey = BackspaceKey("resources/backspace_key.png", .7474 * GameSize[0], 0.893 * GameSize[1] )

    
    def draw(self, window):
        for value in self.keys.values():
            value.draw(window)
        pygame.draw.rect(window, LightGrey,self.enterKey,border_radius = 5)
        window.blit(self.enter_key_text, self.enter_key_rec)
        # draw the backspace key
        window.blit(self.backspaceKey.image, self.backspaceKey.rect)

                                       
    
    