from math import sqrt
from sys import argv, stdin

import viewpoint as vp

def getArgs():
	interval = float(argv[1])
	margin = int(argv[2])
	return (interval, margin)

def main(interval, margin):
	line = stdin.readline()
	row = line.split(',')
	print(row)
	while line:
		line = stdin.readline()
		baseDate = line.split(',')
		date = get(baseDate)
		gaze = getGaze(date)
		gazeAngle = getGazeAngle(date)
		print(gazeAngle)

def get(baseDate):
	if baseDate is not None:
		if baseDate[4] == '1': #Openface success
			return baseDate
		else:
			return fakeDate(497)
			print('Openface failure')
	else:
		return fakeDate(497)
		print('Can not get baseDate')

def getGaze(date):
	if date is not None:
		gazeDate = []
		for num in range(6):
			gazeDate.append(date[num + 5])
		return gazeDate
	else:
		return fakeDate(6)
		print('GazeDate is None')

def getGazeAngle(date):
	if date is not None:
		gazeAngleDate = []
		for num in range(2):
			floatNum = float(date[num + 11])
			degree = vp.radianToDegree(floatNum)
			point = vp.degreeToPoint(degree, 50.0)
			gazeAngleDate.append(point)
		return gazeAngleDate
	else:
		return fakeDate(2)
		print('GazeAngleDate is None')

def  fakeDate(num):
	fake = []
	for i in range(num):
		fake.append('0')
	return fake



if __name__ == '__main__':
	main(*getArgs())


