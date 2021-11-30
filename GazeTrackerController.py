import tkinter as tk
from tkinter import ttk
import math

class Controller():
    
    baseData:list = []
    gazeVectorData:list = []
    gazeAngleData:list = []
    pointData:list = []

    def __init__(self,master,model,view):
        self.master = master
        self.model = model
        self.view = view

        self.master.bind("<space>",self.moveController)
        
    def moveController(self,event):
        self.model.moveModel(self.view.canvas,"id1")

    def movePoint(selfm, event):
        print('movepoint here?')
        
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
        #return self.gazeVectorData
            
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
        #return self.gazeAngleData
    
    def AngleToPoint(self, distance):
        self.pointData.clear()
        try:
            if distance is not None:
                for num in range(len(self.gazeAngleData)):
                    point = distance * math.tan(self.gazeAngleData[num])
                    self.pointData.append(point)
        except:
            print('to point error')
        
        print(self.pointData)
