
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


sun = p.create(width/2,width/2,0,0,0)
planet = p.create(width/2+200,width/2,10,-math.pi/2,0)
planetPosition = planet[0]
planetVelocity = planet[1]
sunPosition = sun[0]
sunVelocity = sun[1]

sunMass = 20000



speed = 0


pg.init()
mainDisplay = pg.display.set_mode((width,width))
pg.display.set_caption("Ball Movement")
frames = pg.time.Clock()
pause = True



def render():
	global particle,position,velocity,particlePosition,particleVelocity,speed,colors,thrust
	mainDisplay.fill(white)
	position  = p.velocityAdded()
	position = p.gravitateTo(planetPosition,sunPosition)
	pg.draw.circle(mainDisplay,red,position,circleRadius,0)


	pg.display.update()
	frames.tick(30)




while True:
	for event in pg.event.get():
		if(event.type == pg.QUIT):
			pg.quit()
			sys.exit()


	render()



