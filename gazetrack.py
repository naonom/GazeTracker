from math import sqrt
from sys import argv, stdin

import viewpoint as vp
import isdatecorrect as idc

def getArgs():
	interval = float(argv[1])
	margin = int(argv[2])
	return (interval, margin)

def main(interval, margin):
	setup()
	beforeGazeAngle = [0.0, 0.0]
	while True:
		line = stdin.readline()
		baseDate = line.split(',')
		date = getDate(baseDate)
		rowGazeAngle = filterGazeAngle(date)
		gazeAngle = checkGazeAngle(beforeGazeAngle, rowGazeAngle)
		print(gazeAngle, end='')
		
		gazePoint = getPoint( gazeAngle)
		print(gazePoint)

def setup():
	try:
		line = stdin.readline()
		row = line.split(',')
		print(row)
	except:
		print('Openface setup error')

#get date from csv
def getDate(baseDate):
	try:
		if baseDate[4] == '1': #Openface success
			return baseDate
		else:
			return fakeDate(497)
			print('Openface failure')
	except:
		return fakeDate(497)
		print('Can not get baseDate')

#filter gaze vector date from date
def filterGazeVector(date):
	try:
		gazeDate = []
		for num in range(6):
			gazeDate.append(date[num + 5])
		return gazeDate
	except:
		return fakeDate(6)
		print('GazeDate is None')

#filter gaze angle date from date
def filterGazeAngle(date):
	try:
		gazeAngleDate = []
		for num in range(2):
			floatNum = float(date[num + 11])
			gazeAngleDate.append(floatNum)
		return gazeAngleDate
	except:
		gazeAngleDate.append(0.0)
		gazeAngleDate.append(0.0)
		print('GazeAngleDate is None')

#check gaze angle date
def checkGazeAngle(beforeGazeAngle, gazeAngle):
	isGazeAngleCorrect = idc.isGazeAngleDateCorrect(beforeGazeAngle, gazeAngle, 200.0)
	if isGazeAngleCorrect is True:
		return gazeAngle
	else:
		return beforeGazeAngle
 
#gazedate to point
def getPoint(gazeAngle):
	gazePointDate = []
	try:
		for num in range(len(gazeAngle)):
			degree = vp.radianToDegree(gazeAngle[num])
			point = vp.degreeToPoint(degree, 50.0)
			gazePointDate.append(point)	
	except:
		gazePointDate.append(0.0)
		gazePointDate.append(0.0)
	return gazePointDate

#false date
def  fakeDate(num):
	fake = []
	for i in range(num):
		fake.append('0')
	return fake

if __name__ == '__main__':
	main(*getArgs())


