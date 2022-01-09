import tkinter as tk
from tkinter.constants import LEFT, NUMERIC
import cv2
import PIL.Image, PIL.ImageTk
from PIL import Image, ImageTk, ImageOps

import gazetracker as gt

class Application(tk.Frame):
        def __init__(self, master=None):
                super().__init__(master)
                self.master.geometry("720x450")
                self.master.title("GazeTracker")
                self.master.resizable(width=False, height=False)
                self.gazetrack = gt.GazeTrack(2)

                self.subWin = None

                #プロパティ
                self.width = self.gazetrack.cap.get( cv2.CAP_PROP_FRAME_WIDTH)
                self.height = self.gazetrack.cap.get( cv2.CAP_PROP_FRAME_HEIGHT)
                self.fps = self.gazetrack.cap.get(cv2.CAP_PROP_FPS)
                self.frame_num = self.gazetrack.cap.get(cv2.CAP_PROP_FRAME_COUNT)
                self.time = self.frame_num / self.fps
        
                self.create_frame()
                self.create_widget()
                self.delay = 10
                self.play_video()
        
        def create_frame(self):
                #フレームの作成frame1 = 背景 frame2 = ラベル
                self.frame1 = tk.Frame(self.master, width=720, height=505, bg="#C4C4C4")
                self.frame1.place(x=0, y=0)
                self.frame2 = tk.Frame(self.master, width=720, height=25, bg="#3F3F3F")
                self.frame2.place(x=0, y=0)
                self.canvas = tk.Canvas(self.frame1, width=720, height=480)
                self.canvas.pack()
        
        def create_widget(self):
                #Labelの生成
                b_camera = tk.Button(self.frame2, text = "camera", width=3, command=self.setup_window)
                b_camera.pack(side=tk.LEFT)

        def setup_window(self):
                if self.subWin == None or not self.subWin.winfo_exists():
                        self.subWin = tk.Toplevel()
                        self.subWin.resizable(width=False, height=False)
                        self.subWin.geometry("300x100")
                        self.subWin.title("camera")
                        headLabel = tk.Label(self.subWin, text="head")
                        headLabel.grid(row=0, column=0, padx=5, pady=2, sticky=tk.E)
                        outcameraLabel = tk.Label(self.subWin, text="outCamera")
                        outcameraLabel.grid(row=1, column=0, padx=5, pady=2, sticky=tk.E)
                        
                        head = tk.StringVar()
                        headEntry = tk.Entry(
                                self.subWin,
                                textvariable=head,
                                width=20
                        )
                        headEntry.grid(row=0, column=1)

                        outCamera = tk.StringVar()
                        outCameraEntry = tk.Entry(
                                self.subWin,
                                textvariable=outCamera,
                                width=20
                        )
                        outCameraEntry.grid(row=1, column=1)
                        #incamera_label.pack()
                        self.subApply = tk.Frame(self.subWin)
                        self.subApply.grid(row=2, column=1, padx=0, pady=5, sticky=tk.W)

                        applyButton = tk.Button(
                                self.subApply,
                                text="Apply",
                                command = lambda: print("apply")
                        )
                        applyButton.pack(side=LEFT)
                        cancelButton = tk.Button(
                                self.subApply,
                                text="Cancel",
                                command = self.close_sub
                        )
                        cancelButton.pack(side=LEFT)
        
        def close_sub(self):
                self.subWin.destroy()






        def play_video(self):
                self.gazetrack.tracking(height= self.height, width= self.width, dsize= 720)
                #self.gazetrack.tracking(height= 720, width= 480, dsize= 720)
                self.image = PIL.Image.fromarray(self.gazetrack.frame)
                self.photo = PIL.ImageTk.PhotoImage(image = self.image)
                self.canvas.create_image(0, 30, image= self.photo, anchor = tk.NW)
                #10ms
                self.master.after(self.delay, self.play_video)

def main():
        root = tk.Tk()
        app = Application(master=root)
        app.subWin = None
        app.mainloop()

if __name__ == "__main__":
        main()