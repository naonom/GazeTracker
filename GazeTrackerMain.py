import tkinter as tk
import time
from GazeTrackerController import Controller
from GazeTrackerModel import Model
from GazeTrackerView import View
import cv2
from PIL import Image, ImageTk, ImageOps

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.model = Model()

        master.geometry(str(self.model.width)+"x"+str(self.model.height))
        master.title("gazetracker")

        self.view = View(master,self.model)
        self.controller = Controller(master,self.model,self.view)
        #self.update_data()
        
    def get_data(self):
        self.controller.getDataController()
        self.master.after(60, self.get_data)

    def update_data(self):
        #s = time.time()
        #self.controller.pickGazeVectorData()
        self.controller.pickGazeAngleData()
        self.controller.AngleToPoint(50.0)
        self.controller.setupPoint()
        self.controller.movePointController()
        #e = time.time()
        #print((e-s) * 1000)
        self.master.after(10, self.update_data)

    def dispImage(self):
        ret, frame = self.view.capture.read()

        cv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(cv_image)

        pil_image = ImageOps.pad(pil_image, (self.model.width, self.model.height))
        self.photo_image = ImageTk.PhotoImage(image=pil_image)
        self.view.canvas.create_image(
            self.model.width/2,
            self.model.height/2,
            image=self.photo_image
        )
        self.master.after(10, self.dispImage)

def main():
    root = tk.Tk()
    app = Application(master = root)
    root.after(60, app.get_data)
    root.after(10, app.dispImage)
    root.after(10, app.update_data)
    app.mainloop()


   
if __name__ == "__main__":
    main()