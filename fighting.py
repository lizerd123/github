
import sys, pygame, pygame.mixer
from pygame.locals import *
import random
p1space=2
print("Viking, Knight, Spearman")
p1=raw_input("chose your fighter!")
if p1=="Viking":
	p1=pygame.image.load("viking.png")
screen=pygame.display.set_mode((300,300))
back=pygame.image.load("arena.png")
while True:
	screen.blit(back,(0,0))		
	screen.blit(p1,(90,260))	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
		  	if event.key == K_d:
		  		p1space-=1