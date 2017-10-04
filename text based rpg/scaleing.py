###################### LEVELING #####################
lvl=0
strn=10
vit=10
dex=10
inte=10
fth=10
stm=10
mge=10
lvl=0
levels=0
freelvls=30
stattochange=0
while freelvls>0:
	print("allocate stats")
	print("Unallocated levels: "+ str(freelvls))
	print("level: "+ str(lvl))
	print("1 Vitality:"+str(vit))
	print("2 Stamina:"+str(stm))
	print("3 Strength:"+str(strn))
	print("4 Dexterity:"+str(dex))
	print("5 Intelegence:"+str(inte))
	print("6 Faith:"+str(fth))
	print("7 Magicality:"+str(mge))
	try:
		stattochange=int(input("Stat: "))
	except:
		print("Please use a vaild number")

	if stattochange>7 or stattochange<=0:
		print("not a stat")

	if 0<stattochange<=7:
		try:
			levels=int(input("Level how much: "))
		except:
			print("Please use a vaild number")
		if levels>freelvls:
			print("Insufficient Unallocated levels")
		if levels<0:
			print("Unable to remove levels")
		if 0<levels<=freelvls:
			if stattochange==1:
				vit+=levels
			if stattochange==2:
				stm+=levels
			if stattochange==3:
				strn+=levels
			if stattochange==4:
				dex+=levels
			if stattochange==5:
				inte+=levels
			if stattochange==6:
				fth+=levels
			if stattochange==7:
				mge+=levels
			lvl+=levels
			freelvls-=levels
###################### WEAPONS #####################
weapon=0
print("(1) Knight Sword (2) Axe (3) Fencing sword (4) Staff (5) Chime")
while weapon==0:
	beginning_weapon=input("Begining weapon: ")
	weapon="0"+str(beginning_weapon)

###################### armor #####################
armor=00




print(str(vit)+str(stm)+str(strn)+str(dex)+str(inte)+str(fth)+str(mge)+str(weapon)+str(armor)+"00")




































