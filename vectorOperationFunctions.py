import math 


#Unit vectors:

vector = [0]*2

def getX(vector):
	return vector[0]
def setX(vector,value):
	vector[0] = value
def setY(vector,value):
	vector[1] = value
def getY(vector):
	return vector[1]
def create(vectorName,x,y):
	vectorName = [0]*2
	x = setX(vectorName,x)
	y = setY(vectorName,y)
	return vectorName

def getLength(vector):
	return (((getX(vector)*getX(vector))+(getY(vector)*getY(vector)))**0.5)

def setLength(vector,length):
	angle = getAngle(vector)
	vector[0] = math.cos(angle) * length 
	vector[1] = math.sin(angle) * length

def setAngle(vector,angle):
	length = getLength(vector)
	vector[0] = math.cos(angle) * length 
	vector[1] = math.sin(angle) * length

def getAngle(vector):
	return math.atan2(getX(vector),getY(vector))



def add(vector1,vector2):
	one =  (getX(vector1) + getX(vector2))
	two =  (getY(vector1) + getY(vector2))
	return [one,two]

def subtract(vector1,vector2):
	one =  (getX(vector1) - getX(vector2))
	two =  (getY(vector1) - getY(vector2))
	return [one,two]


def multiplyScalar(vector,scalar):  
	return [(getX(vector)*scalar),(getY(vector)*scalar)]

def divideScalar(vector,scalar):
	return [(getX(vector)/scalar),(getY(vector)/scalar)]

def toInt(vector):
	return [int(vector[0]),int(vector[1])]