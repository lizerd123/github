import sys, pygame, pygame.mixer
from pygame.locals import *
pygame.init()
import time
pygame.key.set_repeat(25,25)
person = pygame.image.load("motorman.png")
posx=50
posy=240
screen=pygame.display.set_mode((900,700))
x=0
back=pygame.image.load("1.png")
while True:
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
	if x==13:
		back=pygame.image.load("13.png")
	if x==14:
		back=pygame.image.load("14.png")
	if x==15:
		back=pygame.image.load("15.png")
	if x==16:
		back=pygame.image.load("16.png")
	if x==17:
		back=pygame.image.load("17.png")
	if x==18:
		back=pygame.image.load("18.png")
	if x==19:
		back=pygame.image.load("19.png")
	if x==20:
		back=pygame.image.load("20.png")
	if x==21:
		back=pygame.image.load("21.png")
	if x==22:
		back=pygame.image.load("22.png")
	if x==23:
		back=pygame.image.load("23.png")
	if x==24:
		back=pygame.image.load("24.png")
	if x==25:
		back=pygame.image.load("25.png")
	if x==26:
		back=pygame.image.load("26.png")
	if x==27:
		back=pygame.image.load("27.png")
	if x==28:
		back=pygame.image.load("28.png")
	if x==29:
		back=pygame.image.load("29.png")
	if x==30:
		back=pygame.image.load("30.png")
	if x==31:
		back=pygame.image.load("31.png")
	if x==32:
		back=pygame.image.load("32.png")
	if x==33:
		back=pygame.image.load("33.png")
	if x==34:
		back=pygame.image.load("34.png")
	if x==35:
		back=pygame.image.load("35.png")
	if x==36:
		back=pygame.image.load("36.png")
	if x==37:
		back=pygame.image.load("37.png")
	if x==38:
		back=pygame.image.load("38.png")
	if x==39:
		back=pygame.image.load("39.png")
	if x==40:
		back=pygame.image.load("40.png")
	if x==41:
		back=pygame.image.load("41.png")
	if x==42:
		back=pygame.image.load("42.png")
	if x==43:
		back=pygame.image.load("43.png")
	if x==44:
		back=pygame.image.load("44.png")
	if x==45:
		back=pygame.image.load("45.png")
	if x==46:
		back=pygame.image.load("46.png")
	if x==47:
		back=pygame.image.load("47.png")
	if x==48:
		back=pygame.image.load("48.png")
	if x==49:
		back=pygame.image.load("49.png")
	if x==50:
		back=pygame.image.load("50.png")
	if x==51:
		back=pygame.image.load("51.png")
	if x==52:
		back=pygame.image.load("52.png")
	if x==53:
		back=pygame.image.load("53.png")
	if x==54:
		back=pygame.image.load("54.png")
		x=1
