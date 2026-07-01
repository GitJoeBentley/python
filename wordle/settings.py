import pygame

pygame.init()

Red = (200,0,0)
Green = (5,170,5)
Blue = (0, 0, 255)
White = (255,255,255)
Yellow = (235,220,10)
Orange = (240,140,10)
Grey = (128,128,128)
DarkGrey = (115,110,120)
LightGrey = (210,205,215)
Black = (0, 0, 0)

GameSize = (720, 768)
KeySize = (40, 52)

HelpFile =  "resources/howtoplay.txt"
WordFile =  "resources/wordle_words.txt"
GuessFile = "resources/valid_wordle_guesses.txt"
StatsFile = "resources/stats.bin"
Wrong_Sound_File = "resources/wrong.wav" # 8-Bit Wrong 2 by TheDweebMan -- https://freesound.org/s/278164/ -- License: Creative Commons 0
Click_Sound_File = "resources/click.wav" # click.wav by rulfer -- https://freesound.org/s/399097/ -- License: Creative Commons 0
Doh_Sound_File = "resources/homer_doh.wav"
ResultTxt = ["","Genius","Magnificent","Impressive","Splendid","Great","Phew", "Too bad, you lose"]

TimesFont30 = pygame.font.Font("resources/timesbd.ttf", 30)
TimesFont40 = pygame.font.Font("resources/timesbd.ttf", 40)
KeyboardFont = pygame.font.Font("resources/ATypewriterForMe.ttf", 24)
Font16 = pygame.font.Font(None, 16)
Font18 = pygame.font.Font(None, 18)
Font20 = pygame.font.Font(None, 20)
Font24 = pygame.font.Font(None, 24)
Font30 = pygame.font.Font(None, 30)
Font32 = pygame.font.Font(None, 32)
Font36 = pygame.font.Font(None, 36)
Arial16= pygame.font.Font("resources/arial.ttf", 16)
Arial24 = pygame.font.Font("resources/arial.ttf", 24)
ResultsEmojiFilename = \
    {1:"1F640.png", 2:"1F642.png", 3:"1F920.png", 4:"1F913.png", 5:"1F609.png", 7:"1F644.png", 7:"1F625.png"}

class MySprite(pygame.sprite.Sprite):
    def __init__(self, imagefile: pygame.Surface, x: int, y: int) -> None:
        super().__init__()
        self.image = pygame.image.load(imagefile).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

def blit_multiline_text(surface, text, pos, font, color=(255, 255, 255)):
   """
   Splits text by newline characters and draws it line-by-line.
   """
   x, y = pos
   # Get the height of a line for this specific font
   line_height = font.get_linesize()

   # Split the string by line breaks
   lines = text.split('\n')

   for i, line in enumerate(lines):
       # Render the individual line
       line_surface = font.render(line, True, color)
       # Blit it shifted downward by the line index * height
       surface.blit(line_surface, (x, y + (i * line_height)))

def howtoplay(window) -> None:
    with open(HelpFile, 'r') as file:
        contents = file.read()

    example = MySprite("resources/howtoplayexample.png", .5 * GameSize[0], 0.71* GameSize[1])
    running = True
    window.fill(White)
    blit_multiline_text(window, contents, (50,20), Arial16, (20,0,40))
    window.blit(example.image, example.rect)
    line = "One new word is available to play each day, but you can practice all you want."
    lastline = Arial16.render(line, True, (40,0,60))
    window.blit(lastline, (50, .93 * GameSize[1]))
    while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
    return