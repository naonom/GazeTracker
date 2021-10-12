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
		if date is not None:
			print(date)


def get(baseDate):
	if baseDate is not None:
		if baseDate[4] == '1': #Openface success
			return baseDate
		else:
			print('Openface failure')
	else:
		print('can not get baseDate')

def gaze(idx, row, lr):
	def g(c):
		return float(get(idx, row, 'gaze_{}_{}'.format(lr, c)))
	print(g('x'))
	return (g('x'),g('y'),g('z'))


if __name__ == '__main__':
	main(*getArgs())


