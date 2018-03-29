import pygame as pg 
import sys
import math 
import random


black = (0,0,0)
white = (255,255,255)
blue  = (0,0,255)
red   = (255,0,0)
green = (0,155,0)

circleRadius = 30

width = 600

pg.init()
mainDisplay = pg.display.set_mode((width,width))
pg.display.set_caption("Ball Movement")
frames = pg.time.Clock()
pause = True

#Making Balls

ballOnePosition = [50,50]
ballTwoPosition = [50,240]
ballThreePosition = [50,450]

def update():
	global circleRadius
	ballOnePosition[0] = ballOnePosition[0] + 4
	ballOnePosition[1] = ballOnePosition[1] + 0

	ballTwoPosition[0] = ballTwoPosition[0] + 4
	ballTwoPosition[1] = ballTwoPosition[1] + 0

	ballThreePosition[0] = ballThreePosition[0] + 4
	ballThreePosition[1] = ballThreePosition[1] + 0

def render():
	mainDisplay.fill(white)
	pg.draw.circle(mainDisplay,red,ballOnePosition,circleRadius,0)
	pg.draw.circle(mainDisplay,blue,ballTwoPosition,circleRadius,0)
	pg.draw.circle(mainDisplay,green,ballThreePosition,circleRadius,0)
	pg.display.update()
	frames.tick(50)

angle = 0
while True:
	for event in pg.event.get():
		if(event.type == pg.QUIT):
			pg.quit()
			sys.exit() 
		if(event.type == pg.KEYUP):
			if(event.key == pg.K_SPACE):
				pause = not pause
	# print(ballThreePosition)

	if(ballThreePosition[0] >= width-width):
		# circleRadius += circleRadius/20
		circleRadius = int((math.fabs(math.sin(angle)*100)))
		angle = angle + 0.1

		print(circleRadius)




	print("success")

	if not pause:
		update()


	render()


