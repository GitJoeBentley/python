from datetime import datetime, timedelta, time
from settings import *
import pygame
import pickle
import math
from PIL import Image, ImageDraw, ImageFont

class Statistics:
    def __init__(self):
        self.gameNumber: int = 0
        self.lastDate: date = None           # last date played
        self.played: int = 0                 # number of games played
        self.distribution: [int] = [0] * 7   # distribution of guesses per game
        self.currentStreak = 0               # number of consecutive games won
        self.maxStreak = 0                   # max number of consecutive games won
        self.numberOfGuesses = 0             # number of guesses in a completed game
        self.tileContents = [[0]*5] *6       # contains the (letter/evaluation) history of the last active game
        
    # classmethod is bound to the class itself rather than a specific instance of that class.
    @classmethod
    def readStatsFile(cls):
        try:
            with open(StatsFile, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            print("No stats file")
            return Statistics()
    
    def writeStatsFile(self, statsObject):
        with open(StatsFile, "wb") as file:
            pickle.dump(statsObject, file)

    def display_stats(self, window, result, guesses, tiles):
        stats_window_size = (0.7 * GameSize[0],  0.8 * GameSize[1]) 
        stats = pygame.Rect((GameSize[0] / 2,  GameSize[1] / 2), stats_window_size)
        stats.center = (0.5 * GameSize[0],  0.5 * GameSize[1])
        border = pygame.Rect((GameSize[0] / 2,  GameSize[1] / 2), (stats_window_size[0] + 10, stats_window_size[1] + 10))
        border.center = (0.5 * GameSize[0],  0.5 * GameSize[1])
        X = Font30.render("x", True, White)
        X_rec = X.get_rect()
        X_rec.topright = (stats.right - 6, stats.top + 1)
        backtopuzzle = Font24.render("Back to puzzle", True, Black)
        backtopuzzle_rec = backtopuzzle.get_rect()
        backtopuzzle_rec.topleft = (stats.right - 150, stats.top + 6)

        title = Font24.render("STATISTICS", True, Black)
        title_rec = title.get_rect()
        title_rec.topleft = (stats.left + 70, stats.top + 133)
        if not result:
            guesses = 7
        result_text = TimesFont30.render(ResultTxt[guesses], True, Black)
        result_text_rec = result_text.get_rect()
        result_text_rec.center = (GameSize[0] / 2,  stats.top + 100)

        labels = Font20.render("    Played         Win %        Current Streak            Max Streak", True, Black)
        labels_rec = labels.get_rect()
        labels_rec.center = (stats.centerx, stats.top + 195)

        dist_title = Font24.render("GUESS DISTRIBUTION", True, Black)
        dist_title_rec = dist_title.get_rect()
        dist_title_rec.midleft = (stats.left + 70, stats.top + 240)

        next_wordle = Font24.render("NEXT WORDLE", True, Black)
        next_wordle_rec = next_wordle.get_rect()
        next_wordle_rec.center = (stats.centerx, stats.bottom - 55)

        pct = int(100 * sum(self.distribution) / self.played)
        stats_str = str(self.played).rjust(3) + str(pct).rjust(10) + str(self.currentStreak).rjust(14) + str(self.maxStreak).rjust(19) 
        stats_text = Font32.render(stats_str, True, Black)
        stats_text_rec = stats_text.get_rect()
        stats_text_rec.center = (stats.centerx, stats.top + 171)
        maxbarlength = 500
        barlength = [maxbarlength * self.distribution[i]/self.played for i in range(7)]

        filename = "resources/" + ResultsEmojiFilename[guesses]
        resultEmoji = MySprite(filename, stats.centerx, stats.top + 51)
        shareButton = MySprite("resources/share_button.png", stats.centerx + 110, stats.top + 500)
        practiceButton = MySprite("resources/practice_button.png", stats.centerx - 110, stats.top + 500)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button == 1:
                        if pygame.math.Vector2(event.pos).distance_to(X_rec.center) < 18.4:
                            return

                        if pygame.math.Vector2(event.pos).distance_to(shareButton.rect.center) < 50:
                            img = self.copyGameImage(guesses, tiles)
                            filename = "results" + str(self.gameNumber) + ".png"
                            img.save(filename)
                            #message(window, "Game results written to file " + filename)

            pygame.draw.rect(window, (0, 0, 150), border)
            pygame.draw.rect(window, (245, 245, 245), stats)
            pygame.draw.rect(window, (200, 0, 0), (stats.right - 25, stats.top, 26, 26))
            window.blit(backtopuzzle, backtopuzzle_rec)
            window.blit(X, X_rec)
            window.blit(title,title_rec)
            window.blit(result_text, result_text_rec)
            window.blit(labels,labels_rec)
            window.blit(dist_title, dist_title_rec)
            window.blit(stats_text, stats_text_rec)
            window.blit(next_wordle, next_wordle_rec)

            # Draw guess distribution
            for i in range(1,7):
                if i == guesses:
                    barcolor = Green
                else:
                    barcolor = DarkGrey
                
                number = Font24.render(str(i), True, Black)
                number_rec = number.get_rect()
                number_rec.topleft = (stats.left + 70, stats.top + 235 + 32 * i)
                window.blit(number, number_rec)
                pygame.draw.rect(window, barcolor, (stats.left + 84, stats.top + 231 + 32 * i, barlength[i] + 16, 24))

                number = Font20.render(str(self.distribution[i]).rjust(2), True, White)
                number_rec = number.get_rect()
                number_rec.topleft = (stats.left + 74 + barlength[i] - 3, stats.top + 237 + 32 * i)
                window.blit(number, number_rec)
            # Determine next time
            now = datetime.now()
            # Combine tomorrow's date with midnight time (00:00:00)
            midnight = datetime.combine(now + timedelta(days=1), time())
            sec_til_midnight = int((midnight - now).total_seconds())
            hrs = sec_til_midnight // 3600
            min = (sec_til_midnight - hrs * 3600) // 60
            sec = sec_til_midnight - hrs * 3600 - min * 60 
            time_str = str(hrs).rjust(2,'0') + ':' + str(min).rjust(2,'0') + ':' + str(sec).rjust(2,'0')
            time_text = Font36.render(time_str, True, Red)
            time_text_rec = time_text.get_rect()
            time_text_rec.center = (stats.centerx, stats.bottom - 25)
            window.blit(time_text, time_text_rec)
            window.blit(shareButton.image, shareButton.rect)
            window.blit(practiceButton.image, practiceButton.rect)
            window.blit(resultEmoji.image, resultEmoji.rect)
            #message(window, "Press F1 to play a practice game")
            pygame.display.flip()
        return

    def copyGameImage(self, guesses, tiles) -> Image:
        img = Image.new("RGB", (200, 200), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 16)
        draw.text((42, 15), "Wordle " + str(self.gameNumber) + "  " + str(guesses) + "/6", fill="black", font=font)
        y1 = 20
        for row in range(guesses):
            y1 += 22
            y2 = y1 + 20
            x1 = 20
            for col in range(5):
                ascii_code = ord(tiles[row][col].letter)
                color_code = [Grey, Yellow, Green].index(tiles[row][col].color)
                x1 += 22
                x2 = x1 + 20
                
                draw.rectangle((x1, y1, x2, y2), fill=[Grey, Yellow, Green][color_code])
        return img


            



