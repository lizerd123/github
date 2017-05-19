import sys, pygame, pygame.mixer
from pygame.locals import *
pygame.init()
import time
screen=pygame.display.set_mode((900,470))
x=0
back=pygame.image.load("1.png")
while True:
	pygame.display.flip()
	screen.blit(back,(0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	x+=1
	if x==1:
		back=pygame.image.load("1.png")
	if x==2:
		back=pygame.image.load("2.png")
	if x==3:
		back=pygame.image.load("3.png")
	if x==4:
		back=pygame.image.load("4.png")
	if x==5:
		back=pygame.image.load("5.png")
	if x==6:
		back=pygame.image.load("6.png")
	if x==7:
		back=pygame.image.load("7.png")
	if x==8:
		back=pygame.image.load("8.png")
	if x==9:
		back=pygame.image.load("9.png")
	if x==10:
		back=pygame.image.load("10.png")
	if x==11:
		back=pygame.image.load("11.png")
	if x==12:
		back=pygame.image.load("12.png")
		x=1
