from sys import stdin

class CSV:
    def __init__(self):
        pass
    def Row(self):
        line = stdin.readline()
        row = line.split(',')
        print(row)

