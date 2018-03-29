import pygame as pg 
import random
import math
#Defining Colors:
x = pg.init()
white = (255,255,255)
green = (0,255,0)
black = (0,0,0)
blue = black
red = (255,0,0)

def distanceX(x1,x2):
	near = x1 if (x1 < x2) else x2
	return  near + math.fabs(x1-x2)*.5

def distanceY(y1,y2):
	near = y1 if (y1 < y2) else y2

	return near + math.fabs(y1-y2)*.5



width = 600

display = pg.display.set_mode((width,width))

kushal = True

tris = [[width/2,10],[10,width-10],[width-10,width-10]];

curNum = 1
factor = 5

a = [tris[0][0],tris[0][1]]
b = [tris[1][0],tris[1][1]]
c = [tris[2][0],tris[2][1]]

diceList = [0]*2
coordinatesOne = (0,0)
coordinatesTwo = (0,0)
finalCoordinates = (0,0)

preCoords = (tris[0][0],tris[0][1])
curCoords = (0,0)

pt_arr = []


count= 0

while(count<10 or kushal):
	display.fill(blue)

	pg.draw.rect(display,white,[tris[0][0],tris[0][1],2,2])
	pg.draw.rect(display,white,[tris[1][0],tris[1][1],2,2])
	pg.draw.rect(display,white,[tris[2][0],tris[2][1],2,2])
	reset = False
	for i in range(100):
		if (reset != True):
			curNum = random.randint(1,7)
			coordinatesOne = preCoords

			if(curNum == 1 or curNum==2):
				curCoords = (width/(2+(factor-1)),10)
			if(curNum == 3 or curNum==4):
				curCoords = (b[0]*(-factor),b[1]*factor)
			if(curNum == 5 or curNum==6):	
				curCoords = (c[0]*factor,   c[1]*factor)
			# print(curNum,"currCoords",curCoords,"preCoords",preCoords,"finalCoordinates",finalCoordinates)

			finalCoordinates = (curCoords[0]*0 + round(distanceX(preCoords[0],curCoords[0])*1),curCoords[1]*0 + round(distanceY(preCoords[1],curCoords[1]))*1)

			# pg.draw.rect(display,white,[finalCoordinates,2,2])


			pt_arr.append(finalCoordinates);

			if(finalCoordinates!=(0.0,0.0)):
				preCoords = finalCoordinates

			reset = False;
			if (finalCoordinates[0] > width or finalCoordinates[1] > width):
				reset = True;

			for i in range(len(pt_arr)):
				ccd = pt_arr[i]
				# print(ccd)
				pg.draw.rect(display,white,[ccd[0],ccd[1],2,2])

#Event ka jugaad
	for event in pg.event.get():
		if(event.type == pg.QUIT):
			kushal = False
		
		if(event.type == 5):
			# white = (0,100,0);
			factor +=0.1;
			display.fill(blue)
			pt_arr = []
	pg.display.update()
	count+=1


pg.quit()
quit()