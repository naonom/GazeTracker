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
        print('controller')
        self.controller.getDateController()
        self.master.after(1000, self.update_data)

def main():
    root = tk.Tk()
    app = Application(master = root)
    root.after(1000, app.update_data)
    #app.update_data()
    app.mainloop()


   
if __name__ == "__main__":
    main()