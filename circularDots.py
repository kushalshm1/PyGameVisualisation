import pygame as pg 
import sys
import math 
import random


black = (0,0,0)
white = (255,255,255)
blue  = (0,0,255)
red   = (255,0,0)
green = (0,155,0)

#ALl Variables
width = 1000
circleRadius = 30
origin = (width/2)
bigCircleRadius = 100

angle = 0
speed = 0.01

x = width/2
y = width/2
numObjects = 10
sliceVariable = (math.pi*2)/numObjects



pg.init()
mainDisplay = pg.display.set_mode((width,width))
pg.display.set_caption("Ball Movement")
frames = pg.time.Clock()
pause = True

#Making Balls

ballOnePosition = [width/2,width/2]


def update():
	global angle,speed,bigCircleRadius,bigCircleRadius,origin,ballOnePosition
	x = bigCircleRadius*int(math.fabs(math.cos(angle)*6))
	y = bigCircleRadius*int(math.fabs(math.sin(angle)*6))
	print(x,y)
	angle = angle+speed
	ballOnePosition = [x,y]

def render():
	global angle,speed,bigCircleRadius,bigCircleRadius,origin,ballOnePosition
	mainDisplay.fill(white)
	pg.draw.circle(mainDisplay,red,ballOnePosition,circleRadius,0)
	pg.display.update()
	frames.tick(50)

while True:
	for event in pg.event.get():
		if(event.type == pg.QUIT):
			pg.quit()
			sys.exit() 
		if(event.type == pg.KEYUP):
			if(event.key == pg.K_SPACE):
				pause = not pause

	if not pause:
		update()


	render()


