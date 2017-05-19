import sys, pygame, pygame.mixer
from pygame.locals import *
pygame.init()
import time
x=5
y=300
yvol = 0
xvol = 0


MEMES =pygame.display.set_mode((900,470))
person = pygame.image.load("jack.png")
back=pygame.image.load("town.png")
screen = MEMES
pygame.key.set_repeat(25,25)
pygame.display.set_caption('memes')

white=(225,225,225)
screen.blit(back,(0,0))

while True:
    
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == KEYDOWN:
                    if event.key==K_ESCAPE:
                            sys.exit()
                    
                    if event.key==K_LEFT:
            			x=x-10
            			screen.blit(back,(0,0))
						
			
                            
                    if event.key==K_RIGHT:
						x=x+10
						screen.blit(back,(0,0))

                    if event.key==K_UP and yvol<0:
                        yvol = 15
        y -= yvol
        x -= xvol
        if yvol <= 25 and yvol > -50:
            yvol -= 1
        if y > 300:
            y = 300
            if xvol > 0:
                xvol -= 1
        if x>700:
        	back=pygame.image.load("meem.png")
        	x=5
        
 
                    
                
	screen.blit(back,(0,0))
	screen.blit(person,(x,y))
	
	pygame.display.update()
