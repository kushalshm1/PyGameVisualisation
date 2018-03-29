
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
circleRadius = 50

bigCircleRadius = 100

#All Vectors:
# position = vector.create('position',200,200)
# velocity = vector.create('velocity',0,0)
# vector.setLength(velocity,3)
# vector.setAngle(velocity,(math.pi/6))
#Creating a Particle:
particles = []
numParticles = 50
particleGravity = vector.create('particleGravity',0,10)
for x in range(0,numParticles):
	randomPositionX = random.randint(0,30)
	randomPositionY = random.randint(0,30)
	randomVelocity = random.randint(0,50)
	particles.append(p.create(randomPositionX,randomPositionY,randomVelocity,(math.pi/6)))
	particlePosition = vector.toInt(particles[x][0])
	particleVelocity = vector.toInt(particles[x][1])
	particles[x] = [particlePosition,particleVelocity]

print(particles)
speed = 0


pg.init()
mainDisplay = pg.display.set_mode((width,width))
pg.display.set_caption("Ball Movement")
frames = pg.time.Clock()
pause = True


def render():
	global particle,position,velocity,particlePosition,particleVelocity,speed,colors
	mainDisplay.fill(white)


	for x in range(0,numParticles):
		randomBlue = random.randint(0,255)
		randomRed = random.randint(0,255)
		randomGreen = random.randint(0,255)
		randomColor = (randomRed,randomBlue,randomGreen)
		position = vector.toInt(vector.multiplyScalar(vector.add(particles[x][0],particles[x][1]),speed))
		position = vector.toInt(vector.multiplyScalar(vector.add(position,particleGravity),speed))

		speed = speed+0.001
		pg.draw.circle(mainDisplay,randomColor,position,circleRadius,0)
	pg.display.update()
	frames.tick(800)




while True:
	for event in pg.event.get():
		if(event.type == pg.QUIT):
			pg.quit()
			sys.exit() 
	render()



