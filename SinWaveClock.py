import pygame
from pygame import Surface
import time
import math
import os

class SinWaveClock(pygame.Surface):
  def __init__(self, height, width, bgColor, lnColor):
    pygame.Surface.__init__(self,(width, height))
    pygame.font.init()
    self.sin_Length_ = self.get_width()
    self.sin_DotProximity_ = 1
    self.sin_Period_ = .25
    self.sin_Frequency_ = 4
    self.sin_Amplitude_ = 50 # in px
    self.sin_YDisplacment_ = 0
    self.sin_XDisplacment_ = 0
    self.sin_LnColor_ = lnColor
    self.sin_LnRadius_ = 4
    self.bgColor_ = bgColor
    self.bgSurface_ = pygame.Surface((width, height))
    self.secondsFont_ = pygame.font.Font((os.path.dirname(os.path.realpath(__file__)) + '/1979_dot_matrix.ttf'), 30)
    self.dateTimeFont_ = pygame.font.Font((os.path.dirname(os.path.realpath(__file__)) + '/charlie_dotted.ttf'), 150)
    self.previousSec_ = int(time.time() % 60)
    self.previousTime_ = time.strftime('%I:%M %p')
    self.previousDate_ = time.strftime('%a, %b %d')
    self.secondsSurface_ = self.secondsFont_.render(str(self.previousSec_), False, (255,255,255))
    self.dateSurface_ = self.secondsFont_.render(str(self.previousDate_), False, (255,255,255))
    self.timeSurface_ = self.dateTimeFont_.render(str(self.previousTime_), False, (255,255,255))
    self.bgSurface_.fill(bgColor)
    self.bgSurface_.convert()
    self.blit(self.bgSurface_, (0,0))
    self.convert()

  def update(self):
    currentTime = time.strftime('%I:%M %p')
    currentDate = time.strftime('%a, %b %d')
    currentSecond = int(time.time() % 60)
    if self.previousSec_ != currentSecond:
      self.secondsSurface_ = self.secondsFont_.render(str(currentSecond), False, (255,255,255))
      self.previousSec_ = currentSecond
    if self.previousDate_ != currentDate:
      self.dateSurface_ = self.secondsFont_.render(str(self.previousDate_), False, (255,255,255))
      self.previousDate_ = currentDate
    if self.previousTime_ != currentTime:
      self.timeSurface_ = self.dateTimeFont_.render(str(self.previousTime_), False, (255,255,255))
      self.previousTime_ = currentTime

    self.blit(self.bgSurface_, (0,0))
    for x in range(0, self.sin_Length_, self.sin_DotProximity_):
        y = int((self.get_height()/2) + self.sin_Amplitude_*math.sin(self.sin_Frequency_*((float(x)/self.get_width())*(2*math.pi) + ((self.sin_Period_*time.time()*math.pi))))) + self.sin_YDisplacment_
        pygame.draw.circle(self, self.sin_LnColor_, (x + self.sin_XDisplacment_,y), self.sin_LnRadius_)
        if (x - (self.sin_Length_)/2) < self.sin_DotProximity_/2 :
          pygame.draw.circle(self, (158,0,49), (x + self.sin_XDisplacment_,y), 4)
        if (abs(x - (self.sin_Length_)/2) < self.sin_DotProximity_/2) and (y < self.sin_YDisplacment_ + (self.get_height()/2)) :
          pygame.draw.circle(self, (255,255,255), (x + self.sin_XDisplacment_,y), 8)
          self.blit(self.secondsSurface_,(x + self.sin_XDisplacment_ - 55,y - 20))
        elif (abs(x - (self.sin_Length_)/2) < self.sin_DotProximity_/2) and (y >= self.sin_YDisplacment_ + (self.get_height()/2)):
          pygame.draw.circle(self, (255,255,255), (x + self.sin_XDisplacment_,y), 8)
          self.blit(self.secondsSurface_,(x + self.sin_XDisplacment_ - 55,y - 20))
        self.blit(self.dateSurface_, (10, 10))
        self.blit(self.timeSurface_, (160, 45))
    return self







# FOR TESTING ______________________________________
pygame.init()
clock = pygame.time.Clock()
clock.tick(15)
mainScreen = pygame.display.set_mode((1000,1000))
#  ___________________ YOU CAN EDIT ALL OF THESE ______________________
test = SinWaveClock(300, 700, (0,0,0), (198,225,234))
test.sin_Length_ += 5
test.sin_DotProximity_ = 10
test.sin_Period_ = .25
test.sin_Frequency_ = 4
test.sin_Amplitude_ = 50 # in px
test.sin_YDisplacment_ = 75
test.sin_XDisplacment_ = 0
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