cal=0
print("Welcome to Chip's fast food imporium")
print("(1)Cheeseburger (461 calories)")
print("(2)Fish Burger (431 calories)")
print("(3)Veggie Burger (420 calories)")
print("(4)None(0 calories)")
burger=input("Please enter a burger choice:")
if burger==1:
	cal+=461
if burger==2:
	cal+=431
if burger==3:
	cal+=420
if burger==4:
	cal+=0
print("(1)fries (100 calories)")
print("(2)Baked Potato(57 calories)")
print("(3)Chef salad (70 calories)")
print("(4)None(0 calories)")
burger=input("Please enter a Side order choice:")
if burger==1:
	cal+=100
if burger==2:
	cal+=57
if burger==3:
	cal+=70
if burger==4:
	cal+=0
print("(1)Soft Drink (130 calories)")
print("(2)Orange Juice (160 calories)")
print("(3)Milk (118 calories)")
print("(4)None(0 calories)")
burger=input("Please enter a Drink choice:")
if burger==1:
	cal+=130
if burger==2:
	cal+=160
if burger==3:
	cal+=118
if burger==4:
	cal+=0
print("(1)Apple Pie (167 calories)")
print("(2)Sundae (266 calories)")
print("(3)Fruit Cup (75 calories)")
print("(4)None(0 calories)")
burger=input("Please enter a dessert choice:")
if burger==1:
	cal+=167
if burger==2:
	cal+=266
if burger==3:
	cal+=75
if burger==4:
	cal+=0
print (cal)