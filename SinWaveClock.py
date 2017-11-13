import pygame
from pygame import Surface
import time
import math
import os

class SinWaveClock(pygame.Surface):
  def __init__(self, height, width, bgColor, lnColor):
    pygame.Surface.__init__(self,(width, height))
    pygame.font.init()
    self.sin_Length_ = 451
    self.sin_DotProximity_ = 14
    self.sin_DotSize_ = 8
    self.sin_Period_ = .25
    self.sin_Frequency_ = 4
    self.sin_Amplitude_ = 60 # in px
    self.sin_YDisplacment_ = -10
    self.sin_XDisplacment_ = 535
    self.sin_LnColor_ = lnColor
    self.sin_LnRadius_ = 6
    self.bgColor_ = bgColor
    self.bgSurface_ = pygame.Surface((width, height))
    self.datePosition_ = (20,10)
    self.timePosition_ = (20,80)
    self.secondsFont_ = pygame.font.Font((os.path.dirname(os.path.realpath(__file__)) + '/1979_dot_matrix.ttf'), 40)
    self.dateFont_ = pygame.font.Font((os.path.dirname(os.path.realpath(__file__)) + '/lcddot_tr.ttf'), 125)
    self.timeFont_ = pygame.font.Font((os.path.dirname(os.path.realpath(__file__)) + '/lcddot_tr.ttf'), 200)
    self.previousSec_ = int(time.time() % 60)
    self.previousTime_ = time.strftime('%I:%M %p')
    self.previousDate_ = time.strftime('%a, %b %d')
    self.textColor_ = (0,0,0)
    self.secondsSurface_ = self.secondsFont_.render(str(self.previousSec_), False, self.textColor_)
    self.dateSurface_ = self.dateFont_.render(str(self.previousDate_).upper(), False, self.textColor_)
    self.timeSurface_ = self.timeFont_.render(str(self.previousTime_), False, self.textColor_)
    self.bgSurface_.fill(bgColor)
    self.bgSurface_.convert()
    self.blit(self.bgSurface_, (0,0))
    self.convert()

  def update(self):
    currentTime = time.strftime('%I:%M %p')
    currentDate = time.strftime('%a, %b %d')
    currentSecond = int(time.time() % 60)
    if self.previousSec_ != currentSecond:
      self.secondsSurface_ = self.secondsFont_.render(str(currentSecond).rjust(2,'0'), False, self.textColor_)
      self.previousSec_ = currentSecond
    if self.previousDate_ != currentDate:
      self.dateSurface_ = self.dateFont_.render(str(currentDate).upper(), False, self.textColor_)
      self.previousDate_ = currentDate
    if self.previousTime_ != currentTime:
      self.timeSurface_ = self.timeFont_.render(str(currentTime), False, self.textColor_)
      self.previousTime_ = currentTime

    self.blit(self.bgSurface_, (0,0))
    for x in range(0, self.sin_Length_, self.sin_DotProximity_):
        y = int((self.get_height()/2) + self.sin_Amplitude_*math.sin(self.sin_Frequency_*((float(x)/self.get_width())*(2*math.pi) + ((self.sin_Period_*time.time()*math.pi - 1.4))))) + self.sin_YDisplacment_
        if (x - (self.sin_Length_)/2) > self.sin_DotProximity_/2 :
          pygame.draw.circle(self, self.sin_LnColor_, (x + self.sin_XDisplacment_,y), self.sin_LnRadius_)
        elif (x - (self.sin_Length_)/2) < self.sin_DotProximity_/2 :
          pygame.draw.circle(self, (158,0,49), (x + self.sin_XDisplacment_,y), self.sin_LnRadius_)
        if (abs(x - (self.sin_Length_)/2) < self.sin_DotProximity_/2) and (y < self.sin_YDisplacment_ + (self.get_height()/2)) :
          pygame.draw.circle(self, (0,0,0), (x + self.sin_XDisplacment_,y), self.sin_DotSize_)
          self.blit(self.secondsSurface_,(x + self.sin_XDisplacment_ - 65,y - 17))
        elif (abs(x - (self.sin_Length_)/2) < self.sin_DotProximity_/2) and (y >= self.sin_YDisplacment_ + (self.get_height()/2)):
          pygame.draw.circle(self, (158,0,49), (x + self.sin_XDisplacment_,y), self.sin_DotSize_)
          self.blit(self.secondsSurface_,(x + self.sin_XDisplacment_ - 65,y - 17))
        self.blit(self.dateSurface_, self.datePosition_)
        self.blit(self.timeSurface_, self.timePosition_)
    return self







# FOR TESTING ______________________________________
pygame.init()
clock = pygame.time.Clock()
clock.tick(15)
mainScreen = pygame.display.set_mode((1000,1000))
#  ___________________ YOU CAN EDIT ALL OF THESE ______________________
test = SinWaveClock(200, 1000, (255,255,255), (0,0,0))
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