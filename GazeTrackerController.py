import tkinter as tk
from tkinter import ttk

class Controller():
    

    def __init__(self,master,model,view):
        self.master = master
        self.model = model
        self.view = view



        self.master.bind("<space>",self.moveController)
        
    def moveController(self,event):
        self.model.moveModel(self.view.canvas,"id1")

    def getDataController(self):
        self.baseData = self.model.getDataModel()
    
    #check facedata and pick gazedata
    def pickGazeVectorData(self) -> list:
        gazeData = []
        '''
        try:
            if baseData[4] == '1':
                for num in range(6):
                    gazeData.append(int(baseData[num + 5]))
            else:
                for i in 6:
                    gazeData.append(0)
                print('tracking failure')
        except:
                for i in 6:
                    gazeData.append(0)
        '''
        print('pick')
        return gazeData
            
