import pygame
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
pygame.init()
screen = pygame.display.set_mode((1000,1000))
bg = pygame.image.load(dir_path + "/textured_background.jpg").convert()
sin = pygame.image.load(dir_path + "/sin.PNG").convert()
screen.blit(bg, (-100,-100))
clockScreen = pygame.Surface((545,400))
clockScreen.fill((255,255,255))

x=0
x1 = sin.get_width()
clockScreen.blit(sin,(x,0))
clockScreen.blit(sin,(x1,0))
screen.blit(clockScreen,(100,100))
start = pygame.time.get_ticks()
done = False
while done == False:
	pygame.time.wait(900)
	clockScreen.blit(sin,(x,0))
	clockScreen.blit(sin,(x1,0))
	screen.blit(clockScreen,(100,100))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	x -= 1
	x1 -= 1

	if (x + sin.get_width()) < 0:
		x = sin.get_width()
	elif (x1 + sin.get_width()) < 0:
		x1 = sin.get_width()
pygame.quit()
sys.exit()
