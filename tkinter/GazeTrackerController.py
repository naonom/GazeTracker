import tkinter as tk
from tkinter import Canvas, ttk
import math

class Controller():
    
    baseData:list = []
    gazeVectorData:list = []
    gazeAngleData:list = []
    pointData:list = []
    beforeshowPointData: list = [0.0, 0.0]
    movePointData:  list = []

    limitArea: list = []

    limitPoint: list = []
    def __init__(self,master,model,view):
        self.master = master
        self.model = model
        self.view = view

        self.limitArea.append(self.model.width / 2)
        self.limitArea.append(self.model.height/ 2)
        point_x = self.limitArea[0]/2
        point_y = self.limitArea[1]/2

        #self.master.bind("<space>",self.moveController)
        
    #def moveController(self,event):
        #self.model.moveModel(self.view.canvas,"id1")

    def movePointController(self):
        #print('movepoint here?')
        #0より小さい1280より大きい場合動かさない
        output_x: float = 0.0
        output_y: float = 0.0
        try:
            #self.point_x += self.showPointData[0]
            #self.point_y += self.showPointData[1]
            #print(self.limitArea[0] + self.movePointData[0])

            if self.limitArea[0] + self.movePointData[0] > 0 and self.limitArea[0] + self.movePointData[0] < self.model.width: 
                output_x = self.movePointData[0]
            if self.limitArea[1] + self.movePointData[1] > 0 and self.limitArea[1] + self.movePointData[1] < self.model.height:
                output_y = self.movePointData[1]
            #self.model.movePoint(self.view.canvas,"viewpoint", output_x, output_y)

            self.model.movePoint(self.view.canvas,"viewpoint", self.movePointData[0], self.movePointData[1])
        except:
            self.model.movePoint(self.view.canvas,"viewpoint", 0, 0)
        
    def getDataController(self):
        self.baseData = self.model.getDataModel()
        #print(self.baseData)

    #check facedata and pick gazedata
    def pickGazeVectorData(self):
        try:
            self.gazeVectorData.clear()
            if self.baseData[4] == '1':
                for num in range(6):
                    self.gazeVectorData.append(float(self.baseData[num + 5]))
            else:
                for i in 6:
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
            else:
                self.gazeAngleData.clear()
                for i in 6:                  
                    self.gazeAngleData.append(0.0)
                print('tracking fail')
        except:
            self.gazeAngleData.clear()
            for i in range(2):
                self.gazeAngleData.append(0.0)
            print('check data fail')
        #print(self.gazeAngleData)
    
    def AngleToPoint(self, distance):
        self.pointData.clear()
        try:
            if distance is not None:
                for num in range(len(self.gazeAngleData)):
                    point = distance * math.tan(self.gazeAngleData[num])
                    self.pointData.append(point)
        except:
            print('to point error')
        
        #print(self.pointData)

    def setupPoint(self):
        try: 
            showPoint_x = self.pointData[0] * -25
            showPoint_y = (self.pointData[1]-13) * 20


            self.movePointData.clear()
            self.movePointData.append(showPoint_x - self.beforeshowPointData[0])
            self.movePointData.append(showPoint_y - self.beforeshowPointData[1])

            
            self.beforeshowPointData.clear()
            self.beforeshowPointData.append(showPoint_x)
            self.beforeshowPointData.append(showPoint_y)
            
        except:
            print('setup point error')