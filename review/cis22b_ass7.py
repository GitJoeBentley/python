from random import randint

skunk = -1  

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


if __name__ == '__main__':
   d = Dice()
   d.roll()
   joe = Player("Joe", 5)
   print(joe)
