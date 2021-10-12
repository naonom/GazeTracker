from math import sqrt
from sys import argv, stdin
from time import perf_counter

def getArgs():
	interval = float(argv[1])
	margin = int(argv[2])
	return (interval, margin)

def main(interval, margin):
	line = stdin.readline()
	row = line.split(',')
	while line:
		line = stdin.readline()
		baseDate = line.split(',')
		print(baseDate)
		date = get(baseDate)
		gaze = getGaze(date)
		print(gaze)


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
		print('Date is None')
	
def fakeDate(num):
	fake = []
	for i in range(497):
		fake.append('0')
	return fake

if __name__ == '__main__':
	main(*getArgs())


