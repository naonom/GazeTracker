from sys import stdin
import math
import GazeFilter

class OpenFaceAngle():
    gazefilter:GazeFilter.Filter
    baseData:list = []
    gazeVectorData:list = []
    gazeAngleData:list = []
    pointData:list = []
    movePointData:  list = [0.0, 0.0]

    def __init__(self):
        self.width = 1280
        self.height = 720
        self.gazefilter = GazeFilter.Filter()
    
    def getDataModel(self):
        try:
            line = stdin.readline()
            self.baseData = line.split(',')
        
        except:
            print('tail fail')
            fake = []
            for i in range(497):
                fake.append('0')
            self.baseData = fake
        #print(self.baseData)

    def pickGazeVectorData(self):
        try:
            self.gazeVectorData.clear()
            if self.baseData[4] == '1':
                for num in range(6):
                    self.gazeVectorData.append(float(self.baseData[num + 5]))
            else:
                for i in range(6):
                    self.gazeVectorData.append(0.0)
                print('tracking fail')
        except:
                for i in range(6):
                    self.gazeVectorData.append(0.0)
                print('get data fail')
        #print(self.gazeVectorData)

    def pickGazeAngleData(self):
        try:
            if self.baseData[4] == '1':
                    if self.gazeAngleData[0] - float(self.baseData[11]) < 200 and self.gazeAngleData[1] - float(self.baseData[12]):
                        self.gazeAngleData.clear()
                        self.gazeAngleData.append(float(self.baseData[11]))
                        self.gazeAngleData.append(float(self.baseData[12]))

                        #filter
                        try:
                            self.gazeAngleData[0] = self.gazefilter.filterX(self.gazeAngleData[0])
                            self.gazeAngleData[1] = self.gazefilter.filterX(self.gazeAngleData[1])
                            print("filter")
                        except:
                            return

            else:
                self.gazeAngleData.clear()
                for i in 6:                  
                    self.gazeAngleData.append(0.0)
                print('tracking fail')
        except:
            self.gazeAngleData.clear()
            for i in range(6):                  
                    self.gazeAngleData.append(0.0)
            print('check data fail')
            return
        #print(self.gazeAngleData)

    def AngleToPoint(self):
        self.pointData.clear()
        try:
            for num in range(len(self.gazeAngleData)):
                point = math.tan(self.gazeAngleData[num])
                self.pointData.append(point)
        except:
            print('to point error')
            return
        
        #print(self.pointData)

    def setupPoint(self, dis: int, xdis: float, ydis: float):
        try: 
            self.showPoint_x = self.pointData[0] * -1 * dis + xdis
            self.showPoint_y = self.pointData[1] * dis + ydis
            self.movePointData.clear()
            self.movePointData.append(self.showPoint_x)
            self.movePointData.append(self.showPoint_y)
            
        except:
            print('setup point error')
            return
        
        #print(self.movePointData)