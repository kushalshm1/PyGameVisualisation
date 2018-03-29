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

angleX = 0
speedX = 0.01
angleY = 0
speedY = 0.1
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
	global 
	mainDisplay.fill(white)
	x = bigCircleRadiusX*int(math.fabs(math.cos(angleX)*3))

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


