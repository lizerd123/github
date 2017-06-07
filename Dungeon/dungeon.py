import sys, pygame, pygame.mixer
from pygame.locals import *
import random
import time
ground=pygame.image.load("begin.png")
grave=pygame.image.load("grave.png")
hero=pygame.image.load("hero.png")
menu=pygame.image.load("menuNEXT.png")
monster=pygame.image.load("monster.png")
knife=pygame.image.load("knifew.png")
ones=pygame.image.load("1n.png")
tens=pygame.image.load("0n.png")
pygame.init()
hx=225
hy=100
fire=0
di=1
men=0
coinneeded=10
enemies=0
level=1
begin=0
r=1
coin=0
mx=300
my=300
screen=pygame.display.set_mode((500,500))
pygame.key.set_repeat(25,25)
while True:
	ten=int(level/10)

	
	pygame.display.flip()
	screen.blit(ground,(0,0))
	tens=pygame.image.load(str(ten)+"n.png")
	one=level-(ten*10+1)
	ones=pygame.image.load(str(one)+"n.png")
	screen.blit(ones,(110,0))
	screen.blit(tens,(0,0))
	
	if begin==1 and enemies>=0:
		screen.blit(monster,(mx,my))
		if hx-mx>0:
			mx+=coinneeded/10
		if hx-mx<0:
			mx-=coinneeded/10
		if hy-my>0:
			my+=coinneeded/10
		if hy-my<0:
			my-=coinneeded/10
		if my<hy<my+75 and mx<hx<mx+50:
			print("you died at level " + str(level))
			sys.exit()


	if fire==1:
		if di==1:
			ky-=25
		if di==2:
			kx-=25
		if di==3:
			ky+=25
		if di==4:
			kx+=25
		if mx-10<kx<mx+50 and my-10<ky<my+75:
			coin+=10
			print("coins:" + str(coin))
			mx=8000
			my=8000
			enemies-=1
		screen.blit(knife,(kx,ky))
		if kx<0 or kx>500 or ky<0 or ky>500:
			fire=0
	if enemies <=0:
		screen.blit(grave,(225,225))
	screen.blit(hero,(hx,hy))
	if men==1 and enemies<=0:
		screen.blit(menu,(0,400))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == KEYDOWN:
			if event.key==K_a:
				knife=pygame.image.load("knifea.png")
				hx-=25
				if fire!=1:
					di=2
			if event.key==K_f:
				enemies-=1
			if event.key==K_d:
				knife=pygame.image.load("knifed.png")
				hx+=25
				if fire!=1:
					di=4
			if event.key==K_w:
				knife=pygame.image.load("knifew.png")
				hy-=25
				if fire!=1:
					di=1
			if event.key==K_s:
				knife=pygame.image.load("knifes.png")
				hy+=25
				if fire!=1:
					di=3
			if event.key==K_LEFT:
				menu=pygame.image.load("menuNEXT.png")
				r=1
			if event.key==K_RIGHT:
				menu=pygame.image.load("menuUP.png")
				r=0
			if event.key==K_SPACE and fire==0:
				kx=hx
				ky=hy
				screen.blit(knife,(kx,ky))
				fire=1
			if enemies <=0:
				if hx==225 and hy==225 and event.key==K_SPACE:
					men=1
				if hx!=225 or hy!=225:
					men=0
				if men==1 and event.key==K_RETURN and r==0 and coin>=coinneeded:
					
					level+=1
					print("current level:" + str(level))
					coin-=coinneeded
					coinneeded+=10
					print("untill next level:" + str(coinneeded))
					print("coins:" + str(coin))
				if men==1 and event.key==K_RETURN and r==1:
					x=random.randint(1,5)
					ground=pygame.image.load(str(x)+".png")
					enemies=1
					screen.blit(ground,(0,0))
					begin=1
					mx=random.randint(0,100) or random.randint(400,500)
					my=random.randint(0,100) or random.randint(400,500)

























