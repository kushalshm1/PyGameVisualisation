import pygame as pg 
import numpy as np 
import math 
import random
x = pg.init()

red = (100,0,0)
blue = (0,0,155)
green = (0,155,0)
white = (255,255,255)
black = (0,0,0)

width = 800
mainDisplay = pg.display.set_mode((width,width))


status = True

mainDisplay.fill(red)
while(status):
	for event in pg.event.get():
		if(event.type == pg.QUIT):
			status = False
		if(event.type == pg.KEYDOWN):
			if(event.key == pg.K_c):
				angle = 0
				while(angle<math.pi*4):
					x = (angle*200)
					y = int(math.sin(angle)*(x))
					pg.draw.rect(mainDisplay,white,[x,y,2,2])
					print(x,y)
					angle = angle+0.01

	pg.display.update()		



pg.quit()

quit()