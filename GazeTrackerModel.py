import tkinter as tk
from sys import stdin

class Model():
    def __init__(self):
        self.width=1280
        self.height=720

    def moveModel(self,canvas,id):
        canvas.move(id,5,5)

    def movePoint(self, canvas, id, x, y):
        canvas.move(id, x, y)
    
    def getDataModel(self) -> list:
        
        baseData = []
        try:
            line = stdin.readline()
            baseData = line.split(',')
            return baseData
        
        except:
            print('tail fail')
            fake = []
            for i in range(497):
                fake.append('0')
            baseData = fake
            return baseData
        

