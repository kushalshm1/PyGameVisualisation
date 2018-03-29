import pygame as pg 
import numpy as np 
import math 
import random

red = (100,0,0)
blue = (0,0,155)
green = (0,155,0)
white = (255,255,255)
black = (0,0,0)

width = 500
mainDisplay = pg.display.set_mode((width,width))


status = True


while(status):
	for event in pg.event.get():
		if(event.type == pg.QUIT):
			status = False
		if(event.type == pg.KEYDOWN):
			if(event.key == pg.K_c):
				for i in range(0,500):
					pg.draw.rect(mainDisplay,white,[random.randint(0,500),random.randint(0,500),30,2])
					pg.display.update()




	mainDisplay.fill(red)
	pg.display.update()

pg.quit()

quit()