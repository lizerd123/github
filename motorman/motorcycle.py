import sys, pygame, pygame.mixer
from pygame.locals import *
pygame.init()
import time
pygame.key.set_repeat(25,25)
person = pygame.image.load("motorman.png")
deamon=pygame.image.load("deamon.png")
bullet=pygame.image.load("bullet.png")
dx=670
dy=200
posx=50
posy=240
bx=800


screen=pygame.display.set_mode((900,700))
x=0
back=pygame.image.load("1.png")
while True:
	
	bx+=100
	screen.blit(bullet,(bx,400))
	screen.blit(deamon,(dx,dy))
	pygame.display.flip()
	screen.blit(back,(0,0))
	pygame.draw.rect(screen,(0,0,0),(0,0,900,100))
	screen.blit(person,(posx,posy))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == KEYDOWN:
			if event.key==K_LEFT:
				posx=posx-20
			if event.key==K_RIGHT:
				posx=posx+20
			if event.key==K_SPACE:
				bx=posx
				


	x+=1
	time.sleep(1/7)
	back=pygame.image.load(str(x)+".png")
	if x==54:
		x=1