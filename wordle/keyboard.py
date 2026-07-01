import pygame
from key import Key
from pygame.rect import Rect
from settings import *

class Keyboard:
    def __init__(self, window):
        self.keys  = {}
        first_row = "QWERTYUIOP"
        for i in range(len(first_row)):
            self.keys[first_row[i]] = Key(first_row[i], (.185 * GameSize[0] +  i * (KeySize[0] + 4), 0.695 * GameSize[1]))
        second_row = "ASDFGHJKL"
        for i in range(len(second_row)):
            self.keys[second_row[i]] = Key(second_row[i], (.213 * GameSize[0] +  i * (KeySize[0] + 4), 0.77 * GameSize[1]))
        third_row = "ZXCVBNM"
        for i in range(len(third_row)):
            self.keys[third_row[i]] = Key(third_row[i], (.272 * GameSize[0] +  i * (KeySize[0] + 4), 0.845 * GameSize[1]))
        self.enterKey = Rect((.167 * GameSize[0], 0.845 * GameSize[1]), (72, 52))
        self.enter_key_text = Font18.render("ENTER", True, Black)
        self.enter_key_rec = self.enter_key_text.get_rect()
        self.enter_key_rec.center = (.216 * GameSize[0], 0.88 * GameSize[1])

        self.backspaceKey = Rect((.699 * GameSize[0], 0.845 * GameSize[1]), (72, 52))
        #self.backspace = BackspaceKey("resources/backspace.png", .748 * GameSize[0], 0.879 * GameSize[1])
        self.backspace = MySprite("resources/backspace.png", .748 * GameSize[0], 0.879 * GameSize[1])

    
    def draw(self, window):
        for value in self.keys.values():
            value.draw(window)
        # draw the enter key
        pygame.draw.rect(window, LightGrey,self.enterKey,border_radius = 5)
        window.blit(self.enter_key_text, self.enter_key_rec)
        # draw the backspace key
        pygame.draw.rect(window, LightGrey,self.backspaceKey,border_radius = 5)
        window.blit(self.backspace.image, self.backspace.rect)

                                       
    
    