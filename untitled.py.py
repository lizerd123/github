from turtle import *


##############
def go_f():
	forward(10)
def go_b():
	backward(10)
def go_l():
	left(10)
def go_r():
	right(10)
def go_s():
	draw_square()
	
###############

onkey(go_f, "Up")
onkey(go_b, "Down")
onkey(go_l, "Left")
onkey(go_r, "Right")
onkey(go_s, " ")

def draw_square():
	for i in range(36):
		forward(100)
		right(90)
		forward(100)
		right(90)
		forward(100)
		right(90)
		forward(100)
		right(100)
    	
    	i =i+1
	


listen()

mainloop()