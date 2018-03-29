import vectorOperationFunctions as vector
import math


particlePosition = [0]*2

particleVelocity = [0]*2
particleAcceleration = [0]*2
particle = [0]*2
created = [0]*2
createdVelocity = [0]*2
mass = 1
gravity = vector.create('gravity',0,0)
gravityAdded = [0]*2

def create(x,y,speed,direction,acceleration):
	global created
	particlePosition = vector.create('particlePosition',x,y)
	particleVelocity = vector.create('particleVelocity',0,0)
	particleAcceleration = vector.create('particleAcceleration',0,acceleration)
	vector.setLength(particleVelocity,speed)
	vector.setAngle(particleVelocity,direction)
	created = [particlePosition,particleVelocity]
	return [particlePosition,particleVelocity]

# def accelerate()

def velocityAdded():
	global created
	return vector.add(created[0],created[1])


def accelerationAdded():
	global particleAcceleration
	global createdVelocity
	return vector.add(particleAcceleration,velocityAdded())

def angleTo(particle1,particle2):
	return math.atan2(vector.getY(particle2) - vector.getY(particle1),vector.getX(particle2) - vector.getX(particle1))

def distanceTo(particle1,particle2):
	dx = vector.getX(particle2) - vector.getX(particle1)
	dy = vector.getY(particle2) - vector.getY(particle1)
	return ((dx*dx) - (dy*dy))**0.5


def gravitateTo(particle1,particle2):
	global gravity
	global mass
	global gravityAdded
	distance = distanceTo(particle1,particle2)
	vector.setLength(gravity,(mass/(distance*distance)))
	vector.setAngle(gravity,angleTo(particle1,particle2))
	return vector.add(velocityAdded,gravity)
