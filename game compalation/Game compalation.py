print("play (1) motorman (2) Dungeon")
game_chosen=input("what to play... ")
if game_chosen==1:
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
		r1=11
		r2=27
	if difficulty==3 and go<1:
		bh=random.randrange(30,40)
		r1=10
		r2=25
	if difficulty==4 and go<1:
		bh=random.randrange(40,50)
		r1=10
		r2=23
	ticks=900/bh
	go=0
	print(bh)
	screen=pygame.display.set_mode((900,700))
	x=0
	back=pygame.image.load("1.png")





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
					posx=posx-40
				if event.key==K_d or event.key==K_RIGHT:
					posx=posx+40
				if event.key==K_SPACE and bx>700:
					bx=posx
		if dx<bx<dx+125 and dy<400<dy+100:
			bh-=1

			
					


		x+=1
		time.sleep(1/7)
		back=pygame.image.load(str(x)+".png")
		if x==54:
			x=1
if game_chosen==2:
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
						ground=pygame.image.load(str(x)+"b.png")
						enemies=1
						screen.blit(ground,(0,0))
						begin=1
						mx=random.randint(0,100) or random.randint(400,500)
						my=random.randint(0,100) or random.randint(400,500)

























