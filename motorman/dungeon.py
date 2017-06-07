import sys, pygame, pygame.mixer
from pygame.locals import *
import random
import time
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.key.set_repeat(25,25)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
