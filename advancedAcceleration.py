
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

colors = [black,blue,green,red]

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
ship = p.create(width/2,width/2,1,1,1)

thrust = vector.create('thrust',0,0)



speed = 0


pg.init()
mainDisplay = pg.display.set_mode((width,width))
pg.display.set_caption("Ball Movement")
frames = pg.time.Clock()
pause = True



def render():
	global particle,position,velocity,particlePosition,particleVelocity,speed,colors,thrust
	mainDisplay.fill(white)
	acceleration = p.accelerationAdded()
	position = vector.toInt(vector.multiplyScalar(vector.add(acceleration,thrust),1))


	pg.draw.circle(mainDisplay,red,position,circleRadius,0)

	pg.display.update()
	frames.tick(30)




while True:
	for event in pg.event.get():
		if(event.type == pg.QUIT):
			pg.quit()
			sys.exit()
		if(event.type == pg.KEYDOWN):
			if(event.key == pg.K_UP):
				vector.setY(thrust,-100)
				break;
			if(event.key == pg.K_DOWN):
				vector.setY(thrust,100)
				break;
			if(event.key == pg.K_LEFT):
				vector.setX(thrust,-100)
				break;
			if(event.key == pg.K_RIGHT):
				vector.setX(thrust,100)
				break;
		if(event.type == pg.KEYUP):
			if(event.key == pg.K_UP):
				vector.setY(thrust,0)
				break;
			if(event.key == pg.K_DOWN):
				vector.setY(thrust,0)
				break;
			if(event.key == pg.K_LEFT):
				vector.setX(thrust,0)
				break;
			if(event.key == pg.K_RIGHT):
				vector.setX(thrust,0)
				break;
	print(thrust)
	render()



