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
bigCircleRadiusX = 100
bigCircleRadiusY = 200

angle = 0
speed = 0.01
x = width/2
y = width/2





pg.init()
mainDisplay = pg.display.set_mode((width,width))
pg.display.set_caption("Ball Movement")
frames = pg.time.Clock()
pause = True

#Making Balls

ballOnePosition = [width/2,width/2]


def update():

	ballOnePosition[0] = ballOnePosition[0] + 4
	ballOnePosition[1] = ballOnePosition[1] + 0

def render():
	global angle, bigCircleRadiusX,bigCircleRadiusY,origin, ballOnePosition
	mainDisplay.fill(white)
	x = bigCircleRadiusX*int(math.fabs(math.cos(angle)*3))
	y = bigCircleRadiusY*int(math.fabs(math.sin(angle)*3))
	print(x,y)
	ballOnePosition = [x,y]
	pg.draw.circle(mainDisplay,red,ballOnePosition,circleRadius,0)
	angle = angle+speed

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

			angle = angle+0.1
			ballOnePosition = [x,y]

	if not pause:
		update()


	render()


