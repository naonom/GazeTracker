import math
import numpy as np

#distance = 50cm
def radianToDegree(radian):
	deg = np.rad2deg(radian)
	print(deg, end='')
	print(',', end='')
	return deg

def degreeToPoint(degree, distance):
	tanDegree = np.tan(degree)
	print(tanDegree, end='')
	print(',', end='')
	try:
		point = distance * tanDegree
	except:
		point = 0.0
		print('division by zero' + str(tanDegree))
	return point

def radianToPoint(radian, distance):
	try:
		tanRadian = math.tan(radian)
		point = distance * tanRadian
	except:
		point = 0.0
		print('division by zero' + str(tanRadian))
	return point
	
		



