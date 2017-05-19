from turtle import *
import random

##############


def drawline():
	right(90)
	forward(65)
	right(90)
	forward(650)
	left(90)
	forward(65)
	left(90)
	forward(650)

def enemy():
	penup()
	goto(enx*65,eny*65)
	forward(5)
	pendown()
	right(90)
	forward(5)
	right(90)
	forward(10)
	right(90)
	forward(10)
	right(90)
	forward(10)
	right(90)
	forward(5)
	penup()
	goto(0,-65)
	goto(0,0)

def square():
	penup()
	goto(325,325)
	pendown()
	goto(325,-325)
	goto(-325,-325)
	goto(-325,325)
	goto(325,325)

def fight():
	#health of the slime
	health_s = 100
	#health of you
	health= 100
	level = random.randrange(1,11)
	print ('slime level')
	print(level)
	move = False
	choise = ""
	n = 0
	inv = "Health Potion", "Health Potion"
	moveset = ["Attack", "Use an item", "Show health", "Counter"]
	while health > 0 and health_s > 0:
	    move = False
	    n += 1
	    print("")
	    print("------------------Turn "+str(n) + "------------------")
	    while move == False:
	        print ("")
	        print ("I can: " + moveset[0] +", " + moveset[1] + ", " + moveset[2] +" or " + moveset[3])
	        print ("")
	        print("What do I do?")
	        choise = str(raw_input())
	        print("")
	        if choise == "Attack" or "attack":
	            chance = random.randrange(0,10)
	            if chance <= 2:
	                print("You miss")
	                move = True
	            elif chance <=8:
	                print("solid hit")
	                health_s -= random.randrange(10,15)
	                move = True
	            else:
	                print("Critical Hit!")
	                health_s -= random.randrange(20,30)
	                move = True
	        elif choise == "Use an item" and inv != []:
	            print("I have ", inv, "in my inventory")
	            print("What do I use")
	            choise = input()
	            if choise in inv:
	                if choise == "Health Potion":
	                    health += 30
	            else:
	                print("sorry I dont have that Item")
	            
	        elif choise == "Counter":
	            print('Took a defencive stance')
	            move = True
	            
	        elif choise == "Show_health":
	            print ("Me", health)
	            print ("Enemy", health_s)
	        
	    
	        
	    chance = random.randrange(0,10)
	    if chance <= 4:
	        print("The Slime missed")
	    elif chance <=9:
	        print("Slime hit")
	        attack = random.randrange(10,15)
	        health -= attack*(0.1*level+1)
	    else:
	        print("Slime did a Critical Hit!")
	        health -= random.randrange(20,30)*(0.1*level+1)
	    
	    if choise == "Counter" and chance <=4:
	        print ("the counter failed and you fell on your face")
	        health -= random.randrange(10,20)
	    if choise == "Counter" and chance >=5:
	        print ("the slime hit but you hit it harder")
	        health_s -= attack*1.5
	    
	    print ("I now have:", health)
	    print ("The slime now has:", health_s)                
	if health < 0:
	    print('I am now dead')
	else:
	    print("I Won!")
	
###############


speed('fastest')
square()


for i in range (2):	
	for i in range (5):
		drawline()
	left(270)



enx=random.randrange(-5, 5)
eny=random.randrange(-5, 5)
enemy()
	


posx=0
posy=0
while eny!=posy or enx!=posx:
	x=raw_input("what direction?")
	if x == "up":
		if posy == 5:
			print "cant go that way"
		if posy !=5:
			forward(65)
			posy=posy+1
	if x == "right":
		if posx==5:
			print "cant go that way"
		if posx!=5:
			right(90)
			forward(65)
			left(90)
			posx=posx+1
	if x == "left":
		if posx==-5:
			print "cant go that way"
		if posx!=-5:
			left(90)
			forward(65)
			right(90)
			posx=posx-1
	if x == "down":
		if posy == -5:
			print "cant go that way"
		if posy !=-5:
			back(65)
			posy=posy-1

fight()



listen()

mainloop()