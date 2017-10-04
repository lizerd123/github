day=input("day:")
month=input("month:")
if month>2:
	print("after")
if month<2:
	print("before")
if month==2:
	if day > 18:
		print("after")
	if day<18:
		print("before")
	if day==18:
		print("same")