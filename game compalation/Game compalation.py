game_chosen=0
begin_game=0
running=0
while True:
	while begin_game!=1:
			print("play (1) motorman(one player) (2) Dungeon(one player) (3) Shop'n'Stab(one player) (4)Duel(two player)")
			game_chosen=input("what to play... ")
			if game_chosen==1 or 2:
				begin_game=1
				running=1
				
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





			while running==1:
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
					running=0

				if bh<=0:
					print("' ____    ______           _____ _______    _____ _               _____ _   _ '")
					print("'|  _ \  |  ____|   /\    / ____|__   __|  / ____| |        /\   |_   _| \ | |'")
					print("'| |_) | | |__     /  \  | (___    | |    | (___ | |       /  \    | | |  \| |'")
					print("'|  _ <  |  __|   / /\ \  \___ \   | |     \___ \| |      / /\ \   | | | . ` |'")
					print("'| |_) | | |____ / ____ \ ____) |  | |     ____) | |____ / ____ \ _| |_| |\  |'")
					print("'|____/  |______/_/    \_\_____/   |_|    |_____/|______/_/    \_\_____|_| \_|'")
					running=0



				
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
							running=0
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
			if running==0:
				pygame.display.quit()
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
			while running==1:
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
						mx+=coinneeded/20
					if hx-mx<0:
						mx-=coinneeded/20
					if hy-my>0:
						my+=coinneeded/20
					if hy-my<0:
						my-=coinneeded/20
					if my<hy<my+75 and mx<hx<mx+50:
						print("you died at level " + str(level))
						running=0


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
						if event.key==K_SPACE and fire==0 and enemies>0:
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
			if running==0:
				pygame.display.quit()
	if game_chosen==3:
			from random import randint as ri
			inv=[]
			st=1
			sa=0
			money=120
			weapon="your an idiot"
			item="your an idiot"
			magic="your an idiot"
			print (money)
			print ("I better get some weapons items and magic")
			Inventory_Blacksmith=["wooden sword","Axe","longsword","knife","hammer","torch"]
			r = ri(0,5)
			print (Inventory_Blacksmith[r:r+3])



			buy = raw_input("what to buy?")
			if buy == "wooden sword":
				inv.append("wooden sword")
				money=money-25
				weapon="wooden sword"
			if buy == "Axe":
				inv.append("Axe")
				money=money-60
				weapon="Axe"
			if buy == "longsword":
				inv.append("longsword")
				money=money-60
				weapon="longsword"
			if buy == "knife":
				inv.append("knife")
				money=money-30
				weapon="knife"
			if buy == "hammer":
				inv.append("hammer")
				money=money-60
				weapon="hammer"
			if buy == "torch":
				inv.append("torch")
				money=money-30
				weapon="torch"
			if len(inv) < 1:
				inv.append("FOOL")
			print(money)
			print(inv)

			 
			Inventory_Shopkeep=["Potion","attack potion","defence potion"]
			print (Inventory_Shopkeep)
			buy = raw_input("what to buy?")
			if buy == "firebomb":
				inv.append("firebomb")
				money=money-30
				item="firebomb"
			if buy == "Potion":
				inv.append("Potion")
				money=money-30
				item="Potion"
			if buy == "attack potion":
				inv.append("attack potion")
				money=money-30
				item="attack potion"
			if buy == "defence potion":
				inv.append("defence potion")
				money=money-30
				item="defence potion"
			if len(inv) < 2:
				inv.append("FOOL")    
			print(money)
			print(inv)



			Inventory_wizard=["energy","magic weapon","heal","stoneflesh"
			]
			r = ri(0,5)
			print (Inventory_wizard[r:r+3])
			buy = raw_input("what to buy?")
			if buy == "energy":
				magic="energy"
				inv.append("energy")
				money=money-25
			if buy == "magic weapon":
				inv.append("magic weapon")
				money=money-30
				magic="magic weapon"
			if buy == "heal":
				inv.append("heal")
				money=money-60
				magic="heal"
			if buy == "stoneflesh":
				inv.append("stoneflesh")
				money=money-60
				magic="stoneflesh"
			if buy == "thorns":
				inv.append("thorns")
				money=money-30
				magic="thorns"
			if len(inv) < 3:
				inv.append("FOOL")
			print(inv)
			from random import randint as ri
			mg=0
			eh = ri(150, 280)
			mh = 200
			de=1
			if weapon == "Axe":
				st = 1.8
			if weapon == "longsword":
				st = 1.6
			if weapon == "knife":
				st = 1.1
			if weapon == "hammer":
				st = 1.7
			if weapon == "wooden sword":
				st = 1
			if weapon == "torch":
				st = 1.4
			if item == "potion":
				mh=mh+30
			if item == "potion":
				mh=mh+30
			if item == "attack potion":
				st=st+.6
			if item == "defence potion":
				de=de+.4
			if magic == "energy":
				mg=5
			if magic == "magic weapon":
				st=st+.6
			if magic == "heal":
				mh=mh+30
			if magic == "magic weapon":
				st=st+.6
			if magic == "stoneflesh":
				de=de+.2
			if magic == "thorns":
				cd=.5
				

				
			while eh>0 and mh>0:
					counter = 0
					ed=ri(9,30)
					print (" I can attack counter or use skill")
					if sa < 40:
					  print ("I am too tired to use a skill")
					move = raw_input("move ")
					if move == "attack":
						at=ri(9,15)
						eh=eh-st*at+mg
						print ("enemy")
						print (eh)
						print ("the attack was successful")
					if move == ("inventory"):
					  print ("I have") (inv)
					if move == ("skill") and sa > 40:
					  if weapon == "Axe":
						eh = eh-st*2*at+mg
						mh = mh-20
						sa=0
						print("the attack was powerful but left your wrist injujred")
					  if weapon == "longsword":
						 ed = 0
						 sa=0
						 print("You were too far for the enemy to attack")
					  if weapon == "knife":
						slash = ri(1,5)
						if slash == 1:
						  eh = eh-40
						  sa=0
						  print("you slash at the enemy dealing heavy dammage")
						else:
						  print("you miss the enemy")
					  if weapon == "hammer":
						de = + .5
						sa=0
						print("you feel far more fortified")
					  if weapon == "wooden sword":
						st = st-.75
						mh = mh + .1*mh
						sa=0
						print("somehow snaping your flimsy sword makes you feel better")
					  if weapon == "torch":
						mg = 10
						sa=0
						print("you light the enemy ablaze")
					if move == "counter":
						counter = 1
					ea = ri(0,4)
					if ea > 0:
						mh=mh-ed/de
						print ("me")
						print (mh)
						if counter == 1:
							eh=eh-st*ed*1.25+mg
							print ("enemy")
							print (eh)
					if ea == 0:
						if counter ==1:
							print("the counter fails")
							mh=mh-ri(10,20)
							print(mh)
					print ("enemy")
					print (eh)
					sa = sa +10	
	if game_chosen==4:
		p1h=5
		p2h=5
		p1p=4
		p2p=2
		moves1=3
		moves2=3
		space=1
		p1w=raw_input("P1 Weapon: ")
		if p1w == "axe":
		  p1min=-1
		  p1max=1
		if p1w == "longsword":
		  p1min=0
		  p1max=2
		if p1w == "spear":
		  p1min=1
		  p1max=3
		p2w=raw_input("P2 Weapon: ")
		if p2w == "axe":
		  p2min=-1
		  p2max=1
		if p2w == "longsword":
		  p2min=0
		  p2max=2
		if p2w == "spear":
		  p2min=1
		  p2max=3
		while p1h>=0 or p2h>=0:

		  moves1=3
		  moves2=3
		  while moves1>0:
		    if p2p==1:
		      if p1p==2:
		        print("X O_ _ _")
		      if p1p==3:
		        print("X _ O _ _")
		      if p1p==4:
		        print("X _ _ O _")
		      if p1p==5:
		        print("X _ _ _ O")
		    if p2p==2:
		      if p1p==3:
		        print("_ X O _ _")
		      if p1p==4:
		        print("_ X _ O _")
		      if p1p==5:
		        print("_ X _ _ O")
		    if p2p==3:
		      if p1p==4:
		        print("_ _ X O _")
		      if p1p==5:
		        print("_ _ X _ O")
		    if p2p==4:
		      if p1p==5:
		        print("_ _ _ X O")
		      
		    print ("moves:"+ str(moves1))
		    print("health1:"+str(p1h ))
		    action1=raw_input("action P1")
		    if action1 == "back":
		      if p1p == 5:
		        print("my back is against the wall")
		      if p1p<5:
		        moves1=moves1-1
		        p1p=p1p+1
		        space=space+1
		    if action1 == "forwards":
		      if space == 0:
		        print("cant move past the enemy")
		      if space>0:
		        space=space-1
		        p1p=p1p-1
		        print("I moved forwards")
		        moves1=moves1-1
		    if action1 == "attack":
		      if space>p1min and space<p1max:
		        p2h=p2h-1
		        moves1=moves1-1
		        print("Hit")
		      if space<=p1min or space>=p1max:
		        print("out of my range")
		    if action1 == "shove":
		      if space==0:
		        moves1=moves1-1
		        print("I shoved him back")
		        p2p=p2p-1
		        space=space+1
		  while moves2>0:
		  	if p2h>0:
			    if p2p==1:
			      if p1p==2:
			        print("X O_ _ _")
			      if p1p==3:
			        print("X _ O _ _")
			      if p1p==4:
			        print("X _ _ O _")
			      if p1p==5:
			        print("X _ _ _ O")
			    if p2p==2:
			      if p1p==3:
			        print("_ X O _ _")
			      if p1p==4:
			        print("_ X _ O _")
			      if p1p==5:
			        print("_ X _ _ O")
			    if p2p==3:
			      if p1p==4:
			        print("_ _ X O _")
			      if p1p==5:
			        print("_ _ X _ O")
			    if p2p==4:
			      if p1p==5:
			        print("_ _ _ X O")
			    print ("moves:"+ str(moves2))
			    print("health2:"+str(p2h) )
			    action2=raw_input("action P2")
			    if action2 == "back":
			      if p2p == 1:
			        print("my back is against the wall")
			      if p1p>1:
			        moves2=moves2-1
			        p2p=p2p-1
			        space=space+1
			    if action2 == "forwards":
			      if space == 0:
			        print("cant move past the enemy")
			      if space>0:
			        space=space-1
			        p2p=p2p+1
			        print("I moved forwards")
			        moves2=moves2-1
			    if action2 == "attack":
			      if space>p2min and space<p2max:
			        p1h=p1h-1
			        moves2=moves2-1
			        print("Hit")
			      if space<=p2min or space>=p2max:
			        print("out of my range")
			    if action2 == "shove":
			      if space==0:
			        moves2=moves2-1
			        print("I shoved him back")
			        p1p=p1p+1
			        space=space+1	 
	begin_game=0
