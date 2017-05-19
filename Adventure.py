import sys, pygame, pygame.mixer
from pygame.locals import *
pygame.init()
import time
x=100
y=500



MEMES =pygame.display.set_mode((1000,800))
person = pygame.image.load("jack.png")
back=pygame.image.load("town.png")
screen = MEMES

pygame.display.set_caption('memes')

white=(225,225,225)
screen.blit(back,(0,0))

while True:
	

	for event in pygame.event.get():
		screen.blit(person,(x,y))
		if event.type == pygame.QUIT:
			sys.exit()
		pygame.display.flip()
		
		if event.type == KEYDOWN and event.key==K_ESCAPE:
			sys.exit()
		if event.type == KEYDOWN and event.key==K_RIGHT:
			x=x+10
			screen.blit(back,(0,0))

		# #if event.type == KEYDOWN and event.key==K_UP:
			
		# 	for i in range(2):
		# 		y=y+10
		# 		pygame.display.flip()
		# 		time.sleep(.5)
		# 		pygame.display.flip()
		# 		y=y+10
		# 		pygame.display.flip()
				
					
		screen.blit(back,(0,0))
		if event.type == KEYDOWN and event.key==K_LEFT:
			x=x-10
			screen.blit(back,(0,0))