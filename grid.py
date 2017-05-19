from turtle import *


##############

	
###############


penup()
goto(325,325)
pendown()
goto(325,-325)
goto(-325,-325)
goto(-325,325)
goto(325,325)
for i in range(5):
	right(90)
	forward(65)
	right(90)
	forward(650)
	left(90)
	forward(65)
	left(90)
	forward(650)
right(180)

for i in range(5):
	forward(65)
	right(90)
	forward(650)
	left(90)
	forward(65)
	left(90)
	forward(650)
	right(90)
penup()
goto(0,0)
right(90)
posx=0
posy=0
while True:
	listen()
	x=0
	def go_f():
		x="up"
	def go_b():
		x="down"
	def go_l():
		x="left"
	def go_r():
		x="right"
	onkey(go_f, "Up")
	onkey(go_b, "Down")
	onkey(go_l, "Left")
	onkey(go_r, "Right")	
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





	




mainloop()