
import sys, pygame, pygame.mixer
from pygame.locals import *
import random
x1=400
y1=400
distance=0
jumping=0
time=0000000000.1
x2=400
y2=400
distance2=0
jumping2=0
time2=0000000000.1
speed=distance/time
velocity=speed/time
speed2=distance2/time2
velocity2=speed2/time2
hero=pygame.image.load("hero.png")
hero2=pygame.image.load("hero.png")
beck=pygame.image.load("yo.png")
screen=pygame.display.set_mode((900,700))
pygame.key.set_repeat(25,25)


	
while True:
	screen.blit(beck,(0,0))		
	screen.blit(hero2,(x2,y2))
	if jumping2==1 and y2>200:
		y2-=10
	if y2==200:
		jumping2=0
	if jumping2==0 and y2<400:
		y2+=10
	if y2<400:
		friction2=1
	else:
		friction2=1.08
	if  x2<860 and x2>40:
		print
	else:
		y2+=10
		if y2>400:
			y2+=10
	if y2>700:
		print("you fell")
		sys.exit()
	velocity2/=friction2
	if distance2==0:
		time2=00000000.1
	x2+=velocity2
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == K_j:
				distance=-10
				time=1
				speed=distance/time
				velocity=speed/time

			if event.key == K_l:
				distance=10
				time=1
				speed=distance/time
				velocity=speed/time
			if event.key == K_i and y1==400:
				jumping=1
		if event.type == pygame.KEYDOWN:
			if event.key == K_a:
				distance2=-10
				time2=1
				speed2=distance2/time2
				velocity2=speed2/time2

			if event.key == K_d:
				distance2=10
				time2=1
				speed2=distance2/time2
				velocity2=speed2/time2
			if event.key == K_w and y2==400:
				jumping2=1


	screen.blit(hero,(x1,y1))
	
	if jumping==1 and y1>200:
		y1-=10
	if y1==200:
		jumping=0
	if jumping==0 and y1<400:
		y1+=10
	if y1<400:
		friction=1
	else:
		friction=1.08
	if  x1<860 and x1>40:
		print
	else:
		y1+=10
		if y1>400:
			y1+=10
	if y1>700:
		print("you fell")
		sys.exit()
	velocity/=friction
	if distance==0:
		time=00000000.1
	x1+=velocity
	pygame.display.flip()
	
		
	
	