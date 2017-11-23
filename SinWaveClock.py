import pygame
from pygame import Surface
import time
import math
import os

class SinWaveClock(pygame.Surface):
  def __init__(self, height, width, bgColor, lnColor):
    pygame.Surface.__init__(self,(width, height))
    pygame.font.init()
    self.sin_Length = self.get_width() + 5
    self.sin_DotProximity = 10
    self.sin_Period = .25
    self.sin_Frequency = 4
    self.sin_Amplitude = 50 # in px
    self.sin_YDisplacment = 75
    self.sin_XDisplacment = 0
    self.sin_LnColorPrimary = lnColor
    self.sin_LnColorSecondary = (158,0,49)
    self.sin_LnRadius = 4
    self.bgColor = bgColor
    self.bgSurface = pygame.Surface((width, height))
    self.secondsFont = pygame.font.Font((os.path.dirname(os.path.realpath(__file__)) + '/1979_dot_matrix.ttf'), 30)
    self.timeFont = pygame.font.Font((os.path.dirname(os.path.realpath(__file__)) + '/1979_dot_matrix.ttf'), 50)
    self.dateFont = pygame.font.Font((os.path.dirname(os.path.realpath(__file__)) + '/charlie_dotted.ttf'), 150)
    self.previousSec = int(time.time() % 60)
    self.previousTime = time.strftime('%I:%M %p')
    self.previousDate = time.strftime('%a, %b %d')
    self.secondsSurface = self.secondsFont.render(str(self.previousSec), False, (255,255,255))
    self.dateSurface = self.timeFont.render(str(self.previousDate), False, (255,255,255))
    self.timeSurface = self.dateFont.render(str(self.previousTime), False, (255,255,255))
    self.bgSurface.fill(bgColor)
    self.bgSurface.convert()
    self.blit(self.bgSurface, (0,0))
    self.convert()

  def update(self):
    currentTime = time.strftime('%I:%M %p')
    currentDate = time.strftime('%a, %b %d')
    currentSecond = int(time.time() % 60)
    if self.previousSec != currentSecond:
      self.secondsSurface = self.secondsFont.render(str(currentSecond), False, (255,255,255))
      self.previousSec = currentSecond
    if self.previousDate != currentDate:
      self.dateSurface = self.dateFont.render(str(currentDate), False, (255,255,255))
      self.previousDate = currentDate
    if self.previousTime != currentTime:
      self.timeSurface = self.timeFont.render(str(currentTime), False, (255,255,255))
      self.previousTime = currentTime

    self.blit(self.bgSurface, (0,0))
    for x in range(0, self.sin_Length, self.sin_DotProximity):
        y = int((self.get_height()/2) + self.sin_Amplitude*math.sin(self.sin_Frequency*((float(x)/self.get_width())*(2*math.pi) + ((self.sin_Period*time.time()*math.pi))))) + self.sin_YDisplacment
        pygame.draw.circle(self, self.sin_LnColorPrimary, (x + self.sin_XDisplacment,y), self.sin_LnRadius)
        if (x - (self.sin_Length)/2) < self.sin_DotProximity/2 :
          pygame.draw.circle(self, self.sin_LnColorSecondary, (x + self.sin_XDisplacment,y), 4)
        if (abs(x - (self.sin_Length)/2) < self.sin_DotProximity/2) and (y < self.sin_YDisplacment + (self.get_height()/2)) :
          pygame.draw.circle(self, (255,255,255), (x + self.sin_XDisplacment,y), 8)
          self.blit(self.secondsSurface,(x + self.sin_XDisplacment - 55,y - 20))
        elif (abs(x - (self.sin_Length)/2) < self.sin_DotProximity/2) and (y >= self.sin_YDisplacment + (self.get_height()/2)):
          pygame.draw.circle(self, (255,255,255), (x + self.sin_XDisplacment,y), 8)
          self.blit(self.secondsSurface,(x + self.sin_XDisplacment - 55,y - 20))
        self.blit(self.dateSurface, (10, 10))
        self.blit(self.timeSurface, (10, 45))
    return self







# FOR TESTING ______________________________________
pygame.init()
clock = pygame.time.Clock()
clock.tick(15)
mainScreen = pygame.display.set_mode((1000,1000))
#  ___________________ YOU CAN EDIT ALL OF THESE ______________________
test = SinWaveClock(300, 700, (0,0,0), (198,225,234))

pygame.display.update(test.get_rect())
running = True
while running:
  clock.tick(30)
  print(int(time.time() % 60))
  mainScreen.blit(test.update(),(0,20))

  
  for event in pygame.event.get():
    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
      running = False
  pygame.display.update(test.get_rect())
pygame.quit()