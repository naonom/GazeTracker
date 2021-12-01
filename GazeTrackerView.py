import tkinter as tk

class View():
    def __init__(self,master,model):
        self.master = master
        self.model = model

        self.canvas = tk.Canvas(self.master,width=self.model.width,height=self.model.height)
        self.canvas.pack()

        #self.canvas.create_polygon(10,10,10,60,50,35,tag="id1")
        self.canvas.create_oval(self.model.width/2 - 20, self.model.height/2 - 20, self.model.width/2 + 20, self.model.height/2 + 20, tag="viewpoint")



        