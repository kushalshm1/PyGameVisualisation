import pygame as pg 
import sys
import math 
import random
import vectorOperationFunctions as v
import pendulumLibrary as pend


black = (0,0,0)
white = (255,255,255)
blue  = (0,0,255)
red   = (255,0,0)
green = (0,155,0)

width = 700

#Creating Vectors:

position = v.create('position',10,0)
velocity = v.create('velocity',1,0)
gravity = v.create('gravity',10,1)
v.setAngle(gravity,(math.pi)/2)
print(gravity)


pg.init()
mainDisplay = pg.display.set_mode((width,width))
pg.display.set_caption("Ball Movement")
frames = pg.time.Clock()
pause = True

mainDisplay.fill(white)
# position = [width/2,width/2]
speed = 1
def render():
	mainDisplay.fill(white)
	global position,velocity,gravity, speed
	position = v.add(position,velocity)
	position = v.toInt(v.add(position,gravity))
	pg.draw.circle(mainDisplay,blue,position,20,0)

	pg.display.update()




while True:
	for event in pg.event.get():
		if(event.type == pg.QUIT):
			pg.quit()
			sys.exit() 
		if(event.type == pg.KEYUP):
			if(event.key == pg.K_SPACE):
				pause = not pause

		render()





