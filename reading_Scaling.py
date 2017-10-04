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
location=(save[18:20])
input random
hero_health=100*.01*vit+100
while location=="00":
	print("you awaken in a room of stone with only one exit:")
	print(" I can only move forward")
	direction=raw_input("what direction ")
	if direction=="forward":
		location=01
	else:
		print("I cant do that")
		print("")
times_through=1
while times_through<=5
	to_rest=random.randint(3,7)
	
	while to_rest>0:
		################
		if weapon="01":
			damage=17+5*.01*strn+5+5*.01*dex+5
		if weapon="02":
			damage=20
		if weapon="03":
		if weapon="04":
		if weapon="05":	






		################
		event=random.randint(1,10)
		if event>4:
			print ("nothing here")
		if 9<=event<=4:
			print("attacked by an enemy")
			enemy_health=100*.1*times_through+100
			enemy_attack=10*.1*times_through+10
			while enemy_health>0 and hero_health>0:
				print("")
				action=input("what to do...")

		if event=10:
			print("found chest")
