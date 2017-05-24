import sys, pygame, pygame.mixer
from pygame.locals import *
import random
pygame.init()
import time
pygame.key.set_repeat(25,25)
person = pygame.image.load("motorman.png")
deamon=pygame.image.load("deamon.png")
bullet=pygame.image.load("bullet.png")
ex=pygame.image.load("caution.png")
doom=pygame.image.load("doom.png")
dx=670
dy=100
posx=50
posy=460
bx=800
bh=10
go=0
print(bh)
#fpx=random.randrange(0, 600)
screen=pygame.display.set_mode((900,700))
x=0
back=pygame.image.load("1.png")
while True:
	if bh<=0:
		print("BEAST SLAIN")
		sys.exit()

	firepiller=random.randrange(0,60)
	if firepiller==1:
		dy=350
		fx=random.randrange(0,670)
		go=1
	if go > 0:
		go+=1
		if go < 15:
			screen.blit(ex,(fx,400))
		if 15<go<25:
			screen.blit(doom,(fx,400))
			if posx<fx<posx+150:
				print("YOU DIED")
				sys.exit()
		if go >25:
			go=0
			dy=100



	
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
			if event.key==K_SPACE and bx>700:
				bx=posx
	if dx<bx<dx+100 and dy<400<dy+100:
		bh-=1

		
				


	x+=1
	time.sleep(1/7)
	back=pygame.image.load(str(x)+".png")
	if x==54:
		x=1