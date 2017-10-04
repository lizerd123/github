
save=str(input("Insert Save Code:"))
vit=(save[0:2])
stm=(save[2:4])
strn=(save[4:6])
dex=(save[6:8])
inte=(save[8:10])
fth=(save[10:12])
mge=(save[12:14])
weapon=(save[14:16])
armor=(save[16:18])
lvl=int(vit)+int(stm)+int(strn)+int(dex)+int(inte)+int(fth)+int(mge)-70
top="_______"
line1="####"
line2="####"
line3="####"
line4="####"
vert=4
hor=2
rooms=1
freelvls=0
what_to_do=""
import os
import random
door=random.randint(3,6)
steps_til_event=random.randint(5,10)
rooms_til_boss=random.randint(5,8)

while True:
	for i in range(50):
		print("")
	###########################################
	if steps_til_event<=0:
		used=0
		final_fight=0
		evasion=0
		stamina=int(float(stm)*.5)
		hero_health=10*int(vit)
		if weapon=="01":
			base_damage=10
			stamina_use=3
			wasu=6
			scaling=float(dex)*.4
		if weapon=="02":
			base_damage=17
			stamina_use=5
			wasu=5
			scaling=float(strn)*.8
		if weapon=="03":
			base_damage=8
			stamina_use=2.5
			wasu=6
			scaling=float(dex)*.7
		if weapon=="04":
			base_damage=2
			wasu=3.5
			stamina_use=3
			magic_scaling=1.1*float(inte)
		if weapon=="05":
			base_damage=1
			wasu=2
			stamina_use=3
			magic_scaling=1.2*float(faith)
		if weapon=="06":
			base_damage=20
			stamina_use=6
			wasu=7
			scaling=float(strn)*.9
		enemy_health=100+lvl
		enemy_attack=10+.2*lvl
		while enemy_health>0 and hero_health>0:
			while stamina>0 and enemy_health>0:
				print("my heath: "+str(hero_health))
				print("enemy health: "+str(enemy_health))
				print("my stamina: "+str(stamina))
				print("I Can attack, use my weapon talent or try and dodge")
				action=raw_input("What shouls I do?")
				if action =="attack" and stamina>=stamina_use:
					enemy_health-=base_damage+scaling
					stamina-=int(stamina_use)

				if action =="attack" and stamina<stamina_use:
					print("Not enough stamina")

				if action=="weapon talent":
					if weapon=="01" and stamina>=wasu:
						print("You chant a gentle prayer and regain health")
						hero_health+=20
						stamina-=wasu

					if weapon=="02" and stamina>=wasu:
						print("You let out a warcry and increase your attack")
						scaling+=.25
						stamina-=wasu

					if weapon=="03" and stamina>=wasu:
						print("You unleash a precise attack that hits the enemie's weak point")
						enemy_health-=20
						stamina-=wasu

					if weapon=="04" and stamina>=wasu:
						print("You fire a magic orb that hits the enemy")
						enemy_health-=magic_scaling
						stamina-=wasu

					if weapon=="05" and stamina>=wasu:
						print("You fire a small bolt of lightning that hits the enemy")
						enemy_health-=magic_scaling
						stamina-=wasu

					if weapon=="06" and stamina>=wasu and used==0:
						print("You steel your nerves and prepare for a powerful attack")
						final_fight=1
						stamina-=wasu
						used=1

				if action =="weapon talent" and stamina<wasu:
					print("Not enough stamina")
				if action=="dodge":
					evasion=3
					stamina=0
			hero_health-=enemy_attack-evasion
			stamina=int(float(stm)*.5)
			if hero_health<0:
				print("YOU WERE SLAIN")
				quit()

		freelvls+=1
		steps_til_event=random.randint(5,10)
	if rooms_til_boss<=0:
		what_to_do=""
		while what_to_do!= "continue":
			
			print("you arrive in a room where you can level up. You can generate your save code in this room. You may continue, but you feel a strong presence behind the next door")
			
			what_to_do=raw_input("What to do...")
			if what_to_do=="save":
				print(str(vit)+str(stm)+str(strn)+str(dex)+str(inte)+str(fth)+str(mge)+str(weapon)+str(armor)+"00")

			if what_to_do=="level up":
				while int(freelvls)>=1:
					print("allocate stats")
					print("Unallocated levels: "+ str(int(freelvls)))
					print("level: "+ str(lvl))
					print("1 Vitality:"+str(vit))
					print("2 Stamina:"+str(stm))
					print("3 Strength:"+str(strn))
					print("4 Dexterity:"+str(dex))
					print("5 Intelegence:"+str(inte))
					print("6 Faith:"+str(fth))
					print("7 Magicality:"+str(mge))
					stattochange=input("Stat: ")
					levels=input("Level how much: ")
					if levels>freelvls:
						print("Insufficient Unallocated levels")
					if levels<0:
						print("Unable to remove levels")
					if levels<=freelvls:
						if stattochange==1:
							vit=int(vit)+levels
						if stattochange==2:
							stm=int(stm)+levels
						if stattochange==3:
							strn=int(strn)+levels
						if stattochange==4:
							dex=int(dex)+levels
						if stattochange==5:
							inte=int(inte)+levels
						if stattochange==6:
							fth=int(fth)+levels
						if stattochange==7:
							mge=int(mge)+levels
						lvl+=levels
						freelvls-=levels
		print("You encounter A large creature seemingly of pure iron, it wields a large metal club")
		evasion=0
		stamina=int(float(stm)*.5)
		hero_health=10*int(vit)
		if weapon=="01":
			base_damage=10
			stamina_use=3
			wasu=6
			scaling=float(dex)*.4
		if weapon=="02":
			base_damage=17
			stamina_use=5
			wasu=5
			scaling=float(strn)*.8
		if weapon=="03":
			base_damage=8
			stamina_use=2.5
			wasu=6
			scaling=float(dex)*.7
		if weapon=="04":
			base_damage=2
			wasu=3.5
			stamina_use=3
			magic_scaling=1.1*float(inte)
		if weapon=="05":
			base_damage=1
			wasu=2
			stamina_use=3
			magic_scaling=1.2*float(faith)
		enemy_health=100*rooms*.5
		enemy_attack=16*.2*rooms
		while enemy_health>0 and hero_health>0:
			while stamina>0 and enemy_health>0:
				print("my heath: "+str(hero_health))
				print("enemy health: "+str(enemy_health))
				print("my stamina: "+str(stamina))
				print("I Can attack, use my weapon talent or try and dodge")
				action=raw_input("What shouls I do?")
				if action =="attack" and stamina>=stamina_use:
					enemy_health-=base_damage+scaling
					stamina-=int(stamina_use)

				if action =="attack" and stamina<stamina_use:
					print("Not enough stamina")

				if action=="weapon talent":
					if weapon=="01" and stamina>=wasu:
						print("You chant a gentle prayer and regain health")
						hero_health+=20
						stamina-=wasu

					if weapon=="02" and stamina>=wasu:
						print("You let out a warcry and increase your attack")
						scaling+=.25
						stamina-=wasu

					if weapon=="03" and stamina>=wasu:
						print("You unleash a precise attack that hits the enemie's weak point")
						enemy_health-=20
						stamina-=wasu

					if weapon=="04" and stamina>=wasu:
						print("You fire a magic orb that hits the enemy")
						enemy_health-=magic_scaling
						stamina-=wasu

					if weapon=="05" and stamina>=wasu:
						print("You fire a small bolt of lightning that hits the enemy")
						enemy_health-=magic_scaling
						stamina-=wasu

					if weapon=="06" and stamina>=wasu and used==0:
						print("You steel your nerves and prepare for a powerful attack")
						final_fight=1
						stamina-=wasu
						used=1

				if action =="weapon talent" and stamina<wasu:
					print("Not enough stamina")
				if action=="dodge":
					evasion=3
					stamina=0
			if enemy_health>0:
				hero_health-=enemy_attack-evasion
			stamina=int(float(stm)*.5)
			if hero_health<0:
				print("YOU WERE SLAIN")
				quit()
		freelvls+=10
		rooms_til_boss=random.randint(5,8)
		take_club=raw_input("the giant dissapears but leaves behind the club, will you take it?")
		if take_club=="yes":
			weapon="06"

	###########################################
	
	print((top[1:door-1]+"#"+top[door:7]))

	if vert==1:
		print("|"+(line1[0:hor-1]+"x"+line1[hor:4])+"|")
	else:
		print("|"+line1+"|")
	if vert==2:
		print("|"+(line2[0:hor-1]+"x"+line2[hor:4])+"|")
	else:
		print("|"+line2+"|")
	if vert==3:
		print("|"+(line3[0:hor-1]+"x"+line3[hor:4])+"|")
	else:
		print("|"+line3+"|")
	if vert==4:
		print("|"+(line4[0:hor-1]+"x"+line4[hor:4])+"|")
	else:
		print("|"+line4+"|")
	print("______")
	direction=raw_input("Direction?")
	
	if direction=="down"and vert!=4:
		vert+=1
		steps_til_event-=1
	if direction=="right"and hor!=4:
		hor+=1
		steps_til_event-=1
	if direction=="left"and hor!=1:
		hor-=1
		steps_til_event-=1
	if direction=="up" and hor==door-2 and vert==1:
		print("Next room")
		door=random.randint(3,6)
		hor=random.randint(1,4)

		vert=5
		rooms+=1
		steps_til_event-=1
		rooms_til_boss-=1
	if direction=="up" and vert!=1:
		vert-=1
		steps_til_event-=1
