from pygame.locals import *

screen=pygame.display.set_mode((900,470))
pos_cup={'x':0,'y':0}
vel_cup={'x':10,'y':10}
gravity=-3
fricion=0.01
while True:
	if pos_cup.y==0:
		vel.y=0
		vel.x*=fricion