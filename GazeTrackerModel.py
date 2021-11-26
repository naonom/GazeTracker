import tkinter as tk
from sys import stdin

class Model():
    def __init__(self):
        self.width=1280
        self.height=720

    def moveModel(self,canvas,id):
        canvas.move(id,5,5)
    
    def getDataModel(self) -> list:
        #print('here')
        
        baseData = []
        try:
            line = stdin.readline()
            baseData = line.split(',')
            print(baseData)
            return baseData
        
        except:
            print('can not read line')
            fake = []
            for i in range(497):
                fake.append('0')
            baseData = fake
            print(baseData)
            return baseData
        

