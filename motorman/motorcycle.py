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
posx=200
posy=460
bx=800
bh=15
go=0
print(bh)
screen=pygame.display.set_mode((900,700))
x=0
back=pygame.image.load("1.png")
while True:
	pygame.draw.rect(screen,(225,0,0),(0,0,900,100))
	pygame.draw.rect(screen,(0,225,0),(0,0,bh*60,100))
	screen.blit(doom,(0,400))
	if posx<=0:
		print(" __   __  _______  __   __    ______   ___   _______  ______")  
		print("|  | |  ||       ||  | |  |  |      | |   | |       ||      |") 
		print("|  |_|  ||   _   ||  | |  |  |  __   ||   | |    ___||  __   |")
		print("|       ||  | |  ||  | |  |  | |  |  ||   | |   |___ | |  |  |")
		print("|_     _||  |_|  ||  | |  |  | |__|  ||   | |    ___|| |__|  |")
		print("  |   |  |       ||  |_|  |  |       ||   | |   |___ |       |")
		print("  |___|  |_______||_______|  |______| |___| |_______||______|")
		sys.exit()

	if bh<=0:
		print(" ____    ______           _____ _______    _____ _               _____ _   _ ")
 		print("|  _ \  |  ____|   /\    / ____|__   __|  / ____| |        /\   |_   _| \ | |")
 		print("| |_) | | |__     /  \  | (___    | |    | (___ | |       /  \    | | |  \| |")
 		print("|  _ <  |  __|   / /\ \  \___ \   | |     \___ \| |      / /\ \   | | | . ` |")
 		print("| |_) | | |____ / ____ \ ____) |  | |     ____) | |____ / ____ \ _| |_| |\  |")
 		print("|____/  |______/_/    \_\_____/   |_|    |_____/|______/_/    \_\_____|_| \_|")
		sys.exit()



	firepiller=random.randrange(0,15)
	if firepiller==1:
		dy=350
		fx=random.randrange(100,670)
		go=1
	if go > 0:
		go+=1
		if go < 12:
			screen.blit(ex,(fx,500))
		if 12<go<25:
			screen.blit(doom,(fx,400))
			if posx-70<fx<posx+200:
				print(" __   __  _______  __   __    ______   ___   _______  ______")  
				print("|  | |  ||       ||  | |  |  |      | |   | |       ||      |") 
				print("|  |_|  ||   _   ||  | |  |  |  __   ||   | |    ___||  __   |")
				print("|       ||  | |  ||  | |  |  | |  |  ||   | |   |___ | |  |  |")
				print("|_     _||  |_|  ||  | |  |  | |__|  ||   | |    ___|| |__|  |")
				print("  |   |  |       ||  |_|  |  |       ||   | |   |___ |       |")
				print("  |___|  |_______||_______|  |______| |___| |_______||______|")
				sys.exit()
		if go >25:
			go=0
			dy=100



	if x>450:
		no+=1
		if no < 12:
			screen.blit(ex,(600,400))
		if 12<no<25:
			screen.blit(doom,(600,400))

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
				posx=posx-27
			if event.key==K_RIGHT:
				posx=posx+27
			if event.key==K_SPACE and bx>700:
				bx=posx
	if dx<bx<dx+100 and dy<400<dy+100:
		bh-=1

		
				


	x+=1
	time.sleep(1/7)
	back=pygame.image.load(str(x)+".png")
	if x==54:
		x=1