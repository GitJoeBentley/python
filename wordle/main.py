from game import Game
from words import Words

if __name__ == "__main__":
    game = Game()
    
    print(game.stats.lastDate, game.stats.played, game.stats.currentStreak, \
          game.stats.maxStreak, game.stats.lastDate, game.stats.numberOfGuesses, '\n', \
          game.stats.distribution)
    print(game.stats.tileContents)
    
    game.run()
    print("Game Over")

