import pygame
from pygame import Surface
import time
import math
import os

class SinWaveClock(pygame.Surface):
  def __init__(self, height, width):
    pygame.Surface.__init__(self,(width, height))
    pygame.font.init()
    # All values that can edit the sin wave clock
    self.sin_Length = self.get_width() + 5
    # If zero it will just be a line
    self.sin_DotProximity = 10
    # .5 is 1 second period
    self.sin_Period = .25
    self.sin_Frequency = 4
    self.sin_Amplitude = 50 # in px
    self.sin_YDisplacment = 75
    self.sin_XDisplacment = 0
    # Color for dots in the future
    self.sin_LnColorPrimary = (198,225,234)
    # Clolor for dots in the past
    self.sin_LnColorSecondary = (158,0,49)
    # Size of dots
    self.sin_LnRadius = 4
    self.bgColor = (0,0,0)
    self.bgSurface = pygame.Surface((width, height))
    # FONTS
    self.secondsFont = pygame.font.Font((os.path.dirname(os.path.realpath(__file__)) + '/1979_dot_matrix.ttf'), 30)
    self.dateFont = pygame.font.Font((os.path.dirname(os.path.realpath(__file__)) + '/1979_dot_matrix.ttf'), 50)
    self.timeFont = pygame.font.Font((os.path.dirname(os.path.realpath(__file__)) + '/charlie_dotted.ttf'), 150)
    self.fontColor = (255,255,255)
    self.previousSec = int(time.time() % 60)
    self.previousTime = time.strftime('%I:%M %p')
    self.previousDate = time.strftime('%a, %b %d')
    self.secondsSurface = self.secondsFont.render(str(self.previousSec), False, (255,255,255))
    self.dateSurface = self.dateFont.render(str(self.previousDate), False, (255,255,255))
    self.timeSurface = self.timeFont.render(str(self.previousTime), False, (255,255,255))
    self.bgSurface.fill(self.bgColor)
    self.bgSurface.convert()
    self.blit(self.bgSurface, (0,0))
    self.convert()

  def update(self):
    currentTime = time.strftime('%I:%M %p')
    currentDate = time.strftime('%a, %b %d')
    currentSecond = int(time.time() % 60)
    if self.previousSec != currentSecond:
      self.secondsSurface = self.secondsFont.render(str(currentSecond), False, self.fontColor)
      self.previousSec = currentSecond
    if self.previousDate != currentDate:
      self.dateSurface = self.dateFont.render(str(currentDate), False, self.fontColor)
      self.previousDate = currentDate
    if self.previousTime != currentTime:
      self.timeSurface = self.timeFont.render(str(currentTime), False, self.fontColor)
      self.previousTime = currentTime

    self.blit(self.bgSurface, (0,0))
    # Traverses through every pixel from left to right for sin wave and prints every frame
    for x in range(0, self.sin_Length, self.sin_DotProximity):
        # Find the points on a sine wave
        y = int((self.get_height()/2) + self.sin_Amplitude*math.sin(self.sin_Frequency*((float(x)/self.get_width())*(2*math.pi) + ((self.sin_Period*time.time()*math.pi))))) + self.sin_YDisplacment
        # Draw dots infront of seconds counts
        pygame.draw.circle(self, self.sin_LnColorPrimary, (x + self.sin_XDisplacment,y), self.sin_LnRadius)
        if (x - (self.sin_Length)/2) < self.sin_DotProximity/2 :
          # Draw dots behind seconds counter if behind the middle mark of sinwave.
          pygame.draw.circle(self, self.sin_LnColorSecondary, (x + self.sin_XDisplacment,y), 4)
        # Draws larger second counter Dot
        if (abs(x - (self.sin_Length)/2) < self.sin_DotProximity/2) and (y < self.sin_YDisplacment + (self.get_height()/2)) :
          pygame.draw.circle(self, self.sin_LnColorPrimary, (x + self.sin_XDisplacment,y), 8)
          self.blit(self.secondsSurface,(x + self.sin_XDisplacment - 55,y - 20))
        elif (abs(x - (self.sin_Length)/2) < self.sin_DotProximity/2) and (y >= self.sin_YDisplacment + (self.get_height()/2)):
          pygame.draw.circle(self, self.sin_LnColorSecondary, (x + self.sin_XDisplacment,y), 8)
          self.blit(self.secondsSurface,(x + self.sin_XDisplacment - 55,y - 20))
        self.blit(self.dateSurface, (10, 10))
        self.blit(self.timeSurface, (10, 45))
    return self