import math

#distance = 50cm
def radianToDegree(radian):
	deg = math.degrees(radian)
	return deg

def degreeToPoint(degree, distance):
	#0point is camera
	tanDegree = math.tan(degree)
	try:
		point = distance * tanDegree
	except:
		point = 0.0
		print('division by zero' + str(tanDegree))
	return point
	



