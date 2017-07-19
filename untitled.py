

	screen.blit(hero,(x1,y1))
	
	if jumping==1 and y1>200:
		y1-=10
	if y1==200:
		jumping=0
	if jumping==0 and y1<400:
		y1+=10
	if y1<400:
		friction=1
	else:
		friction=1.08
	if  x1<860 and x1>40:
		print
	else:
		y1+=10
		if y1>400:
			y1+=10
	if y1>700:
		print("you fell")
		sys.exit()
	velocity/=friction
	if distance==0:
		time=00000000.1
	x1+=velocity
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == K_j:
				distance=-10
				time=1
				speed=distance/time
				velocity=speed/time

			if event.key == K_l:
				distance=10
				time=1
				speed=distance/time
				velocity=speed/time
			if event.key == K_i and y1==400:
				jumping=1
	