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
		date = line.split(',')
		
		print(date)
		#gaze(idx, row, 0)

def get(idx, row, name):
	i = idx[name]
	return row[i]

def gaze(idx, row, lr):
	def g(c):
		return float(get(idx, row, 'gaze_{}_{}'.format(lr, c)))
	print(g('x'))
	return (g('x'),g('y'),g('z'))


if __name__ == '__main__':
	main(*getArgs())


