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

    def getDateController(self):
        self.master.after(1000, self.model.getDataModel())
        #self.model.getDataModel()

