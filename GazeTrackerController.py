import tkinter as tk
from tkinter import ttk

class Controller():
    
    baseData:list = []
    gazeVectorData:list = []
    gazeAngleData:list = []

    def __init__(self,master,model,view):
        self.master = master
        self.model = model
        self.view = view



        self.master.bind("<space>",self.moveController)
        
    def moveController(self,event):
        self.model.moveModel(self.view.canvas,"id1")

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
                    print('data fail')
        #print(self.gazeVectorData)
        return self.gazeVectorData
            
    def pickGazeAngleData(self):
        try:
            self.gazeAngleData.clear()
            if self.baseData[4] == '1':
                for num in range(2):
                    self.gazeAngleData.append(float(self.baseData[num + 11]))
            else:
                for i in 6:
                    self.gazeAngleData.append(0.0)
                print('tracking fail')
        except:
                for i in range(2):
                    self.gazeAngleData.append(0.0)
                    print('data fail')
        print(self.gazeAngleData)
        return self.gazeAngleData