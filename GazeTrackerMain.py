import tkinter as tk

from GazeTrackerController import Controller
from GazeTrackerModel import Model
from GazeTrackerView import View

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.model = Model()

        master.geometry(str(self.model.width)+"x"+str(self.model.height))
        master.title("gazetracker")

        self.view = View(master,self.model)
        self.controller = Controller(master,self.model,self.view)
        self.update_data()

    def update_data(self):
        self.controller.getDataController()
        self.controller.pickGazeVectorData()
        self.controller.pickGazeAngleData()
        self.controller.AngleToPoint(50.0)
        self.controller.setupPoint()

        self.controller.movePointController()

        self.master.after(50, self.update_data)

def main():
    root = tk.Tk()
    app = Application(master = root)
    root.after(50, app.update_data)
    app.mainloop()


   
if __name__ == "__main__":
    main()