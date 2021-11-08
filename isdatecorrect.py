import math

#get date is correct or wrong

def isGazeAngleDateCorrect(before, now, difference):
	try:
		numX = before[0] - now[0]
		numY = before[1] - now[1]	
		#print(abs(num), end = '')
		if abs(numX) < difference and abs(numY) < difference:
			return True
		else:
			return False
	except:
		print('check error')
		return False

