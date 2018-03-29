import numpy as np
import pygame as pg
import math
import random

x = pg.init()

red = (155,0,0)
blue = (0,0,155)
green = (0,155,0)
white = (255,255,255)
black = (0,0,0)
width = 600
mainDisplay = pg.display.set_mode((width,width))

status = True


vector1 = [-3,2]
vector2 = [1,1]
add = 0
def magnitude(vector):
	global add
	for i in range(0,len(vector)):
		add = add + (vector[i]**2)
	return (add)**0.5


def dotProduct(vector1, vector2):
	global add
	for i in range(0,len(vector1)):
		add = add + (vector1[i]*vector2[i])
	return add

def crossProduct(vector1,vector2):
	global add
	vectorMatrix = np.asarray((vector1,vector2))
	return math.fabs(int(np.linalg.det(vectorMatrix)))




while(status):
	#All the Events:
	randomNumber = random.randint(0,30)
	for event in pg.event.get():
		if(event.type == pg.QUIT):
			status = False
		if(event.type == pg.KEYDOWN):
			if(event.key == pg.K_c):
				mainDisplay.fill(blue)
		if(event.type == pg.KEYDOWN):
			if(event.key == pg.K_a):
				vector1 = [random.randint(0,randomNumber),random.randint(0,randomNumber)]
				vector2 = [random.randint(0,randomNumber),random.randint(0,randomNumber)]
				pg.draw.rect(mainDisplay,blue,[(width/2)+10,(width/2)+10,crossProduct(vector1,vector2),2])
			if(event.key == pg.K_r):
				vector1 = [1,1]
				vector2 = [1,1]
	pg.draw.rect(mainDisplay,white,[(width/2),(width/2),crossProduct(vector1,vector2),2])
	pg.display.update()


pg.quit()
quit()