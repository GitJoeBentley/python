from tile import Tile
from keyboard import Keyboard
from words import Words
from statistics import Statistics
from datetime import date
from settings import *
import pygame
import time

class Game:
    def __init__(self):
        """Initialize the game, and create game resources."""
        self.words = Words()
        print(self.words.word)  # for debugging
        pygame.init()
        self.window = pygame.display.set_mode(GameSize)
        self.window_width = self.window.get_rect().width
        self.window_height = self.window.get_rect().height
        pygame.display.set_caption("Wordle by Joe")
        self.bg_color = White
        # sounds
        self.letter_click = pygame.mixer.Sound(Click_Sound_File)
        self.letter_click.set_volume(0.30)
        self.wrong_guess = pygame.mixer.Sound(Wrong_Sound_File)
        self.wrong_guess.set_volume(0.35)
        self.doh = pygame.mixer.Sound(Doh_Sound_File)
        self.doh.set_volume(0.95)

        self.title = TitleFont.render("WORDLE by Joe", True, Black)
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (GameSize[0]/2, GameSize[1]/24)

        self.tile = Tile((00, 0))
        self.tiles = []
        for row in range(6):
            row_of_tiles = [Tile((GameSize[0]/3.8 + col * 69, GameSize[1]/7 + row * 69)) for col in range(5)]
            self.tiles.append(row_of_tiles)

        # Keyboard
        self.keyboard = Keyboard(self.window)

        # Create Statistics object by attempting to read Stats file
        self.stats = Statistics.readStatsFile()

    def run(self):
        self.window.fill(self.bg_color)
        running = True
        targetRow = 0
        targetCol = 0
        evaluation = []
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    ltr = pygame.key.name(event.key).upper()
                    
                    if ltr == "BACKSPACE" and targetCol > 0:
                        targetCol -= 1
                        self.tiles[targetRow][targetCol].set_letter(' ')
                        self.tiles[targetRow][targetCol].set_color(White)
                        break
                    if ltr == "RETURN":
                        if targetCol < 5:
                            self.doh.play()
                            break
                        guess = "".join([self.tiles[targetRow][i].letter for i in range(5)])
                        goodGuess = self.words.isValidWord(guess)
                        if not goodGuess:
                            self.wrong_guess.play()
                            self.wiggleTiles(targetRow)
                            break

                        evaluation = self.words.evaluateGuess(guess)
                        self.update_tiles(targetRow, evaluation)
                        
                        targetRow += 1
                        targetCol = 0
                        break
                    # ignore invalid letters
                    if ltr < 'A' or ltr > 'Z' or targetCol > 4:
                        break
                    self.letter_click.play()
                    self.tiles[targetRow][targetCol].set_color(White)
                    self.tiles[targetRow][targetCol].set_letter(ltr)
                    targetCol += 1
                    break
                
            self.window.fill(White)
            self.draw()
            pygame.display.flip()
            if sum(evaluation) == 10:
                self.gameOver(targetRow, True)
                pygame.quit()
                return
            if targetRow == 6:
                self.gameOver(6, False)
                pygame.quit()
                return

    def draw(self):
        for row in range(6):
            for col in range(5):
                self.tiles[row][col].draw(self.window)
        pygame.draw.line(self.window, Black, (0, GameSize[1]/12), (GameSize[0], GameSize[1]/12) , 1)
        self.keyboard.draw(self.window)
        self.window.blit(self.title, self.title_rect)

    def update_tiles(self, row: int, evaluation: [int]):
        for i in range(5):
            if evaluation[i] == 0:
                self.tiles[row][i].set_color(Grey)
                if self.keyboard.keys[self.tiles[row][i].letter].color == LightGrey:
                    self.keyboard.keys[self.tiles[row][i].letter].set_color(DarkGrey)
            elif evaluation[i] == 1:
                self.tiles[row][i].set_color(Yellow)
                if self.keyboard.keys[self.tiles[row][i].letter].color != Green:
                    self.keyboard.keys[self.tiles[row][i].letter].set_color(Yellow)

            elif evaluation[i] == 2:
                self.tiles[row][i].set_color(Green)
                self.keyboard.keys[self.tiles[row][i].letter].set_color(Green)

    def wiggleTiles(self, row):
        deltas = (-5, 0, 5)
        for switch in range(14):
            delta = deltas[switch % 3]
            for col in range(5):
                new_rect_specs = (self.tiles[row][col].pos[0] + delta, self.tiles[row][col].pos[1], 64, 64)
                self.tiles[row][col].tile.update(new_rect_specs)
            self.window.fill(White)
            self.draw()
            pygame.display.flip()
            time.sleep(0.05)

    def gameOver(self, guesses, result):
        print(guesses, result)
        if result == True:
            filename = "resources/win" + str(guesses) + ".wav"
            cheer = pygame.mixer.Sound(filename)
            cheer.set_volume(0.4)
            cheer.play()
           
        else:
            filename = "resources/lose.wav"
            lose = pygame.mixer.Sound(filename)
            lose.set_volume(0.5)
            lose.play()

        time.sleep(3)   # this will need to be increased
        self.updateStats(result, guesses)
        self.stats.display_stats(self.window, result, guesses)

        return

    def updateStats(self, result, guesses):
        self.stats.lastDate = date.today()
        self.stats.played += 1
        self.stats.tileContents = []
        for row in range(6):
            temp = []
            for col in range(5):
                if self.tiles[row][col].letter:
                    ascii_code = ord(self.tiles[row][col].letter)
                    color_code = [Grey, Yellow, Green].index(self.tiles[row][col].color)
                else:
                    ascii_code = 0
                    color_code = 0
                print(ascii_code * 100 + color_code, end=' ')
                temp.append(ascii_code * 100 + color_code)
            self.stats.tileContents.append(temp)              
            print("")

        if result:
            self.stats.numberOfGuesses = guesses
            self.stats.distribution[guesses] += 1
            self.stats.currentStreak += 1
            if self.stats.currentStreak > self.stats.maxStreak:
                self.stats.maxStreak = self.stats.currentStreak
        else:
            self.stats.currentStreak += 0
        self.stats.writeStatsFile(self.stats)
