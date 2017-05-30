import sys, pygame, pygame.mixer
from pygame.locals import *
import random
import time
print("'You must hunt down the beast that has plauged this land, do so using arrow keys or A and D to accelerate or decellerate, use space to fire, take cation in doing so as it will prevent you from speeding up'")
print("(1)easy,(2)medium,(3)hard,(4)NIGHTMARE")
difficulty=input()
pygame.init()

pygame.key.set_repeat(25,25)
person = pygame.image.load("motorman.png")
deamon=pygame.image.load("deamon.png")
bullet=pygame.image.load("bullet.png")
ex=pygame.image.load("caution.png")
doom=pygame.image.load("doom.png")
intro=pygame.image.load("instructions.png")
go=0
dx=670
dy=100
posx=200
posy=460
bx=800
if difficulty==1 and go<1:
	bh=random.randrange(10,20)
	r1=12
	r2=29
if difficulty==2 and go<1:
	bh=random.randrange(20,30)
	r1=10
	r2=27
if difficulty==3 and go<1:
	bh=random.randrange(30,40)
	r1=9
	r2=25
if difficulty==4 and go<1:
	bh=random.randrange(40,50)
	r1=8
	r2=23
ticks=900/bh
go=0
print(bh)
screen=pygame.display.set_mode((900,700))
x=0
back=pygame.image.load("1.png")
screen.blit(intro,(0,0))




while True:
	if difficulty==1:
		firepiller=random.randrange(0,26)
	if difficulty==2:
		firepiller=random.randrange(0,23)
	if difficulty==3:
		firepiller=random.randrange(0,18)
	if difficulty==4:
		firepiller=random.randrange(0,13)
	pygame.draw.rect(screen,(225,0,0),(0,0,900,100))
	pygame.draw.rect(screen,(0,225,0),(0,0,bh*ticks,100))
	screen.blit(doom,(0,400))
	if posx<=0:
		print('" __   __  _______  __   __    ______   ___   _______  ______  "')  
		print('"|  | |  ||       ||  | |  |  |      \ |   | |       ||      \ "') 
		print('"|  | |  ||   _   ||  | |  |  |  __   ||   | |    ___||  __   |"')
		print('"|  |_|  ||  | |  ||  | |  |  | |  \  ||   | |   |___ | |  \  |"')
		print('" \     / |  |_|  ||  | |  |  | |__/  ||   | |    ___|| |__/  |"')
		print('"  |   |  |       ||  |_|  |  |       ||   | |   |___ |       |"')
		print('"  |___|  |_______||_______|  |______/ |___| |_______||______/ "')
		sys.exit()

	if bh<=0:
		print("' ____    ______           _____ _______    _____ _               _____ _   _ '")
 		print("'|  _ \  |  ____|   /\    / ____|__   __|  / ____| |        /\   |_   _| \ | |'")
 		print("'| |_) | | |__     /  \  | (___    | |    | (___ | |       /  \    | | |  \| |'")
 		print("'|  _ <  |  __|   / /\ \  \___ \   | |     \___ \| |      / /\ \   | | | . ` |'")
 		print("'| |_) | | |____ / ____ \ ____) |  | |     ____) | |____ / ____ \ _| |_| |\  |'")
 		print("'|____/  |______/_/    \_\_____/   |_|    |_____/|______/_/    \_\_____|_| \_|'")
		sys.exit()



	
	if firepiller==1 and go<1:
		dy=350
		fx=random.randrange(100,670)
		go=1
	if go > 0:
		go+=1
		if go < r1:
			screen.blit(ex,(fx,500))
		if r1<go<r2:
			screen.blit(doom,(fx,400))
			if posx-70<fx<posx+200:
				print("' __   __  _______  __   __    ______   ___   _______  ______  '")  
				print("'|  | |  ||       ||  | |  |  |      \ |   | |       ||      \ '") 
				print("'|  | |  ||   _   ||  | |  |  |  __   ||   | |    ___||  __   |'")
				print("'|  |_|  ||  | |  ||  | |  |  | |  \  ||   | |   |___ | |  \  |'")
				print("' \     / |  |_|  ||  | |  |  | |__/  ||   | |    ___|| |__/  |'")
				print("'  |   |  |       ||  |_|  |  |       ||   | |   |___ |       |'")
				print("'  |___|  |_______||_______|  |______/ |___| |_______||______/ '")
				sys.exit()
		if go >r2:
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
			if event.key==K_a or event.key==K_LEFT:
				posx=posx-33
			if event.key==K_d or event.key==K_RIGHT:
				posx=posx+33
			if event.key==K_SPACE and bx>700:
				bx=posx
	if dx<bx<dx+125 and dy<400<dy+100:
		bh-=1

		
				


	x+=1
	time.sleep(1/7)
	back=pygame.image.load(str(x)+".png")
	if x==54:
		x=1