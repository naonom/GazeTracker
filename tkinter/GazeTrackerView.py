import tkinter as tk
import cv2

class View():
    def __init__(self,master,model):
        self.master = master
        self.model = model

        self.canvas = tk.Canvas(self.master,width=self.model.width,height=self.model.height)
        self.canvas.pack()

        #self.canvas.create_polygon(10,10,10,60,50,35,tag="id1")
        self.canvas.create_oval(self.model.width/2 - 20, self.model.height/2 - 20, self.model.width/2 + 20, self.model.height/2 + 20, tag="viewpoint")
        self.canvas.lift("viewpoint")
        #self.canvas.config(bg="")
        # Canvasにマウスイベント（左ボタンクリック）の追加
        self.canvas.bind('<Button-1>', self.canvas_click)
        # Canvasを配置
        self.canvas.pack(expand = True, fill = tk.BOTH)

        self.capture = cv2.VideoCapture(0)

        self.disp_id = None


    def canvas_click(self, event):
        print('click!')

    