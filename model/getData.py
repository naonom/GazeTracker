from sys import stdin
from typing import List

class CSV():
    beforeGazeAngle: List[float] = [0.0, 0.0]
    
    def __init__(self):
        pass

    #get data row
    def Row(self) -> None:
        try:
            rowline = stdin.readline()
            row = rowline.split(',')
            print(row)
        except:
            print('row error')

    #get face data
    def gazeData(self) -> list:
        try:
            line = stdin.readline()
            baseData = line.split(',')
            if baseData[4] == '1': #get face data
                return baseData
            else:
                fake = []
                for i in range(497):
                    fake.append('0')
                return fake
        except:
            print('openface failure')
            fake = []
            for i in range(497):
                fake.append('0')
            return fake
		             