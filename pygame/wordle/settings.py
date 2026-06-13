import pygame

pygame.init()

Red = (200,0,0)
Green = (5,170,5)
White = (255,240,240)
Yellow = (190,180,60)
Grey = (128,128,128)
DarkGrey = (115,110,120)
LightGrey = (210,205,215)
Black = (0, 0, 0)

GameSize = (720, 768)
KeySize = (40, 52)

WordFile =  "resources/wordle_words.txt"
GuessFile = "resources/valid_wordle_guesses.txt"
StatsFile = "resources/stats.bin"
Wrong_Sound_File = "resources/wrong.wav" # 8-Bit Wrong 2 by TheDweebMan -- https://freesound.org/s/278164/ -- License: Creative Commons 0
Click_Sound_File = "resources/click.wav" # click.wav by rulfer -- https://freesound.org/s/399097/ -- License: Creative Commons 0
Doh_Sound_File = "resources/homer_doh.wav"

TitleFont = pygame.font.Font("resources/timesbd.ttf", 48)
KeyboardFont = pygame.font.Font("resources/ATypewriterForMe.ttf", 24)
Font16 = pygame.font.Font(None, 16)
Font18 = pygame.font.Font(None, 18)
Font20 = pygame.font.Font(None, 20)
Font24 = pygame.font.Font(None, 24)
Font30 = pygame.font.Font(None, 30)
Font32 = pygame.font.Font(None, 32)
Font36 = pygame.font.Font(None, 36)

class BackspaceKey(pygame.sprite.Sprite):
    def __init__(self, imagefile: pygame.Surface, x: int, y: int) -> None:
        super().__init__()
        self.image = pygame.image.load(imagefile).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
