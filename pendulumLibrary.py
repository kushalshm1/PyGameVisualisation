x = 0
y = 0
length = 100
angle = 0
obj = 0


def create(name,x,y,length,angle):
	name = [x,y,length,angle]
	return name

def getEndX(vector):
	return vector[0] + math.cos(vector[3])*vector[2]

def getEndY(vector):
	return vector[0] + math.sin(vector[3])*vector[2]

