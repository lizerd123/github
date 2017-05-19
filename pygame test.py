import pygame,sys
from pygame.locals import *
import random
screen.blit(person,(0,0))
pygame.init()
MEMES =pygame.display.set_mode((1000,1000))
pygame.display.set_caption('memes')

def go_f():
	x=x+1

while True:
	onkey(go_f, "Up")
	listen()
	pygame.draw.rect(MEMES, (0,0,225), (x,500,20,20))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
