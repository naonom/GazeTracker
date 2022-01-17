import tkinter as tk
from tkinter.constants import LEFT, NUMERIC
import cv2
import PIL.Image, PIL.ImageTk
from PIL import Image, ImageTk, ImageOps
import datetime
import os
import gazetracker as gt
import makedata
import serial


class Application(tk.Frame):
        #ls -l /dev/tty.*

        pointing: bool = False
        xCenter: float = 0.0
        yCenter: float = 0.0

        def __init__(self, master=None):
                super().__init__(master)
                self.master.geometry("720x450")
                self.master.title("GazeTracker")
                self.master.resizable(width=False, height=False)
                self.gazetrack = gt.GazeTrack(1)

                basetime = datetime.datetime.now()
                self.makedata = makedata.MakeData(str(basetime.strftime("%Y,%m,%d,%H,%M")))
                #self.makedata.makefile()
                self.makedata.makeFile()
                self.makedata.openFile()
                self.makedata.makeHeader()
                self.subWin = None

                #プロパティ
                self.width = self.gazetrack.cap.get( cv2.CAP_PROP_FRAME_WIDTH)
                self.height = self.gazetrack.cap.get( cv2.CAP_PROP_FRAME_HEIGHT)

                self.xParam: list = [0, 0, 0]
                self.yParam: list = [0, 0, 0]

                self.xdis: float = 0.0
                self.ydis: float = 0.0
                self.dis: int = 50


                self.create_frame()
                self.create_widget()
                self.delay = 10
                self.play_video()

                self.com = '/dev/tty.usbserial-3552041E93'
                self.ser = serial.Serial(self.com, 9600, timeout=None)
                self.serialCheck()

        def create_frame(self):
                #フレームの作成frame1 = 背景 frame2 = ラベル
                self.frame1 = tk.Frame(self.master, width=720, height=505, bg="#C4C4C4")
                self.frame1.place(x=0, y=0)
                self.frame2 = tk.Frame(self.master, width=720, height=40, bg="#3F3F3F")
                self.frame2.place(x=0, y=0)
                self.canvas = tk.Canvas(self.frame1, width=720, height=480)
                self.canvas.pack()
        
        def create_widget(self):
                #Labelの生成
                b_camera = tk.Button(self.frame2, text = "camera", width=3, command=self.setup_window)
                b_camera.grid(row=0, column=0, padx=2, pady=2, sticky=tk.E)
                e_camera = tk.Button(self.frame2, text = "Exit", width=3, command=self.endApp)
                e_camera.grid(row=0, column=1, padx=2, pady=2, sticky=tk.E)

        def setup_window(self):
                #self.gazetrack.takePhoto()
                if self.subWin == None or not self.subWin.winfo_exists():
                        self.subWin = tk.Toplevel()
                        self.subWin.resizable(width=False, height=False)
                        self.subWin.geometry("350x150")
                        self.subWin.title("camera")
                        distance = tk.Label(self.subWin, text="distance")
                        distance.grid(row=0, column=0, padx=5, pady=2, sticky=tk.E)
                        headLabel = tk.Label(self.subWin, text="xParam")
                        headLabel.grid(row=1, column=0, padx=5, pady=2, sticky=tk.E)
                        outcameraLabel = tk.Label(self.subWin, text="yParam")
                        outcameraLabel.grid(row=2, column=0, padx=5, pady=2, sticky=tk.E)
                        
                        self.distance = tk.StringVar()
                        distanceEntry = tk.Entry(
                                self.subWin,
                                textvariable=self.distance,
                                width=20
                        )
                        distanceEntry.insert(tk.END, "0")
                        distanceEntry.grid(row=0, column=1)

                        self.head = tk.StringVar()
                        headEntry = tk.Entry(
                                self.subWin,
                                textvariable=self.head,
                                width=20
                        )
                        headEntry.insert(tk.END, "0.0")
                        headEntry.grid(row=1, column=1)


                        self.outCamera = tk.StringVar()
                        outCameraEntry = tk.Entry(
                                self.subWin,
                                textvariable=self.outCamera,
                                width=20
                        )
                        outCameraEntry.insert(tk.END, "0.0")
                        outCameraEntry.grid(row=2, column=1)
                        #incamera_label.pack()
                        self.subApply = tk.Frame(self.subWin)
                        self.subApply.grid(row=3, column=1, padx=0, pady=5, sticky=tk.W)

                        toCenterButton = tk.Button(
                                self.subApply,
                                text="toCenter",
                                command = self.toCenter
                        )
                        toCenterButton.pack(side=LEFT)
                        applyButton = tk.Button(
                                self.subApply,
                                text="Apply",
                                command = self.get_setting
                        )
                        applyButton.pack(side=LEFT)
                        cancelButton = tk.Button(
                                self.subApply,
                                text="Cancel",
                                command = self.close_sub
                        )
                        cancelButton.pack(side=LEFT)
        def toCenter(self):
                self.gazetrack.toCenter()

        def get_setting(self):
                #self.basehead = self.head.get()
                #self.baseoutcamera = self.outCamera.get()
                try:
                        #self.xParam = list(map(int, self.basehead.split(",")))
                        #self.yParam = list(map(int, self.baseoutcamera.split(",")))
                        self.dis = int(self.distance.get())
                        self.xdis = float(self.head.get())
                        self.ydis = float(self.outCamera.get())
                        
                except:
                        return

        def close_sub(self):
                self.subWin.destroy()

        def key_event(self, e):
                key = e.keysym
                if key == "p":
                        self.takePhoto()
                        '''
                        self.makedata.addData(
                                gaze_x=self.gazetrack.getAngle.gazeAngleData[0],
                                gaze_y=self.gazetrack.getAngle.gazeAngleData[1],
                                basepoint_x=self.gazetrack.getAngle.pointData[0],
                                basepoint_y=self.gazetrack.getAngle.pointData[1],
                                showpoint_x=self.gazetrack.getAngle.showPoint_x,
                                showpoint_y=self.gazetrack.getAngle.showPoint_y,
                                scale_x=self.xParam[0],
                                scale_y=self.yParam[0],
                                zeropoint_x=self.xParam[1],
                                zeropoint_y=self.yParam[1],
                                pointing=self.pointing
                        )
                        '''
                        self.makedata.addNewData(
                                gaze_x=self.gazetrack.getAngle.gazeAngleData[0],
                                gaze_y=self.gazetrack.getAngle.gazeAngleData[1],
                                basepoint_x=self.gazetrack.getAngle.pointData[0],
                                basepoint_y=self.gazetrack.getAngle.pointData[1],
                                showpoint_x=self.gazetrack.getAngle.showPoint_x,
                                showpoint_y=self.gazetrack.getAngle.showPoint_y,
                                distance=self.dis,
                                xParam=self.xdis,
                                yParam=self.ydis,
                                pointing=self.pointing,
                        )
                        
                        self.pointing = False
                if key == "s":
                        self.setup_window()
                if key == "e":
                        self.endApp()
                        self.makedata.closeFile()
                
        def endApp(self):
                self.master.destroy()

        def takePhoto(self):
                print("take")
                self.pointing = True
                if not os.path.exists("Photo"):
                        os.mkdir("Photo")
                
                nowtime = datetime.datetime.now()

                self.outputimage.save("Photo/" + str(nowtime) + ".jpg")
                self.norectimage.save("Photo/" + str(nowtime) + "noRect.jpg")
        

        def play_video(self):
                self.gazetrack.tracking(height= self.height, width= self.width, dsize= 720, distance = self.dis, xdis = self.xdis, ydis = self.ydis)
                #self.gazetrack.tracking(height= 720, width= 480, dsize= 720)
                self.outputimage = PIL.Image.fromarray(self.gazetrack.outputframe)
                self.norectimage = PIL.Image.fromarray(self.gazetrack.norectframe)
                self.image = PIL.Image.fromarray(self.gazetrack.frame)
                self.photo = PIL.ImageTk.PhotoImage(image = self.image)
                self.canvas.create_image(0, 30, image= self.photo, anchor = tk.NW)

                #csv
                '''
                self.makedata.addData(
                        gaze_x=self.gazetrack.getAngle.gazeAngleData[0],
                        gaze_y=self.gazetrack.getAngle.gazeAngleData[1],
                        basepoint_x=self.gazetrack.getAngle.pointData[0],
                        basepoint_y=self.gazetrack.getAngle.pointData[1],
                        showpoint_x=self.gazetrack.getAngle.showPoint_x,
                        showpoint_y=self.gazetrack.getAngle.showPoint_y,
                        scale_x=self.xParam[0],
                        scale_y=self.yParam[0],
                        zeropoint_x=self.xParam[1],
                        zeropoint_y=self.yParam[1],
                        pointing=self.pointing
                )
                '''
                self.makedata.addNewData(
                                gaze_x=self.gazetrack.getAngle.gazeAngleData[0],
                                gaze_y=self.gazetrack.getAngle.gazeAngleData[1],
                                basepoint_x=self.gazetrack.getAngle.pointData[0],
                                basepoint_y=self.gazetrack.getAngle.pointData[1],
                                showpoint_x=self.gazetrack.xTrack,
                                showpoint_y=self.gazetrack.yTrack,
                                distance=self.dis,
                                xParam=self.xdis,
                                yParam=self.ydis,
                                pointing=self.pointing,
                        )
                #10ms
                self.master.after(self.delay, self.play_video)
        
        def serialCheck(self):
                result = self.ser.read_all()
                if result == b"P":
                        self.takePhoto()
                self.master.after(self.delay, self.serialCheck)

def main():
        root = tk.Tk()
        app = Application(master=root)
        app.subWin = None
        root.bind("<KeyPress>", app.key_event)
        app.mainloop()

if __name__ == "__main__":
        main()