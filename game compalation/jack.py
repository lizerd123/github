# A map GUI thing
# +---------+
# |####|****|
# |####|****|
# |####|****|
# |----+----|
# |::::|$$$$|
# |::::|$$$$|
# |::::|$$$$|
# +---------+

print "+-----------+"
print "| U = Up    |"
print "| D = Down  |"
print "| R = Right |"
print "| L = Left  |"
print "| Q = Quit  |"
print "+-----------+"

mainmap = []
coords = [6,5]

# these are for making map
def genMap(inarray):
	for i in range(3):
		makeLine(inarray, '#', '|', '*')
	
	makeLine(inarray, '-', '+', '-')

	for i in range(3):
		makeLine(inarray, ':', '|', '$')

def makeLine(inarray, a, b, c):
	inarray.append([])
	iter = len(inarray) - 1 
	for i in range(4):
		inarray[iter].append(a)
	inarray[iter].append(b)
	for i in range(4):
		inarray[iter].append(c)

def resetMap(mainmap):
	mainmap = []
	genMap(mainmap)

genMap(mainmap)

#shows the map off
def showMap(mainmap):
	print " 123456789 "
	print "+---------+"
	iter = 0
	for z in range(len(mainmap)):
		iter += 1
		if ((z + 1) == coords[1]):
			storage = mainmap[coords[1]-1]
			storage[coords[0]-1] = '@'
			print (str(iter) + '|' + (''.join(storage)) + '|')
		else:
			print (str(iter) + '|' + (''.join(mainmap[z])) + '|')

	print "+---------+"

showMap(mainmap)

# give the user reason
# dir = x/y (0 = x, 1 = y)
# move = direction of movement (move on x is right, move on y is down)
def move(coords, dir, move):
	coords[dir] += move
	if coords[dir] > 9:
		coords[dir] = 1
	if coords[dir] < 1:
		coords[dir] = 9

#UI
while True:
	cmd = raw_input(": ").lower()
	
	if cmd == 'u':
		move(coords, 1, -1)
		showMap(mainmap)
		resetMap(mainmap)
	if cmd == 'd':
		move(coords, 1, 1)
		showMap(mainmap)
		resetMap(mainmap)
	if cmd == 'r':
		move(coords, 0, 1)
		showMap(mainmap)
		resetMap(mainmap)
	if cmd == 'l':
		move(coords, 0, -1)
		showMap(mainmap)
		resetMap(mainmap)
	if cmd == 'q':
		break