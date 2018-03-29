import vectorOperationFunctions as vector



particlePosition = [0]*2
particleVelocity = [0]*2
particleAcceleration = [0]*2
particle = [0]*2
created = [0]*2
createdVelocity = [0]*2
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

