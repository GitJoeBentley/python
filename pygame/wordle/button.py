import pygame

White = (255,255,255)

class Button:
   def __init__(self, radius, length, location, color, text, textColor = White):
      self.font = pygame.font.Font("resources/arial.ttf", int(0.9 * radius))
      self.text = self.font.render(text, True, textColor)
      self.text_rect = self.text.get_rect()
      self.text_rect.center = location
      self.rad = radius
      self.len = length
      self.loc = location
      self.color = color
      self.rect = (self.loc[0] - int(0.5 * self.len), self.loc[1] - self.rad, self.len, self.rad * 2)
      
   def draw(self, window):
      x = self.loc[0]
      y = self.loc[1]
   
      pygame.draw.circle(window, self.color, (x - self.len // 2, y), self.rad)
      pygame.draw.circle(window, self.color, (x + self.len // 2, y), self.rad)
      pygame.draw.rect(window, self.color, self.rect)
      window.blit(self.text, self.text_rect)
