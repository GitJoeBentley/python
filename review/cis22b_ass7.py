# CIS22B Assignment 7

from random import randint

skunk = -1
game_points = 100

class Dice:
   def __init__(self):
      self.die1 = 0
      self.die2 = 0
      
   def roll(self) -> int:
      sum = 0
      self.die1 = randint(1, 6)
      self.die2 = randint(1, 6)
      if self.die1 == 1 and self.die2 == 1:
         sum = skunk
      elif self.die1 == 1 or self.die2 == 1:
         sum = 0
      else:
         sum = self.die1 + self.die2
      print('   You rolled', self.die1, 'and', self.die2, "That's ", end='')
      if sum < 0:
         print('a SKUNK!!!')
      else:
         print(sum)
      return sum

class Player:
   def __init__(self, name: str, rolls_per_turn: int):
      self.name = name
      self.rolls_per_turn = rolls_per_turn
      self.points = 0

   def __str__(self) -> str:
      return self.name
   
   def take_turn(self, dice: Dice) -> int:
      points_for_turn = 0
      points_for_roll = 0
      
      print(self.name + ", it is your turn")
      for turn in range(self.rolls_per_turn):
         points_for_roll = dice.roll()
         if points_for_roll == skunk:
            points_for_turn = 0
            self.points = 0
            break
         elif points_for_roll == 0:
            points_for_turn = 0
            break
         else:
            points_for_turn += points_for_roll
            if self.points + points_for_turn >= game_points:
               break
      self.points += points_for_turn
      print("  Points for the turn =",str(points_for_turn) + ".  Total points =",self.points,"\n")
      return self.points
      
   def declare_winner(self):
      print(self.name,"won the game with",self.points,"points.)")
      

if __name__ == '__main__':
   players = [Player(entry[0], entry[1]) for entry in [('Curly', 1), ('Larry', 2), ('Moe', 4)]]
   dice = Dice()
   player_num = 0
   
   while True:
      player_points = players[player_num].take_turn(dice)
      if player_points and player_points >= 100:
         break
      if player_num == 2:
         print("----------------------------------------------")
      player_num = player_num + 1 if player_num < 2 else 0
   players[player_num].declare_winner();
   print("That's all folks!!!")
