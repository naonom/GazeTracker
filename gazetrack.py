from math import sqrt
from sys import argv, stdin
from time import perf_counter

def getArgs():
	interval = float(argv[1])
	margin = int(argv[2])
	return (interval, margin)

def main(interval, margin):
	line = stdin.readline()
	idx = parse(line)
	print(idx)

	while line:
		line = stdin.readline()
		row = line.split(', ')
		print(row)

def parse(header):
	names = header
	n = len(names)
	z = zip(names, range(n))
	return dict(z)

if __name__ == '__main__':
	main(*getArgs())


