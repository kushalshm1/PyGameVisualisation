import pygame as pg 
import sys
import math 
import random
import vectorOperationFunctions as vector
import particleFunctions as p
black = (0,0,0)
white = (255,255,255)
blue  = (0,0,255)
red   = (255,0,0)
green = (0,155,0)

#ALl Variables
width = 600
circleRadius = 30

bigCircleRadius = 100

#All Vectors:
# position = vector.create('position',200,200)
# velocity = vector.create('velocity',0,0)
# vector.setLength(velocity,3)
# vector.setAngle(velocity,(math.pi/6))
#Creating a Particle:

particle = (p.create(100,100,3,(math.pi/6)))
particlePosition = vector.toInt(particle[0])
particleVelocity = vector.toInt(particle[1])
particle = [particlePosition,particleVelocity]
print(particlePosition,particleVelocity)
speed = 0


pg.init()
mainDisplay = pg.display.set_mode((width,width))
pg.display.set_caption("Ball Movement")
frames = pg.time.Clock()
pause = True




def update():
	mainDisplay.fill(white)

def render():
	global particle,position,velocity,particlePosition,particleVelocity,speed
	mainDisplay.fill(white)
	position = vector.toInt(vector.multiplyScalar(vector.add(particlePosition,particleVelocity),speed))
	speed = speed+0.01
	pg.draw.circle(mainDisplay,red,position,circleRadius,0)
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


