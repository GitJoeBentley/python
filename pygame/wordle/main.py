from game import Game
from words import Words
from settings import *
from statistics import Statistics
from datetime import date


if __name__ == "__main__":

   #  Read prior stats
   stats = Statistics.readStatsFile()
   if stats.lastDate == date.today():
      status = Status.COMPLETED
   else:
      status = Status.NEW_GAME

   if status == Status.COMPLETED:
      game = Game(stats, status)
      status = game.display_completed_game()

   while status != Status.EXIT:
      game = Game(stats, status)      
      status = game.run()
            
      if game.status == Status.EXIT:
         break
