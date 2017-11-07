import pygame
from pygame import Surface 
import time
import math

pygame.init()
class SinWaveClock(pygame.Surface):
  def __init__(self, Clock, height, width, bgColor, lnColor, yRangeBuffer = 20):
    pygame.Surface.__init__(self,(width, height))
    self.bgSurface_ = pygame.Surface((width, height))
    self.bgSurface_.fill(bgColor)
    self.blit(self.bgSurface_, (0,0))
    self.amplitude_buffer_ = 5
    self.period_ = 2
    self.lnColor_ = lnColor
    self.clock_ = Clock
    self.y_ = height/2
    self.x_ = width - 20
    self.timePassed_ = 0
    self.yRangeBuffer_ = yRangeBuffer

  def update(self):
    self.timePassed_ += self.clock_.get_time()
    if self.timePassed_ >= 2000:
      self.timePassed_ = 0
    self.y_ = (math.sin(self.timePassed_ * math.pi/1000) * ((self.get_height()/2) - self.yRangeBuffer_)) + ((self.get_height()/2) - 10)
    print(self.y_, self.timePassed_)
    self.bgSurface_.scroll(-1, 0)
    #print(self.lnColor_, self.get_width() - 20, int(self.y_))
    pygame.draw.circle(self.bgSurface_, self.lnColor_, (self.get_width() - 20, int(self.y_)), 5)
    self.blit(self.bgSurface_, (0,0))







# FOR TESTING ______________________________________
clock = pygame.time.Clock()
clock.tick()
mainScreen = pygame.display.set_mode((1000,1000))
test = SinWaveClock(clock, 300, 500, (255,255,255), (0,0,0))
pygame.display.update(test.get_rect())

running = True
while running:
  clock.tick()
  test.update()
  mainScreen.blit(test,(0,20))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
      running = False
  pygame.display.update(test.get_rect())
pygame.quit()